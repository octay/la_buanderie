#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image  # pip install pillow

import os


def combine2Pdf(folder_path, pdf_file_path):
    files = os.listdir(folder_path)
    pngFiles = []
    sources = []
    for file in files:
        if 'jpg' in file:  # if png, change it to check every png
            pngFiles.append(folder_path + '\\' + file)  # if you ve not added r'\' in folder_path
    pngFiles.sort(key=lambda x: eval((x.split('(')[1]).split(')')[0]))
    '''
    write your own key here
    example : 蓝宝书15版 (1).jpg
    x.split('(')[1] → 1).jpg
    (x.split('(')[1]).split(')')[0] → 1
    eval((x.split('(')[1]).split(')')[0]) → 1 (type : int)
    '''

    print(folder_path)
    print(pngFiles)

    output = Image.open(pngFiles[0])
    output = output.convert("RGB")
    pngFiles.pop(0)  # pop first pic
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGBA":  # to avoid error occurring
            pngFile = pngFile.convert("RGB")
        sources.append(pngFile)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)


if __name__ == "__main__":
    main_folder_path = r"D:\日语N1\にほんご\《D蓝宝书》\15版"  # write your path here
    main_pdf_file_path = r"D:\日语N1\にほんご\《D蓝宝书》\蓝宝书N1-N5 15.pdf"  # write expected pdf path here
    combine2Pdf(main_folder_path, main_pdf_file_path)
