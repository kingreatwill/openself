import io

from PIL import Image


def is_img(name):
    if name.lower() in Image.registered_extensions():
        return True
    return False


def to_mimetype(extension):
    save_format = Image.registered_extensions()[extension.lower()]
    return "image/{}".format(save_format.lower())


def thumbnail(file, format, width=0, height=0, force="resize", resample=Image.ANTIALIAS, **kwargs):
    # quality=95
    width = int(width)
    height = int(height)
    # 判断是否需要处理图片
    if (width <= 0 or height <= 0) and force == "resize" and len(kwargs) == 0:
        return file
    img = Image.open(file)
    ori_width, ori_height = img.size
    if width <= 0 or height <= 0:
        width = ori_width
        height = ori_height

    if force in ("crop_center", "1"):
        # 中心裁剪:center_crop;
        left = (ori_width - width) / 2
        top = (ori_height - height) / 2
        right = (ori_width + width) / 2
        bottom = (ori_height + height) / 2
        new_img = img.crop((left, top, right, bottom))
    else:
        # resize;
        new_img = img.resize((width, height), int(resample))

    byte_io = io.BytesIO()
    save_format = Image.registered_extensions()[format.lower()]
    new_img.save(byte_io, format=save_format, **kwargs)
    byte_io.seek(0)
    # params_size = ("width", "height", "force")
    # extra_args = {"size": size, "thumbnail_size": thumbnail_size}
    return byte_io
