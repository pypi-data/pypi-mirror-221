"""Unit test file to test our Capon beamformer.
"""
import os
import numpy as np
import pytest

from ultraspy.io.reader import Reader
from ultraspy.scan import GridScan, PolarScan
from ultraspy.beamformers.capon import Capon
from ultraspy.config import cfg


def test_capon_rfs():
    # High level checks for Capon
    # Get the data
    rsc_dir = cfg.PATHS_RESOURCES
    reader = Reader(os.path.join(rsc_dir, 'picmus_simu_rfs.hdf5'), 'picmus')
    x = np.linspace(-20, 20, 300) * 1e-3
    z = np.linspace(5, 50, 600) * 1e-3
    scan = GridScan(x, z, on_gpu=False)
    beamformer = Capon(on_gpu=False)
    beamformer.automatic_setup(reader.acquisition_info, reader.probe)
    pw = [37]
    data = reader.data[0, pw]
    beamformer.update_setup('transmissions_idx', pw)

    # Beamformed
    # beamformed = beamformer.beamform(data, scan)

    # Should perform some high level tests, also with diagonal loading etc
