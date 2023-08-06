# %%
import os, time, string, json
import numpy as np
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import plotly.express as px
import plotly.io as pio
pio.templates.default = 'plotly_dark'
from typing import Union, Any, List, Dict, Tuple

# %%
from image2layout_computer_vision import (
    ImageBoxes, detect_text, detect_text_boxes, BoxMerge, get_image
)


# %%
boxes_top, boxes_bottom = detect_text_boxes(
    '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/SCR-20230710-jhbw.png',
)
boxes_top, boxes_bottom


# %%
IB = detect_text(
    '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/SCR-20230710-jhbw.png',
    grouping=False,
)
IB

# %%
print(len(IB))
IB.draw_anno().convert('RGB')

# %%
IBG = IB.to_grouped_imageboxes()
IBG
IBG.draw_anno().convert('RGB')


# %%
def group_texts_by_match_fn(boxes: np.ndarray, fn, sort_index=None, **kwargs):
    # boxes should be sorted
    assert callable(fn)
    assert isinstance(boxes, np.ndarray)
    assert len(boxes.shape) == 2
    assert boxes.shape[-1] == 4
    
    count = len(boxes)
    assert count > 0
    
    if sort_index is None:
        sorted_indices = np.arange(count)
    else:
        assert sort_index in list(range(4))
        sorted_indices = np.argsort(boxes[:, sort_index])
    sorted_indices_reverse  = np.zeros(count, int)
    sorted_indices_reverse[sorted_indices] = np.arange(count)
    
    sorted_boxes = boxes[sorted_indices]
    count = len(sorted_boxes)
    
    matched_indices = set()
    remaining_indices = set(range(count))
    linked_groups = []
    
    for _ in range(count):
        if len(remaining_indices) <= 0:
            break
        
        start_index = min(remaining_indices)
        
        head_index = start_index
        linked_indices = [head_index]
        
        for next_index in range(head_index+1, count):
            if next_index in matched_indices:
                continue
            if fn(sorted_boxes[head_index], sorted_boxes[next_index], **kwargs):
                linked_indices.append(next_index)
                head_index = next_index
        
        linked_groups.append(linked_indices)
        matched_indices.update(linked_indices)
        remaining_indices.difference_update(linked_indices)
    
    data_group = []
    for i, indices in enumerate(linked_groups):
        original_indices = sorted_indices[indices]
        _merging_boxes = sorted_boxes[indices]
        group_box = BoxMerge.merge_boxes(sorted_boxes[indices])
        data_group.append({
            'indices': original_indices,
            'merging_boxes': _merging_boxes,
            'box': group_box,
        })
    
    df_group = pd.DataFrame(data_group)
    df_group
    return df_group

_boxes = np.array(_boxes_original)

df_group_temp = group_texts_by_match_fn(
    _boxes,
    fn=BoxMerge.same_line_match,
    sort_index=0,
    dist_max=line_dist_max,
    dist_min=line_dist_min,
    iou_min=line_iou_min,
)
df_group_temp

# %%
















# %%
line_dist_max:float=1.0
line_dist_min:float=-0.1
line_iou_min:float=0.4
row_hdist_max:float=0.4
row_vdist_max:float=1.8
row_height_ratio_min:float=0.8

_boxes_original = np.array(IB.boxes)
_boxes = np.array(_boxes_original)
assert _boxes.ndim == 2
assert _boxes.shape[-1] == 4

df_group_0 = BoxMerge.group_texts_by_match_fn(
    _boxes,
    fn=BoxMerge.same_line_match,
    sort_index=0,
    dist_max=line_dist_max,
    dist_min=line_dist_min,
    iou_min=line_iou_min,
)
_boxes = np.array(list(df_group_0['box']))
df_group_1 = BoxMerge.group_texts_by_match_fn(
    _boxes,
    fn=BoxMerge.same_column_match,
    sort_index=1,
    hdist_max=row_hdist_max,
    vdist_max=row_vdist_max,
    height_ratio_min=row_height_ratio_min,
)
_boxes = np.array(list(df_group_1['box']))
df_group_2 = BoxMerge.group_texts_by_match_fn(
    _boxes,
    fn=BoxMerge.box_containing_match,
)
_boxes = np.array(df_group_2['box'].to_list(), int)

# %%
def get_original_nested_indices(df_groups):
    indices_nested = [
        [
            v.tolist()
            for v in _df['indices']
        ]
        for _df in df_groups
    ]
    
    indices_original = None
    for i, _indices in enumerate(indices_nested):
        if i == 0:
            indices_original = [list(v) for v in _indices]
        else:
            indices_original = [
                [
                    v
                    for prev_index in prev_indices
                    for v in indices_original[prev_index]
                ]
                for prev_indices in _indices
            ]
    
    return indices_original

# %%
indices_original = get_original_nested_indices([
    df_group_0,
    df_group_1,
    df_group_2,
])
indices_original

# %%
boxes_nested_final = [
    [
        _boxes_original[i].tolist()
        for i in _indices
    ]
    for _indices in indices_original
]

# %%
imageboxes_nested = ImageBoxes(
    boxes=boxes_nested_final,
    image=IB.image,
)
imageboxes_nested

# %%
imageboxes_nested.boxes

# %%
imageboxes_nested.boxes_top

# %%
overlay_anno_bottom = draw_anno_box(
    img.size,
    boxes=imageboxes_nested.boxes,
    # texts=boxes_wh_str,
    font=font_fp,
    color='#00FF00',
    # color_text='#000000',
)

overlay_anno_top = draw_anno_box(
    img.size,
    boxes=imageboxes_nested.boxes_top,
    font=font_fp,
    color='#FF00FF',
)
overlay_anno = Image.alpha_composite(
    overlay_anno_bottom,
    overlay_anno_top,
)
Image.alpha_composite(
    img.convert('RGBA'),
    overlay_anno,
).convert('RGB')

# %%
[v.box_outer for v in imageboxes_nested]









# %%
font_fp = 'image2layout_computer_vision/utils/OpenSans_Condensed-Medium.ttf'
font_fp

# %%
img_fp = '/Users/felixdo/Documents/Code/AI/image2layout-computer-vision/data/inputs/SCR-20230710-jhbw.png'
img = get_image(img_fp).convert('RGB')
img

# %%
def draw_anno_box(
            img=(10, 10),
            font=None,
            boxes:Union[np.ndarray, list]=[],
            texts=None,
            width=None,
            text_pad=None,
            color='#00FF00',
            color_text='#000000',
            ):
    
    if isinstance(img, (tuple, list)):
        size = tuple(img)
    else:
        size = img.size
    
    img_anno = Image.new('RGBA', size)
    
    size_min = (min(size) + np.linalg.norm(size)) / 2
    if isinstance(font, str):
        font = ImageFont.truetype(font, int(size_min // 60))
    elif font is None:
        font = ImageFont.load_default()
    
    width = int(max(size_min // 600 if width is None else width, 1))
    
    text_pad = int(max(size_min // 200 if text_pad is None else text_pad, 1))
    
    # if mode in ['mask', 'all']:
    #     img_mask_inner = Image.new('L', self.size, 255)
    #     img_mask_full = Image.new('RGBA', self.size, (*self.mask_color, int(self.mask_opacity*255)))
        
    #     draw = ImageDraw.Draw(img_mask_inner)
    #     for box in self.boxes:
    #         draw.rectangle(
    #             tuple(box),
    #             fill=0,
    #             width=0,
    #         )
        
    #     img_anno.paste(img_mask_full, (0, 0), img_mask_inner)
    
    draw = ImageDraw.Draw(img_anno)
    drawing_texts = isinstance(texts, list) and len(texts) == len(boxes)
    for i, box in enumerate(boxes):
        _box = np.array(box)
        draw.rectangle(
            tuple(_box),
            outline=color,
            width=width,
        )
        
        if drawing_texts:
            _size = _box[2:] - _box[:2]
            _text = f'{_size[0]}•{_size[1]}'
            _text_box = np.array(font.getbbox(_text))
            _text_size = _text_box[2:] - _text_box[:2] + [text_pad * 2] * 2
            _text_box_padded = np.tile(_text_size, 2) * [-.5, -1, .5, 0]
            _text_offset = _text_box_padded[:2] + [text_pad, 0]
            _anchor = [(_box[0] + _box[2]) / 2, _box[1]]
            
            draw.rectangle(
                tuple(_text_box_padded + np.tile(_anchor, 2)),
                fill=color,
            )
            draw.text(
                tuple(_text_offset + _anchor),
                text=_text,
                fill=color_text,
                font=font,
            )
    
    if isinstance(img, Image.Image):
        # img_anno = Image.blend(
        #     img.convert('RGBA'),
        #     img_anno,
        #     0.75,
        # )
        img_anno = Image.alpha_composite(
            img.convert('RGBA'),
            img_anno,
            # 0.75,
        )
    return img_anno

# %%
boxes = np.stack(df_original['box'].to_list())
boxes

boxes_wh = boxes[:, 2:] - boxes[:, :2]
boxes_wh_str = [
    f'{v[0]}x{v[1]}'
    for v in boxes_wh
]

img_anno = draw_anno_box(
    img,
    # boxes=df_groups[0]['box'].to_list(),
    boxes=boxes,
    texts=boxes_wh_str,
    font=font_fp,
    # color='#00FF00',
    # color_text='#000000',
)
img_anno.convert('RGB')

# %%
