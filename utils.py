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

#判断传入的路径字符串是CSV文件还是Excel文件
def check_path_type(path):
    if os.path.isdir(path):
        return 'Folder'
    elif os.path.isfile(path):
        file_name, file_extension = os.path.splitext(path)
        return file_extension.replace('.', '')
    else:
        return 'Not Found'