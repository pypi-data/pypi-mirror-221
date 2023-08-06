Beamformers optimization on GPU
===============================

DAS
---
No real limitations here, if we don’t vectorize the algorithm, it just has to
be a double for-loop (along the plane waves and then the probe elements). Every
pixel is independent, so we don’t see the point of using shared memory here.
The grid / blocks can be organized in the most basic way.

However, we’ve noted that the time delays for a given position X (defined as
:math:`\tau_{n,m}(x,z)` in our equations) only depends on the dimension of the
medium we are scanning, and not on the data. It means that it can be computed
only once, and might fasten up the computation time if we extract it from our
kernel. Turned out that the time delays are actually really trivial to compute
and, since we need to loop over all the elements of the scan anyway, it ain't
much faster. Furthermore, it is also really heavy in memory as we need to keep
a matrix of size :math:`n_{x}\times n{z}\times N\times M`.


FDMAS
-----
This algorithm is a typical example of how beneficial the GPU can be for our
applications. Indeed, the multiplication of all the elements of
:math:`s_{n}(x,z)` by pairs can’t be vectorized as all the pixels of the scan
have a vector of different sizes (depending on the f#). It means that we need
to preserve a for-loop, which is really inefficient on CPU.

About the reduction step itself (the multiplication), we’ve tried two
approaches, a straightforward one, where we use one thread per pixel, each of
them doing the whole computation process, and another one where we are using
the shared memory, as described in figure below. The idea behind this second
method is to have one block per pixel, which will be composed of a few threads,
each of them dedicated to one of the pair multiplication. Thus, the
parallelization is reinforced.

If the idea of the second method was programmatically interesting (and might be
useful later), it appears that the multiplication process was way too trivial
to gain from being parallelized and we are actually losing time when
synchronizing the threads after the multiplication steps.

.. image:: ../images/fdmas_optim_gpu.png
   :width: 600
   :align: center


p-DAS
-----
There is nothing specific here, the implementation can’t be more parallelizable
than DAS, and we can do the implementation the same way, just changing the
reduction step.


Capon
-----
For this algorithm, we need to invert the covariance matrix for every pixel.
Since these matrices have various sizes depending of the depth in the scan and
the f#, it is not trivial. We will face two issues: first the inversion itself
needs to be implemented completely, which isn’t easy, and second, we’ll need to
allocate an array with a dynamic size for our covariance matrix, since its size
is not fixed for every element of the grid.

a) The covariance matrix
^^^^^^^^^^^^^^^^^^^^^^^^
We need to invert the covariance matrix within the kernel, which is quite
complicated to implement efficiently from scratch, especially with matrices of
various sizes. However, as stated in [1], we note that all our covariance
matrices are semi-definite positive. Indeed, the covariance matrix can be
defined by the following equation, given :math:`X=[X_1, X_2, ..., X_n]`:

.. math::
    R=X.X^{H}=\begin{bmatrix}
    {X_{1}\cdot \overline{X_{1}}}&{\dots}&{X_{1}\cdot \overline{X_{n}}}\\
    {\vdots}&{\ddots}&{\vdots}\\
    {X_{n}\cdot \overline{X_{1}}}&{\dots}&{X_{n}\cdot \overline{X_{n}}}\\
    \end{bmatrix}=\begin{bmatrix}
    {\left|X_{1}\right|^{2}}&{\dots}&{X_{1,n}}\\
    {\vdots}&{\ddots}&{\vdots}\\
    {\overline{X_{1,n}}}&{\dots}&{\left|X_{n}\right|^{2}}\\
    \end{bmatrix}

And we observe that the diagonal elements are real numbers, and that the lower
triangular matrix is the conjugate of the upper triangular matrix, so, for any
signal, we have :math:`R=R^H`. When we are working with real signals (RFs), we
observe the same properties, but, as the conjugate of a real number is the
number itself, the matrix is symmetric, which means that :math:`R=R^T`.

Given this, we can use the Cholesky decomposition to decompose a matrix into a
dot product of a lower triangular matrix :math:`T_{low}` with its conjugate
transpose:

.. math::
    R=T_{low}\,.T_{low}^{H} \tag{1}

Once we have done this decomposition, we can also define the inverse of R as:

.. math::
    R^{-1}=\left(T_{low}\cdot T_{low}^{H}\right)^{-1}=T_{low}^{-H}\cdot T_{low}^{-1} \tag{2}

This method is great for us because it allows us to invert any covariance
matrix (as long as it is semi-definite positive) using both Cholesky
decomposition and the inversion of a triangular matrix. Both of these
operations are quite easy and straightforward to implement.

b) Memory allocation
^^^^^^^^^^^^^^^^^^^^
As discussed in the GPU section, we need to know beforehand how much memory is
needed. However, the size of our covariance matrices changes with the depth of
the medium: it is not the same for all the kernels. Indeed, if we have 128
probe elements, we know that the covariance matrix will have a dimension of
:math:`L \times L`, with  :math:`L < \frac{N}{2}`. It means that the matrices
will be, at most, (:math:`64 \times 64`), but it also could be very small on
the shallowest pixels.

The most intuitive solution here is to allocate the maximum needed amount of
memory for all the kernels, even if we know that most of it won’t be used for
most of the medium. It means that, for every kernel, we’d allocate
:math:`64 \times 64=4096` complex numbers, even if we only need let’s say 100
memory allocation (:math:`L=10`). A simplification can be done though,
considering that our matrix is demi-definite positive, we know that, for any
data, we have :math:`R=R^H`, so we can afford to only define half our matrices,
since the other half is deducible. That said, we only need
:math:`L \times \frac{L+1}{2}` instead of :math:`L^2` allocations.

Another solution could be to subdivide the image in different areas given their
depth, so we could adapt their memory needs. The figure 1 shows a proposition
on how to organize this implementation. This would probably optimize the GPU
occupancy and would be worth a try.

.. image:: ../images/capon_gpu_allocation.png
   :width: 400
   :align: center

Something else to consider is also the way we are using our memory. We’ve seen
that our covariance matrices can be very heavy for deeper points in the medium,
so we need to use it smartly. Indeed, many algorithms are built in order to
minimize the computation complexity, but don’t take into consideration the
memory needs. In our algorithms, we will prefer inplace implementations (where
we don’t need to allocate the covariance matrix twice).

c) Allowed parallelization
^^^^^^^^^^^^^^^^^^^^^^^^^^
When implementing a new algorithm, here the Cholesky decomposition or the
inverse of a triangular matrix, we can propose a straightforward implementation
where a single thread is doing the whole process, or we can think of a way to
parallelize it. However, it needs to be done carefully, as some elements of the
matrix are dependent on each other.

The figure 2, inspired from [2] is an example of the data dependencies problems
we are facing on the typical implementation of Cholesky. It is showing that we
can’t parallelize the operation along the columns of our matrices, as the
elements depend on other columns. However, the figure 12b shows that, if we are
doing it row by row, the only dependencies are the diagonal elements. So as
long as we compute the diagonal elements at first, it is fine to parallelize
the processes along a column. In our case, our matrices have various size, up
to :math:`\frac{N}{2} \times \frac{N}{2} = (64 \times 64)`. Which means that,
at best, we can parallelize 63 processes for the first column, 62 for the
secondth, ... and finally only one for the last column. This could be
implemented for research purposes, but it seems to be a bad way to optimize GPU
occupancy as, most of the time, the GPU would have unworking threads.

.. image:: ../images/capon_cholesky.png
   :width: 500
   :align: center


d) Detail of parallel Cholesky
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Cholesky decomposition [3] can determine the lower triangular matrix
:math:`T_{low}` which can verify the following dot product:
:math:`R=T_{low}.T_{low}^H`. The implementation is quite straightforward, we
can observe a pattern. For the diagonal elements, we have:

.. math::
    T_{k,\,k}={\sqrt[]{a_{k,k}-\sum_{j=1}^{k-1}T_{k,j}^{2}}} \tag{3}

While, for the elements below the diagonal:

.. math::
    T_{i,\,k}=\frac{1}{T_{k,\,k}}\left(a_{i,k}-\sum_{j=1}^{k-1}T_{i,j}\cdot T_{k,j}\right) \tag{4}

The above formulas can be performed inplace, as long as we process it from top
to bottom.


e) Detail of parallel Triangular matrix inversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Inverse of the triangular matrix [4] is easy to compute as we can go line
by line and perform forward substitution to define the coefficients of the
columns where all the other elements are known. We can then define the inverse
using, for the diagonal elements, the formula:

.. math::
    \left(T_{low}\right)_{k,k}^{-1}=\frac{1}{\left(T_{low}\right)_{k,k}} \tag{5}

While we have below the diagonal:

.. math::
    \left(T_{low}\right)_{i,k}^{-1}=-\frac{1}{\left(T_{low}\right)_{k,k}}\cdot\sum_{j=i}^{k-1}\left(T_{low}\right)_{i,k}\cdot\left(T_{low}\right)_{j,i}^{-1} \tag{6}

(and the rest, above the diagonal, is set to zero).


- [1] Multi-operator Minimum Variance AdaptiveBeamforming Algorithms
  Accelerated with GPU, Chen & al.
- [2] Parallel Implementations of the Cholesky Decomposition on CPUs and GPUs,
  Tarasconi Reschel
- [3] Cholesky Decomposition, Rosetta,
  https://rosettacode.org/wiki/Cholesky_decomposition
- [4] Matrix Algorithms: Volume 1: Basic Decompositions, Stewart & al.
