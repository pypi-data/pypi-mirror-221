.. _probe_class:

The Probe class
---------------
The Probe class can be of three kind: either Linear, Convex or Matricial. Each
of them have similar parameters inherited from their parent class, including:

- :code:`name`: The name of the probe
- :code:`geometry_type`: The kind of the probe (linear, convex or matricial)
- :code:`geometry`: The position of each elements (of shape (3, nb_elements),
  3D coordinates)
- :code:`central_freq`: The estimated central frequency of the probe
- :code:`bandwidth`: The estimated bandwidth of the emitted signals (in %)

.. image:: ../images/probes.png
   :width: 600
   :align: center


Possible to create multiple ways
--------------------------------
There are two ways to build probes:

Load an existing one
^^^^^^^^^^^^^^^^^^^^
The probe can be stored within an :code:`.ini` file, templates are available
within the :code:`probes/configs/` directory of the source code. The following
sections are expected:

- [General]: With the name and geometry type of the probe
- [Geometry]: Contains information about the probe. If linear, the number of
  elements and the pitch are sufficient. If convex, the radius of the probe is
  also expected. If matricial, The number of elements has to be 2D ([lateral,
  elevational]), and same for the pitch. The empty lines can also be provided,
  defining, in 2D, the empty lines occurence pattern within the matrix.
- [Transmission] Contains the emission values of the probe (central frequency
  and bandwidth)

Below is an example of `l7-4.ini` file, for the 128 linear L7-4 probe:

.. code-block:: ini

    [General]
    name: L7-4
    constructor: ATL
    type: linear

    [Geometry]
    nb_elements: 128
    pitch: 0.298e-3

    [Transmission]
    central_freq: 5.208e6
    bandwidth: 80


Create a new one
^^^^^^^^^^^^^^^^
Sometimes, one might need to create his own probe (with fixed physical
positions for example, or adjusted bandwidth). In that case, the user must
provide a matlab file containing X, Y, and Z, three vectors with the
coordinates of each element of the probe. The central frequency must also be
provided, and a bandwidth is preferred.
