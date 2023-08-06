.. _reader_class:

The Reader class
----------------
The Reader class is used to automatically read data in a given format, and to
automatically convert it within the expected format for `ultraspy`. A few are
supported, although some refactoring should be done for most of them to make
sure they are really flexible to any situation we can face.

- :code:`ultraspy` format: the default format, no conversion is made, simply
  reads the file
- :code:`dbsas` format: the format of the data for the systems from the TPAC
  company (Explorer and Pioneer). Note that when data is acquired with a TPAC
  system but using the ultraspy GUI, the recorded data will be of the format
  `ultraspy`
- :code:`picmus` format: the data from the PICMUS challenge
- :code:`must` format: basically the rotating disk file from the MUST toolbox


Additional readers are quite high-levels, and expect very specific format, read
their code before using them:

- :code:`simus` format: Data we've simulated using SIMUS, and that we've saved
  in a specific way. Nothing complicated, but there is no rule, so not all the
  data from SIMUS will have the same format
- :code:`simus_3d` format: Same for 3D simulations


The following Readers were implemented a very long time ago, and haven't been
maintained since, it is not recommended to use them:

- :code:`vera` format: the data format of acquisitions made with a Verasonics
  machine. Similarly to SIMUS, there is no dedicated way to save the data, so
  each user can do it the way he wants. This Reader is however based on the TX,
  Trans, Receive, etc. objects tho, so you can use some of it. This has only
  been tested for simple acquisitions (simple signals, plane waves only, etc.)
- :code:`ulaop` format: This has only been tested, a long time ago, for simple
  acquisitions (simple signals, plane waves only, etc.). This probably won't
  work fine


