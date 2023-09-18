from utils import get_file_paths
from compute import getLeadFail
from compute import getHvsFail

# paths = get_file_paths(r"C:\Users\pengcheng.yan\Desktop\work\aps日常统计\0915\0906")
# for path in paths:
#     getLeadFail(path)

paths = get_file_paths(r"C:\Users\pengcheng.yan\Desktop\work\aps日常统计\0914\0913off")
for path in paths:
    getHvsFail(path)