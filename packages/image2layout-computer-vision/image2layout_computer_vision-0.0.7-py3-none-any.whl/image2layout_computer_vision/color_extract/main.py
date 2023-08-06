# %%
import time
import numpy as np
import pandas as pd
from typing import Any, Union, Dict, List, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from sklearn.cluster import KMeans

from ..utils import get_image, COLOR, PixelMask

# %%
class ColorKMeans:
    def __init__(self,
                colors:Union[np.ndarray, Image.Image],
                n_clusters:int=2,
                edge_amounts:list=[0.05, 0.1, 0.15],
                middle_amounts:list=[0.2, 0.4],
                ):
        assert n_clusters >= 2
        self.n_clusters = n_clusters
        
        self.colors = COLOR.get_colors(np.array(colors), 3)
        self.colors_yiq = COLOR.rgb2yiq(self.colors)
        self.colors_yiq_flat = self.colors_yiq.reshape(-1, 3)
        
        self.shape = self.colors.shape[:-1]
        uniques, counts = COLOR.count_unique_colors(self.colors_yiq_flat)
        n_uniques = uniques.shape[0]
        assert n_uniques > 0, f'`data` is either empty or invalid'
        # if n_uniques == 1:
        #     return np.zeros(shape, int), uniques[0]
        assert n_clusters <= n_uniques
    
        self.model = KMeans(
            n_clusters=n_clusters,
            n_init='auto',
            init=uniques[:n_clusters],
        )
        cluster_indices = self.model.fit_predict(self.colors_yiq_flat)
        self.cluster_map = cluster_indices.reshape(self.shape)
        
        self.cluster_onehot = self.cluster_map[:, :, None] == np.arange(self.n_clusters)
        
        self.cluster_centers_yiq = self.model.cluster_centers_
        self.cluster_centers = COLOR.yiq2rgb(self.cluster_centers_yiq)
        
        self.center_dists = np.linalg.norm(
            self.cluster_centers_yiq[None] - self.cluster_centers_yiq[:, None],
            axis=-1,
        )
        self.center_dist_max = self.center_dists.max()
        self.center_dists_nonzero = self.center_dists[
            np.logical_not(PixelMask.diagonal_mask(self.n_clusters))
        ].reshape(self.n_clusters, self.n_clusters-1)
        
        self.cluster_errors = np.array([
            np.linalg.norm(
                self.colors_yiq[self.cluster_map == cluster_index] - self.cluster_centers_yiq[cluster_index][None],
                axis=-1
            ).mean()
            for cluster_index in range(self.n_clusters)
        ])
        self.cluster_errors_ratio = self.cluster_errors / self.center_dist_max
        
        self.edge_scores = self.compute_scores_from_dist(amount=edge_amounts, from_edge=True)
        self.middle_scores = self.compute_scores_from_dist(amount=middle_amounts, from_edge=False)
        self.areas = self.cluster_onehot.mean(0).mean(0)
    
    def __repr__(self) -> str:
        info = ' | '.join([
            f'{k}{v.round(3)}'
            for k, v in {
                'areas': self.areas,
                'errors_r': self.cluster_errors_ratio,
                'edge_scores': self.edge_scores,
                'middle_scores': self.middle_scores,
            }.items()
        ])
        return f'ColorKMeans[{self.n_clusters}]({info})'
    
    def compute_scores_from_dist(self, amount:float=0.1, from_edge:bool=True) -> np.ndarray:
        if isinstance(amount, (list, tuple, np.ndarray)):
            assert len(amount) >= 1
            edge_ratios = np.array([
                self.compute_scores_from_dist(amount=_amount, from_edge=from_edge)
                for _, _amount in enumerate(amount)
            ])
            edge_scores = edge_ratios.mean(0)
            return edge_scores
        
        _mask = PixelMask.edge_mask(shape=self.shape, amount=float(amount))
        if not from_edge:
            _mask = np.logical_not(_mask)
        _indices, _counts = COLOR.count_uniques(self.cluster_map[_mask])
        _scores = np.zeros(self.n_clusters, float)
        _scores[_indices] = _counts / _counts.sum()
        return _scores

# %%
class ColorExtractor:
    def __init__(self,
                image:Image.Image, 
                n_clusters_max=5,
                n_clusters_min=2,
                with_foreground=True,
                **kwargs,
                ):
        '''
        Parameters:
            n_clusters_min / n_clusters_max (int): range of values for KMeans n_clusters
            with_foreground (bool): whether to extract foreground color
            kwargs:
                bg_error_ratio_max [0.05]
                unique_ratio_min [0.5]
        '''
        self.image = get_image(image).convert('RGB')
        self.size = self.image.size
        self.shape = np.array(self.image.size[::-1])
        
        self.extracted_data = self.extract_colors_from_scores_and_dist(
            image=self.image,
            n_clusters_max=n_clusters_max,
            n_clusters_min=n_clusters_min,
            with_foreground=with_foreground,
            force_run_all=False,
            **kwargs,
        )
        self.extract_map = self.extracted_data['extract_map']
        self.color_bg = tuple(self.extracted_data['color_bg'])
        self.color_fg = tuple(self.extracted_data['color_fg'])
        self.colors = [self.color_bg, self.color_fg]
    
    def __repr__(self) -> str:
        return f'ColorExtractor[{self.shape}]({self.color_bg} | {self.color_fg})'
    
    def draw_anno(self,):
        img_anno_np = np.zeros([*self.shape, 4], np.uint8)
        img_anno_np[self.extract_map == 0] = [*self.color_bg, 255]
        img_anno_np[self.extract_map == 1] = [*self.color_fg, 255]
        img_anno = Image.fromarray(img_anno_np, 'RGBA')
        return img_anno

    @classmethod
    def get_primary_color(cls, colors:np.ndarray, unique_ratio_min=0.5):
        '''
        Parameters:
            colors: (np.ndarray) [..., 3] RGB colors
        '''
        _colors = COLOR.get_colors(colors, 3).reshape(-1, 3)
        uniques, counts = COLOR.count_unique_colors(_colors)
        ratios = counts / counts.sum()
        if ratios[0] >= unique_ratio_min:
            return uniques[0]
        colors_yiq = COLOR.rgb2yiq(_colors)
        avg_color_yiq = colors_yiq.mean(0)
        avg_color = COLOR.yiq2rgb(avg_color_yiq)
        return avg_color
    
    @classmethod
    def extract_colors_from_scores_and_dist(cls,
                image,
                n_clusters_max=5,
                n_clusters_min=2,
                bg_error_ratio_max=0.05,
                with_foreground=True,
                unique_ratio_min=0.5,
                force_run_all=False,
                **kwargs
                ):
        assert n_clusters_max >= n_clusters_min, f'n_clusters_max[{n_clusters_max}] >= n_clusters_min[{n_clusters_min}]'
        data = []
        _img = get_image(image).convert('RGB')
        for n_clusters in range(n_clusters_min, n_clusters_max+1):
            ckm = ColorKMeans(_img, n_clusters=n_clusters, **kwargs)
            extract_map = np.zeros(ckm.shape, int) - 1
            
            bg_scores = ckm.edge_scores + ckm.areas / 4
            bg_order = np.argsort(bg_scores)[::-1]
            bg_index = bg_order[0]
            bg_mask = ckm.cluster_map == bg_index
            bg_color = cls.get_primary_color(ckm.colors[bg_mask], unique_ratio_min=unique_ratio_min)
            extract_map[bg_mask] = 0
            
            bg_error = ckm.cluster_errors_ratio[bg_index]
            bg_passed = bg_error <= bg_error_ratio_max
            
            fg_color = np.zeros(3, np.uint8)
            if with_foreground:
                fg_scores = ckm.middle_scores + ckm.areas / 10
                fg_order = np.argsort(fg_scores)[::-1]
                fg_index = [v for v in fg_order if v != bg_index][0]
                fg_mask = ckm.cluster_map == fg_index
                extract_map[fg_mask] = 1
                fg_color = cls.get_primary_color(ckm.colors[fg_mask], unique_ratio_min=unique_ratio_min)
            
            d = {
                'n_clusters': n_clusters,
                'bg_passed': bg_passed,
                'bg_error': bg_error,
                'color_bg': bg_color,
                'color_fg': fg_color,
                # 'ckm': ckm,
                'extract_map': extract_map, 
            }
            data.append(d)
            del ckm
            
            if not force_run_all and bg_passed:
                return d
            
        else:
            if not force_run_all:
                return d
        return data


# %%
def extract_colors(image):
    img = get_image(image)
    color_extractor = ColorExtractor(img)
    return color_extractor.colors

# %%
if __name__ == '__main__':
    image = Image.open('path/to/the/image.png').convert('RGB')
    color_extractor = ColorExtractor(image)
    color_extractor.colors
    color_extractor.color_bg
    color_extractor.color_fg
