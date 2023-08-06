# %%
import time
import json
import os
import numpy as np
import pandas as pd
from PIL import Image
from typing import Union, Any, List, Dict, Tuple
from .model_layoutmlv2 import ModelDispatch_LayoutMLv2
from ..utils import get_image, ImageConvert
from .imagebox import ImageBoxes, BoxMerge

# %%
model_dispatch_layout = ModelDispatch_LayoutMLv2(
    device='cpu',
)

# %%
def detect_text(image: Union[Image.Image, np.ndarray], **kwargs) -> ImageBoxes:
    '''predict boxes for text in the image
    Parameters:
        image: (PIL.Image.Image, np.ndarray) RGB image
        **kwargs:
            line_dist_max:          max distance between boxes to be in the same sentence (as a ratio of line height)
            line_dist_min:          min (negative) distance between boxes to be in the same sentence (as a ratio of line height)
            line_iou_min:           min vertical iou between boxes to be on the same line
            row_hdist_max:          max horizontal offset between rows to aligned as a column (as a ratio of line height)
            row_vdist_max:          max vertical distance between rows to be in the same column (as a ratio of line height)
            row_height_ratio_min:   min ratio between heights of rows to be in the same column
    Returns:
        imageboxes: (ImageBoxes) object containing prediction boxes
    '''
    _image = get_image(image).convert('RGB')
    
    true_predictions, true_boxes = model_dispatch_layout(_image)
    true_boxes_np = np.array(true_boxes, int)
    true_boxes_check = np.all(true_boxes_np[:, 2:] > true_boxes_np[:, :2], axis=-1)
    true_boxes_np = true_boxes_np[true_boxes_check]
    
    imageboxes_raw = ImageBoxes(
        image=_image,
        boxes=true_boxes_np.tolist(),
    )
    imageboxes = imageboxes_raw.to_grouped_imageboxes(**kwargs)
    return imageboxes

def detect_text_boxes(image: Union[Image.Image, np.ndarray], **kwargs) -> Tuple[np.ndarray, np.ndarray]:
    '''predict boxes for text in the image
    Parameters: (same as detect_text)
    Returns:
        boxes_merged: (np.ndarray) [M, 4] text boxes detected, merged boxes
        boxes_raw:    (np.ndarray) [N, 4] text boxes detected, all individual boxes (N >= M)
    '''
    imageboxes = detect_text(image, **kwargs)
    boxes = np.array(list(imageboxes.df['box'])).astype(int)
    
    boxes_merged = np.array(imageboxes.boxes_top, int)
    boxes_raw = np.array(imageboxes.boxes, int)
    return boxes_merged, boxes_raw

# %%
if __name__ == '__main__':
    imageboxes = detect_text('data/inputs/SCR-20230710-ixfw.jpeg')
    imageboxes.draw_anno(width=3)
    imageboxes.df
    boxes = np.array(list(imageboxes.df['box'])).astype(int)
