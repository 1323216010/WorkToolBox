import os

# 遍历当前文件夹，并获取所有文件的绝对路径
def get_file_paths(folder_path, include_subfolders=False):
    file_paths = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        if not include_subfolders and foldername != folder_path:
            continue
        for filename in filenames:
            file_paths.append(os.path.join(foldername, filename))
    return file_paths
