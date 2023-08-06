import glob
from pathlib import Path

from PIL import Image

import social_collage


# Read image files into a list of PIL objects
dirc = Path(__file__).resolve(strict=True).parent / 'example_images'
imgs = []
for imgpath in sorted(glob.glob(str(dirc / '*.jpg'))):
    imgs.append(Image.open(imgpath))

# Send list of PIL images to a collage function
collage = social_collage.collage_5_1(imgs)

# Show the returned PIL image containing the resulting collage
collage.show()
