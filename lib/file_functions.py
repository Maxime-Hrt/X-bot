import os
import numpy as np


def get_file_names(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


def get_file_paths(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


def split_list(folder_path, split_indices):
    images = get_file_paths(folder_path)
    sub_arrays = np.array_split(images, split_indices)
    sub_arrays = [list(sub_array) for sub_array in sub_arrays]
    return sub_arrays


