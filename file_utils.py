import pathlib


def get_file_names_from_folder(name, mask = '*.PNG*'):
    folder_path = pathlib.Path(name)
    file_list = list(folder_path.rglob(mask))
    img_paths_list = [str(path) for path in file_list]
    return img_paths_list