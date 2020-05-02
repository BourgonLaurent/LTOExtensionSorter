""" LTO's Extension Sorter

Sort a folder with extension

"""

import os
import shutil

WORKDIR = os.path.join(os.getcwd())

files_to_move = [f for f in os.listdir(WORKDIR)
                 if os.path.isfile(os.path.join(WORKDIR, f))]

extension_dict = dict()

for file_tm in files_to_move:
    # Get the clean extension of the file and lower it
    ext = os.path.splitext(file_tm)[-1].replace('.', '').lower()

    if ext:  # Be sure the extension isn't absent
        if not ext in extension_dict:  # Check if a file with this extension already exists
            extension_dict[ext] = list()

        extension_dict[ext].append(file_tm)


for ext, file_tm_list in extension_dict.items():
    if not os.path.isdir(os.path.join(WORKDIR, ext)):
        os.mkdir(os.path.join(WORKDIR, ext))

    for file_tm in file_tm_list:
        shutil.move(os.path.join(WORKDIR, file_tm),
                    os.path.join(WORKDIR, ext))
