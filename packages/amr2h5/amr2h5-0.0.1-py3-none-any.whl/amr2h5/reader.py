import h5py
import matplotlib.pyplot as plt
import numpy as np


class H5Reader(dict):
    """
    H5 reader class based on the dict object
    The whole dataset is read into memory so reading is slow
    but plotting is fast (I think that's what we want)
    """

    non_field_keys = ["x", "y"]

    def __init__(self, h5file, fast_field=None):
        """
        Constructor for the H5Reader class
        param h5file (str): filename of the H5 file to read
        param fast_field (str): specify a single field to be read from the
        dataset, usefull when plotting a time series (it's litterally n times
        faster with n the number of fields in the dataset)
        """
        super().__init__()
        self.f = h5py.File(h5file, "r")
        # Read the grid coordinates
        self["x"] = np.array(self.f["x"])
        self["y"] = np.array(self.f["y"])
        # Read all the fields
        if fast_field is None:
            self._read_all_fields()
        # Read a single field (fast)
        elif fast_field in self.f.keys():
            ds = self.f[fast_field]
            if ds.shape[0] == len(self["y"]) and ds.shape[1] == len(self["x"]):
                self[fast_field] = np.array(ds)
        # Something's not right
        else:
            raise ValueError("Fast field not in dataset")

    def _read_all_fields(self):
        """
        Read all the H5 fields into the H5Reader class
        """
        field_keys = [ky for ky in self.f.keys() if ky not in self.non_field_keys]
        field_data = {}
        for key in field_keys:
            ds = self.f[key]
            # Just making sure
            if ds.shape[0] == len(self["y"]) and ds.shape[1] == len(self["x"]):
                field_data[key] = np.array(ds)
            else:
                print(f"Cannot read field {key}, wrong shape")
        self.update(field_data)

    def plot(self, field, **kwargs):
        """
        Plot a 2D field from the dataset
        keyword arguments can be passed to matplotlib.pyplot.pcolormesh
        see help(matplotlib.pyplot.pcolormesh) for more information
        """
        # Default colormap is not so nice
        if "cmap" not in kwargs:
            kwargs["cmap"] = "coolwarm"
        # plot plot plot
        out = plt.pcolormesh(self["x"], self["y"], self[field], **kwargs)
        # Make it well scaled
        plt.gca().set_aspect("equal")
        # add a colorbar
        plt.colorbar(out, label=field)

    def save(self, filename):
        """
        Save the current state of the dataset into a .h5 file
        """
        # Use .h5 format
        filename += ".h5"
        with h5py.File(filename, "w") as h5file:
            for key in self:
                h5file.create_dataset(key, data=self[key])
