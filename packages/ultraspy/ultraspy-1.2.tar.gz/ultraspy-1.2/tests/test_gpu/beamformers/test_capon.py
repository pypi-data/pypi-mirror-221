"""Unit test file to test our Capon beamformer.
"""
import os
import numpy as np

from ultraspy.io.reader import Reader
from ultraspy.scan import GridScan
from ultraspy.beamformers.capon import Capon
from ultraspy.gpu import gpu_utils
from ultraspy.config import cfg


def test_capon():
    # Get the data
    rsc_dir = cfg.PATHS_RESOURCES
    reader = Reader(os.path.join(rsc_dir, 'picmus_simu_rfs.hdf5'), 'picmus')
    x = np.linspace(-5, 5, 75) * 1e-3
    z = np.linspace(20, 30, 200) * 1e-3
    scan = GridScan(x, z)
    beamformer = Capon()
    beamformer_cpu = Capon(on_gpu=False)
    beamformer.automatic_setup(reader.acquisition_info, reader.probe)
    beamformer_cpu.automatic_setup(reader.acquisition_info, reader.probe)
    indices = [37]
    data = reader.data[0, indices].copy()
    beamformer.update_setup('f_number', 1.75)
    beamformer_cpu.update_setup('f_number', 1.75)
    beamformer.update_setup('transmissions_idx', indices)
    beamformer_cpu.update_setup('transmissions_idx', indices)

    # Send to GPU
    d_data = gpu_utils.send_to_gpu(data, np.float32)

    # Beamformed
    d_beamformed = beamformer.beamform(d_data, scan)
    beamformed = d_beamformed.get()
    beamformed_cpu = beamformer_cpu.beamform(data, scan)
    tol = np.max(beamformed_cpu) * 1e-4
    assert np.allclose(beamformed, beamformed_cpu, atol=tol)

    # Should compare with other methods, such as diagonal loading or so
