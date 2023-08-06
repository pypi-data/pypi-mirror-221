Torch interoperability
======================

Send data to torch
------------------
When using `ultraspy` on GPU, the objects are sent to GPU using the `cupy`
library, which is dealing with the pointers to know where to find the data
within the GPU device.

If you aim to use some Deep Learning algorithm, or simply to run your own
algorithm using the `torch` library, it is possible to send the information to
the torch library. You can do it the following way:

.. code-block:: python
    :linenos:

    import numpy as np
    import cupy as cp
    import torch

    # Some random data
    a = np.random.randint(10, size=(5, 6))

    # Send it to device using cupy, as ultraspy does
    cupy_a = cp.array(a, np.float32)

    # Transfer its pointer to torch so it can be used in both libraries
    torch_a = torch.as_tensor(cupy_a, device='cuda')


Now, the array :code:`a` is available both on CPU (the numpy array called
:code:`a`) and on GPU (accessible both by `cupy` with :code:`cupy_a` and
`torch` with :code:`torch_a`). Note that both :code:`cupy_a` and
:code:`torch_a` refers to the same data on GPU, meaning that if you update one,
the other one will also be updated. Let's say for example that you want to
convert the data as decibel using both libraries you can do:

.. code-block:: python
    :linenos:

    # Normalize the data using cupy
    cupy_a /= cupy_a.max()

    # Convert to log using torch
    torch.log10(torch_a, out=torch_a)

    # Get the data back on CPU
    cpu_cupy_a = cupy_a.get()
    cpu_torch_a = torch_a.cpu()

    # Both are equal
    print(np.allclose(cpu_cupy_a, cpu_torch_a))


All good. Few things to consider here though. It works as long as we are
modifying directly the device array. Make sure that all the operations are
inplace, and won't allocate a new array in memory in the process. If a new
array is allocated by either `cupy` or `torch`, the other lib won't be aware of
the update:

.. code-block:: python
    :linenos:

    # Operation is modifying both libraries
    cupy_a /= cupy_a.max()
    print(np.allclose(cupy_a.get(), torch_a.cpu()))  # True

    # The array in cupy is divided by max, then stored in a new array on GPU,
    # that happens to have the same name, torch and cupy are now different
    # pointers
    cupy_a = cupy_a / cupy_a.max()
    print(np.allclose(cupy_a.get(), torch_a.cpu()))  # False


Similarly in `torch`:

.. code-block:: python
    :linenos:

    # The log10, by default, is allocating a new array, but we can specify the
    # output location. If it is the same as before, it'll still be the same
    # pointer as cupy
    torch.log10(torch_a, out=torch_a)
    print(np.allclose(cupy_a.get(), torch_a.cpu()))  # True

    # A new pointer is created, cupy array is detached from torch'
    torch_a = torch.log10(torch_a)
    print(np.allclose(cupy_a.get(), torch_a.cpu()))  # False


That's it! And if you want to go the other way, and converting your torch
Tensor to a cupy array, you should use:

.. code-block:: python
    :linenos:

    a = np.random.randint(10, size=(5, 6))
    torch_a = torch.as_tensor(a)
    cupy_a = cp.asarray(torch_a)


Load a Deep Learning model
--------------------------
A good way to call a Deep Learning model from `ultraspy` could be to embed it
within a Singleton class. That way, we can ensure that the model is
instantiated only once. Any other way would work too based on your application,
but we'll focus on the Singleton in this example.

Let's imagine we've trained a network to process three tilted plane waves to
produce results as good as if we had sent 31 plane waves. A way to embed it
could be:

.. code-block:: python
    :linenos:

    class MyModelSingleton:
        # General information
        _instance = None
        _model = None
        _weights = "torch_models/my_model_weights.pth"

        def __new__(cls, *args, **kwargs):
            # Initializer, only once
            if cls._instance is None:
                cls._model = MyModelClass().to("cuda")
                cls._model.load_state_dict(torch.load(cls._weights))
                cls._model.eval()
                cls._instance = super().__new__(cls)
            return cls._instance

        def prepare_data(self, d_data):
            # Prepare the data, and transfer its pointer to torch
            return torch.as_tensor(d_data, device='cuda')

        def run_inference(self, t_data):
            # Runs the inference and return the prediction
            with torch.inference_mode():
                prediction = self._model(t_data)
            return prediction

        def back_to_cupy(self, t_data):
            # Returns the data to the cupy lib
            return cp.asarray(t_data)

That way, our function would be very simple:

.. code-block:: python
    :linenos:

    def deep_compound(d_beamformed):
        # The model is ready for use after the first instantiation
        model = CidNetSingleton()

        input_model_tensor = model.prepare_data(d_beamformed)
        prediction = model.run_inference(input_model_tensor)
        return model.back_to_cupy(prediction)
