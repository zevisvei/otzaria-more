import os

import os

def list_files_and_folders(path_to_folder):
    files_list = []
    for _, _, files in os.walk(path_to_folder):
        files_list.extend(files)
    return files_list


otzaria_library_path = "/workspaces/alll/otzaria-library/אוצריא"
folder_path = "לא ערוך"
otzaria_library_files = list_files_and_folders(otzaria_library_path)
files_list = list_files_and_folders(folder_path)
list_names = []
for i in otzaria_library_files:
    if i in files_list:
        print(i)
        list_names.append(i)
with open(f"{folder_path}.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(list_names))

