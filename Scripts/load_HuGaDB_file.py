"""Function for downloading data from HuGaDB file."""
import numpy as np

def load_HuGaDB_file(path_to_file):
    """Read HuGaDB data from file and get numpy matrix
        Parameters:
            path_to_file: string
                path to HuGaDB file.
        Return: 2d-array 
            Data in numpy format 
    """
    return np.genfromtxt(path_to_file, delimiter='\t', skip_header=4)