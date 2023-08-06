Capon algorithm
===============

Algorithm
---------

The SCB (Standard Capon Beamforming) [1] algorithm is an adaptive beamforming
technique, which means that it is computing a ponderation vector of weights to
apply to our delayed vectors :math:`s_{n}(x,z)` based on the data. It is then
supposed to decide which data is relevant or not based on their coherence
altogether.

In order to get the weighting vector, we need to compute a covariance matrix
:math:`R(x,z)` over the delayed vector and to reduce its variance. Then, given
a steering vector am (direction of the elements), we can determine the weights
which minimize the variance of our covariance matrix with the Capon formula:

.. math::
    w_{m}\left(x,z\right)=\frac{R\left(x,z\right)^{-1}\cdot a_{m}}{a_{m}^{H}\cdot R\left(x,z\right)^{-1}\cdot a_{m}} \tag{1}

with H the operator for the Hermitian conjugate. In our case, we compensate for
the directions of our signal when we compute the delays, so the steering vector
is only composed of 1.

However, this method is not really efficient in our applications (the steering
vector is not precisely known, and there is a lot of noise in medical imagery),
so we need to make it more robust. The next sections are describing some
variations we have implemented for our applications.


Spatial smoothing
^^^^^^^^^^^^^^^^^
The idea here is to subdivide the delayed vector into K superposed windows of
size L. Then if a window has M number of elements, we’ll have the relation
:math:`K=M-L+1`. These windows change the equation of the covariance matrix
which now can be defined as:

.. math::
    R\left(x,z\right)=\frac{1}{K}\left(\sum_{k=1}^{K}X_{k}\left(x,z\right)\cdot X_{k}\left(x,z\right)^{H}\right) \tag{2}

with :math:`X_{k}(x,z)` the vector of :math:`s_{n}(x,z)` of the window k.

.. image:: ../images/capon_windows.png
   :width: 400
   :align: center

We should note that this is changing the resolution of our image, and thus of
the weighting vector, which means that we should define L carefully, as it is a
trade-off between resolution and the precision of the estimation of the
covariance matrix. Also we should respect :math:`L < \frac{N}{2}` if we want to
make sure R is invertible, as stated in [2].

Once we’ve computed the new covariance matrix, inverted it, and applied Capon,
we can deduce w and have the new beamformed value:

.. math::
    r_{RCB-SS}\left(x,z\right)=\sum_{l=1}^{L}w_{l}\left(x,z\right)\cdot\left(\sum_{k=1}^{K}X_{k,l}\left(x,z\right)\right) \tag{3}



Diagonal Loading
^^^^^^^^^^^^^^^^
This method is surcharging the covariance matrix using a coefficient
:math:`\lambda`. The concept here is to add a Gaussian noise which forces the
algorithm to take into consideration the uncertainties. When :math:`\lambda` is
weak, these uncertainties are ignored, while they are overestimated when it is
too strong. It is not intuitive to define, as stated in [2,3,4], and a deeper
study would be relevant here. In the case of our project, we’ll define  as in
[3], which is: :math:`\lambda=\frac{tr(R)}{\delta . L}`, with :math:`tr(R)` the
trace of the covariance matrix. :math:`\delta` is left free to define to the
user (from 1 to 1000). Then the new covariance matrix (overloaded) is defined
as (with I the identity matrix):

.. math::
    R_{DL}\left(x,z\right)=\lambda\cdot I\cdot R\left(x,z\right) \tag{4}

The other equations (1 and 3) remain unchanged, but are using the new
covariance matrix.


Forward Backward
^^^^^^^^^^^^^^^^
Same as for the Diagonal Loading, this variation is changing the covariance
matrix, using the following:

.. math::
    R_{FWBW}\left(x,z\right)=\frac{1}{2}\left(R\left(x,z\right)\,+\,\left(J\cdot R\left(x,z\right)^{T}\cdot J\right)\right) \tag{5}

Considering the exchange matrix:

.. math::
    J=\begin{bmatrix}
    {0}&{\cdots}&{1}\\
    {\vdots}&{\ddots}&{\vdots}\\
    {1}&{\cdots}&{0}\\
    \end{bmatrix}

The new covariance matrix can then be replaced in the other equations (1 and 3)
to define the new weights.


Extension to In-Phase Quadrature data
-------------------------------------
The IQs version is very similar to the RFs version here. Indeed, as long as we
are doing the phase rotation in our delays vector, and we’re doing the
Hermitian conjugate (and not only the Transpose, which could work for RFs),
nothing changes.


- [1] Robust Minimum Variance Beamforming, Lorenz & al.
- [2] Spectral Analysis of Signals, Stoica & al.
- [3] Adaptive beamforming applied to medical ultrasound imaging, Synnevag & al.
- [4] Efficient method to determine diagonal loading value, Ma & al.
