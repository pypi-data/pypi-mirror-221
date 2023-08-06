# %%
import os, time, string, json
import numpy as np
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from typing import Union, Any, List, Dict, Tuple

# %%
def draw_anno_box(
            img=(10, 10),
            boxes:Union[np.ndarray, list]=[],
            texts=None,
            width=None,
            text_pad=None,
            color='#00FF00',
            color_text='#000000',
            font='utils/OpenSans_Condensed-Medium.ttf',
            ):
    
    if isinstance(img, (tuple, list)):
        size = tuple(img)
    else:
        size = img.size
    
    img_anno = Image.new('RGBA', size)
    
    size_min = (min(size) + np.linalg.norm(size)) / 2
    if isinstance(font, str) and os.path.isfile(font):
        font = ImageFont.truetype(font, int(size_min // 60))
    else:
        font = ImageFont.load_default()
    
    width = int(max(size_min // 600 if width is None else width, 1))
    text_pad = int(max(size_min // 200 if text_pad is None else text_pad, 1))
    
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
        img_anno = Image.alpha_composite(
            img.convert('RGBA'),
            img_anno,
        )
    return img_anno
