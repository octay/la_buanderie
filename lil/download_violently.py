import os
from urllib.request import urlretrieve

os.makedirs('./img/', exist_ok=True)  # avoiding error interrupt
image_url_part = r'https://i3.nhentai.net/galleries/1070581/'  # check manually
total_num = 159  # check manually


def urllib_download(image_url: str, ind: int):
    urlretrieve(image_url, r'./img/' + str(ind) + '.jpg')


for i in range(1, total_num + 1):
    urllib_download(image_url_part + str(i) + r'.jpg', i)
    print("downloading: {} / {}".format(i, total_num))

print('downloading accomplished')  # print info
