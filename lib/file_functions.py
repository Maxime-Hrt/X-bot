import os


def get_file_names(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


def get_file_paths(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


def generate_pattern(folder_path):
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    if (file_count - 1) % 3 == 0:
        pattern = list(range(1, file_count + 1, 3))
    else:
        pattern = list(range(1, file_count, 3)) + [file_count]
    return pattern


def custom_split(array, indices):
    sub_arrays = []
    last_index = 0
    for index in indices:
        sub_array = array[last_index:index]
        if sub_array:
            sub_arrays.append(sub_array)
        last_index = index
    return sub_arrays
