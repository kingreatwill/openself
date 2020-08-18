import io

from PIL import Image


def is_img(name):
    if name.lower() in Image.registered_extensions():
        return True
    return False


def thumbnail(file, width, height, format, force="resize", resample=Image.ANTIALIAS, **kwargs):
    # quality=95
    width = int(width)
    height = int(height)
    img = Image.open(file)
    if force in ("crop_center", "1"):
        # 中心裁剪:center_crop;
        ori_width, ori_height = img.size
        left = (ori_width - width) / 2
        top = (ori_height - height) / 2
        right = (ori_width + width) / 2
        bottom = (ori_height + height) / 2
        new_img = img.crop((left, top, right, bottom))
    else:
        # resize;
        new_img = img.resize((width, height), int(resample))

    byte_io = io.BytesIO()
    new_img.save(byte_io, format=format.strip("."), **kwargs)
    byte_io.seek(0)
    # params_size = ("width", "height", "force")
    # extra_args = {"size": size, "thumbnail_size": thumbnail_size}
    return byte_io
