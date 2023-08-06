import glob
from pathlib import Path

from PIL import Image


__version__ = '1.0.0'
__author__ = 'Mikhail Varantsou'


BG_COLOR = (255, 255, 255, 255)
SPACE_SHARE = 150


def _crop(img, ratio=1):
    """
    Apply ratio
    """
    imwidth, imheight = img.size

    if imwidth / imheight > ratio:
        width = ratio * imheight
        indent = (imwidth - width) / 2
        return img.crop((int(indent), 0, int(width + indent), imheight))
    else:
        height = imwidth / ratio
        indent = (imheight - height) / 2
        return img.crop((0, int(indent), imwidth, int(height + indent)))


def _prepare_imgs(images, length):
    if len(images) < length:
        raise ValueError(f'Provided {len(images)} images, have to be {length}')

    converted = [img.convert(mode='RGBA') for img in images]
    return converted


def _calc_space(width, spaceshare):
    if spaceshare:
        space = width // spaceshare
    else:
        space = 0
    return space


def _new_collage(width, height, bgcolor, img, space):
    clg = Image.new('RGBA', (width, height), bgcolor)
    clg.paste(img, (space, space))
    return clg


def collage_3_1(images, ratio=3/2, bgcolor=BG_COLOR, spaceshare=SPACE_SHARE):
    images = _prepare_imgs(images, 3)

    crimg0 = _crop(images[0], ratio)
    crimg1 = _crop(images[1], ratio)
    crimg2 = _crop(images[2], ratio)

    crimg0_w, crimg0_h = crimg0.size
    space = _calc_space(crimg0_w, spaceshare)
    btm_img_w = int((crimg0_w - space) / 2)
    btm_img_h = int(btm_img_w / ratio)

    crimg1 = crimg1.resize((btm_img_w, btm_img_h))
    crimg2 = crimg2.resize((btm_img_w, btm_img_h))

    total_w = crimg0_w + space * 2
    total_h = crimg0_h + btm_img_h + space * 3
    btm_img_h_place = crimg0_h + space * 2

    clg = _new_collage(total_w, total_h, bgcolor, crimg0, space)
    clg.paste(crimg1, (space, btm_img_h_place))
    clg.paste(crimg2, (btm_img_w + space * 2, btm_img_h_place))

    return clg


def collage_4_1(images, ratio=5/4, bgcolor=BG_COLOR, spaceshare=SPACE_SHARE):
    images = _prepare_imgs(images, 4)

    crimg0 = _crop(images[0], ratio)
    crimg1 = _crop(images[1], ratio)
    crimg2 = _crop(images[2], ratio)
    crimg3 = _crop(images[3], ratio)

    crimg0_w, crimg0_h = crimg0.size
    space = _calc_space(crimg0_w, spaceshare)
    btm_img_w = int((crimg0_w - space * 2) / 3)
    btm_img_h = int(btm_img_w / ratio)

    crimg1 = crimg1.resize((btm_img_w, btm_img_h))
    crimg2 = crimg2.resize((btm_img_w, btm_img_h))
    crimg3 = crimg3.resize((btm_img_w, btm_img_h))

    total_w = crimg0_w + space * 2
    total_h = crimg0_h + btm_img_h + space * 3
    btm_img_h_place = crimg0_h + space * 2

    clg = _new_collage(total_w, total_h, bgcolor, crimg0, space)
    clg.paste(crimg1, (space, btm_img_h_place))
    clg.paste(crimg2, (btm_img_w + space * 2, btm_img_h_place))
    clg.paste(crimg3, (btm_img_w * 2 + space * 3, btm_img_h_place))

    return clg


def collage_4_2(images, ratio=2, bgcolor=BG_COLOR, spaceshare=SPACE_SHARE):
    images = _prepare_imgs(images, 4)
    ratio_btm = ratio / 2

    crimg0 = _crop(images[0], ratio)
    crimg1 = _crop(images[1], ratio)
    crimg2 = _crop(images[2], ratio)
    crimg3 = _crop(images[3], ratio_btm)

    crimg0_w, crimg0_h = crimg0.size
    space = _calc_space(crimg0_w, spaceshare)

    btm_img_h = crimg0_h
    btm_img_w = int(btm_img_h * ratio_btm)

    btm_side_img_h = (btm_img_h - space) // 2
    btm_side_img_w = int(btm_side_img_h * ratio)

    crimg1 = crimg1.resize((btm_side_img_w, btm_side_img_h))
    crimg2 = crimg2.resize((btm_side_img_w, btm_side_img_h))
    crimg3 = crimg3.resize((btm_img_w, btm_img_h))

    total_w = crimg0_w + space * 2
    total_h = crimg0_h * 2 + space * 3
    btm_img_h_place = crimg0_h + space * 2

    clg = _new_collage(total_w, total_h, bgcolor, crimg0, space)
    clg.paste(crimg1, (space, btm_img_h_place))
    clg.paste(crimg2, (space, crimg0_h + btm_side_img_h + space * 3))
    clg.paste(crimg3, (btm_side_img_w + space * 2, btm_img_h_place))

    return clg


def collage_5_1(images, ratio=7/4, bgcolor=BG_COLOR, spaceshare=SPACE_SHARE):
    images = _prepare_imgs(images, 5)

    crimg0 = _crop(images[0], ratio)
    crimg1 = _crop(images[1], ratio)
    crimg2 = _crop(images[2], ratio)
    crimg3 = _crop(images[3], ratio)
    crimg4 = _crop(images[4], ratio)

    crimg0_w, crimg0_h = crimg0.size
    space = _calc_space(crimg0_w, spaceshare)
    btm_img_w = (crimg0_w - space) // 2
    btm_img_h = crimg0_h // 2

    crimg1 = crimg1.resize((btm_img_w, btm_img_h))
    crimg2 = crimg2.resize((btm_img_w, btm_img_h))
    crimg3 = crimg3.resize((btm_img_w, btm_img_h))
    crimg4 = crimg4.resize((btm_img_w, btm_img_h))

    total_w = crimg0_w + space * 2
    total_h = crimg0_h * 2 + space * 4

    clg = _new_collage(total_w, total_h, bgcolor, crimg0, space)
    clg.paste(crimg1, (space, crimg0_h + space * 2))
    clg.paste(crimg2, (btm_img_w + space * 2, crimg0_h + space * 2))
    clg.paste(crimg3, (space, crimg0_h + btm_img_h + space * 3))
    clg.paste(crimg4, (btm_img_w + space * 2, crimg0_h + btm_img_h + space * 3))

    return clg


def example():
    # Read image files into a list of PIL objects
    dirc = Path(__file__).resolve(strict=True).parent / 'example_images'
    imgs = []
    for imgpath in sorted(glob.glob(str(dirc / '*.jpg'))):
        imgs.append(Image.open(imgpath))

    # Send list of PIL images to a collage function
    collage = collage_5_1(imgs)

    # Show the returned PIL image containing the resulting collage
    collage.show()
