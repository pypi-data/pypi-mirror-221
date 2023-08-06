.. _scan_class:

The Scan class
---------------
The Scan class defines the area of interest where to perform the beamforming.
It can be either of a regular grid shape (GridScan) or with polar coordinates
(PolarScan). You also can create your own (such as an irregular grid, with a
zoom or so in a given ROI), as long as it inherits the Scan parent class. If
you do so, keep in mind that some methods would need a specific attention. For
example, the compute_envelope method on beamformed RFs is using the axial
resolution to compute the beamformed sampling frequency, or FDMAS requires to
downsample / upsample the data by default. Those standard methods won't work
on irregular grid.

It expects in any case:

- :code:`on_gpu`, :code:`is_3d`: General parameters defining if the scan is
  within the GPU memory or not, and if the grid must be 2D or 3D
- :code:`pixels`: contains the coordinates of each of the points of the scan,
  of shape (2, nb_lateral, nb_axial) for 2D
- :code:`bounds`: set the minimum values for each dimension
- :code:`nb_x`, :code:`nb_y`, :code:`nb_z`: set the resolution of the x, y and
  z axes, by convention respectively the lateral, elevational and axial
  dimensions

The pixels are the coordinates used for beamforming.
