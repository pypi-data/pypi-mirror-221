import os
import unittest

import h5py

from amr2h5 import AMR2H5Converter, H5Reader


class TestAMR2H5Converter(unittest.TestCase):
    def test_converter(self):
        out = AMR2H5Converter("assets/plotfile")
        self.assertIsInstance(out, AMR2H5Converter)
        self.assertIsInstance(out, h5py.File)

    def test_converter_return_opened(self):
        out = AMR2H5Converter("assets/plotfile", return_opened=True)
        self.assertIsInstance(out, AMR2H5Converter)
        self.assertIsInstance(out, h5py.File)
        self.assertEqual("assets/plotfile.h5", out.filename)


class TestH5Reader(unittest.TestCase):
    def test_read(self):
        ds = H5Reader("assets/plotfile.h5")
        self.assertIsInstance(ds, dict)
        self.assertIsInstance(ds, H5Reader)
        self.assertIn("x", ds.keys())
        self.assertIn("y", ds.keys())
        self.assertTrue(len(ds.keys()) > 3)

    def test_read_fast_field(self):
        ds = H5Reader("assets/plotfile.h5", fast_field="temp")
        self.assertIn("temp", ds.keys())
        self.assertIsInstance(ds, dict)
        self.assertIsInstance(ds, H5Reader)
        os.remove("assets/plotfile.h5")


if __name__ == "__main__":
    unittest.main()
