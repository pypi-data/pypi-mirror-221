import logging
import os

import h5py
import numpy as np
import yt


class AMR2H5Converter(h5py.File):
    def __init__(self, fname, return_opened=False):
        """Constructor for the converter"""
        # Load the AMR file
        logging.disable()
        ds = yt.load(fname)
        if ds.domain_dimensions[2] != 1:
            raise NotImplementedError("Cannot convert 3D file (yet)")
        # Get the covering grid
        grid = self.compute_covering_grid(ds)
        # Overwrite and create file
        h5fname = ".".join([fname, "h5"])
        if h5fname in os.listdir():
            os.remove(h5fname)
        super().__init__(h5fname, "w")
        # Create a H5 dataset from the grid
        for key in grid.keys():
            data = grid[key]
            self.create_dataset(key[1], data=np.transpose(data[:, :, 0]))
        # Add the gridpoints values
        x_values = np.linspace(grid.left_edge[0], grid.right_edge[0], grid.shape[0])
        self.create_dataset("x", data=x_values)
        y_values = np.linspace(grid.left_edge[1], grid.right_edge[1], grid.shape[1])
        self.create_dataset("y", data=y_values)
        # Close the written file and reopen as read
        self.close()
        if return_opened:
            super().__init__(h5fname, "r")

    def compute_covering_grid(self, ds):
        """
        Compute a smoothed covering grid for all the
        fields in the domain at the maximum AMR level
        """
        # Get the max level domain dimensions
        dims = [0, 0, 0]
        dims[:2] = ds.domain_dimensions[:2] * 2**ds.max_level
        dims[2] = ds.domain_dimensions[2]
        # Create the covering grid
        ds.force_periodicity()  # Yt is wack
        # Making the grid
        fields = ds.field_list
        # Add the AMR grid level
        fields.append(("index", "grid_level"))
        # Compute the smoothed covering grid
        grid = ds.smoothed_covering_grid(
            level=ds.max_level, dims=dims, fields=fields, left_edge=ds.domain_left_edge
        )
        return grid
