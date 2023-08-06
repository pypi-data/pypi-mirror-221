# -*- coding: utf-8 -*-
# @Author  : zhousf
# @Function:
import os
import base64
import requests
from io import BytesIO
import numpy as np
from PIL import Image, ImageDraw, ImageOps
from pathlib import Path
import random
from PIL import Image
from zhousflib.datasets.coco import coco_bbox_vis


def _normalize_box(box, old_size, new_size, offset_x=0, offset_y=0):
    """
    box标准化
    :param box: (x_min, y_min, x_max, y_max)
    :param old_size: [img_w, img_h] 图片宽高
    :param new_size: [1000, 1000]
    :param offset_x:
    :param offset_y:
    :return:
    """
    return [
        int((box[0] + offset_x) * new_size[0] / old_size[0]),
        int((box[1] + offset_y) * new_size[1] / old_size[1]),
        int((box[2] + offset_x) * new_size[0] / old_size[0]),
        int((box[3] + offset_y) * new_size[1] / old_size[1]),
    ]


def _denormalize_box(box, old_size, new_size, offset_x=0, offset_y=0):
    """
    box反标准化
    :param box: (x_min, y_min, x_max, y_max)
    :param old_size: [img_w, img_h] 图片宽高
    :param new_size: [1000, 1000]
    :param offset_x:
    :param offset_y:
    :return:
    """
    return [
        int((box[0] - offset_x) * old_size[0] / new_size[0]),
        int((box[1] - offset_y) * old_size[1] / new_size[0]),
        int((box[2] - offset_x) * old_size[0] / new_size[0]),
        int((box[3] - offset_y) * old_size[1] / new_size[0])
    ]


def np2base64(image_np):
    img = Image.fromarray(image_np)
    base64_str = pil2base64(img)
    return base64_str


def pil2base64(image, image_type=None, size=False):
    if not image_type:
        image_type = "JPEG"
    img_buffer = BytesIO()
    image.save(img_buffer, format=image_type)

    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)

    base64_string = base64_str.decode("utf-8")

    if size:
        return base64_string, image.size
    else:
        return base64_string


def _get_buffer(data, file_like=False):
    buff = None
    if len(data) < 1024:
        if os.path.exists(data):
            buff = open(data, "rb").read()
        elif data.startswith("http://") or data.startswith("https://"):
            resp = requests.get(data, stream=True)
            if not resp.ok:
                raise RuntimeError("Failed to download the file from {}".format(data))
            buff = resp.raw.read()
        else:
            raise FileNotFoundError("Image file {} not found!".format(data))
    if buff is None:
        buff = base64.b64decode(data)
    if buff and file_like:
        return BytesIO(buff)
    return buff


def read_image(image):
    """
    read image to np.ndarray
    """
    image_buff = _get_buffer(image)

    # Use exif_transpose to correct orientation
    _image = np.array(ImageOps.exif_transpose(Image.open(BytesIO(image_buff)).convert("RGB")))
    return _image


img_file = Path(r"C:\Users\zhousf-a\Desktop\uie\33.jpg")
# classes_dict = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5"}
# image = Image.open(img_file)
# bboxes = []
# for bbox_coco in prompt_item.get("bbox"):
#     box = _denormalize_box(bbox_coco, [image.width, image.height], [1000, 1000])
#     bboxes.append([random.randint(1, 5), 1, box[0], box[1], box[2], box[3]])
# image = coco_bbox_vis.draw_bbox_label(img_file=img_file, bboxes=bboxes, classes_dict=classes_dict, show=False)
# image.show()


image = read_image(str(img_file))
image_base64 = np2base64(image)

prompt_item = {
    "content": "118±25平均560平均560",
    "result_list": [
        {
            "text": "平均560",
            "start": 11,
            "end": 16,
        }
    ],
    "prompt": "边长",
    "bbox": [[527, 174, 751, 366],
             [527, 174, 751, 366],
             [527, 174, 751, 366],
             [527, 174, 751, 366],
             [527, 174, 751, 366],
             [527, 174, 751, 366],
             [530, 465, 753, 686],
             [530, 465, 753, 686],
             [530, 465, 753, 686],
             [530, 465, 753, 686],
             [530, 465, 753, 686],
             [146, 534, 363, 761],
             [146, 534, 363, 761],
             [146, 534, 363, 761],
             [146, 534, 363, 761],
             [146, 534, 363, 761]],
    "image": image_base64,
}
