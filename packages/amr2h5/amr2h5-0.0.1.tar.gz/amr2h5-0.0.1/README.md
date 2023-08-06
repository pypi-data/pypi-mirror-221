# AMR Block data to H5 converter

This python package can be used to convert AMR block data files to the H5 format with covered grid arrays at the maximum refinement level. 

Right now only 2D AMR files are supported, support for 3D dataset will likely be for the creation of slices as creating a 3D covered grid array would not be practical in terms of file size.

This python package relies heavily on the `yt` package to read AMR plotfiles.

## Installation

```bash
pip install amr2h5
```

## Usage

- The `AMR2H5Converter` class creates a single `.h5` file from a AMR plotfile directory. All the fields are keept and the AMR Level is added to the dataset. The `x` and `y` coordinates at the highest refinement level are added as 1D arrays. The `return_opened` option can be used to dynamically read plotfiles into 2D arrays.
- The `H5Reader` class reads all the data from a converted AMR plotfile into a dictionnary with all the fields as keys and 2D arrays for all the dataset. The `fast_field` option can be used to read a single field (faster), this is usefull when analyzing time series data for a single field.

## Example

```python
from amr2h5 import AMR2H5Converter
from amr2h5 import H5Reader

# Convert a single plotfile
AMR2H5Converter('plt02000') # New file plt02000.h5 is created

# Convert and read a single plotfile
 # New file plt02000.h5 is created and read
dataset = AMR2H5Converter('plt02000', return_opened=True)

# Read a converted file
dataset = H5Reader('plt02000.h5') # dataset is a dict with the whole dataset

# Reader a single field from file (faster)
# dataset_temp contains only coordinates and 'temp' field
dataset_temp = H5Reader('plt02000.h5', fast_field='temp')

```