# %%
from image2layout_computer_vision import (
    get_image, COLOR, PixelMask, 
    ColorExtractor, extract_colors
)

# %%
fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/Screenshot 2023-07-26 at 14.22.06.png'
fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/Screenshot 2023-07-13 at 17.02.04.png'
# fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/SCR-20230710-khrl.jpeg'
fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/Bite.jpeg'
fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/Screenshot 2023-07-26 at 16.01.11.png'

CE = ColorExtractor(fp)
CE

CE.image
CE.draw_anno().convert('RGB')
