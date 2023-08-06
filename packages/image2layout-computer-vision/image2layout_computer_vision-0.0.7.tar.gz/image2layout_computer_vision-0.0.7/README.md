# image2layout_computer_vision

An image processing module for some computer vision tasks (public module for image2layout)

Package Page: [pypi](https://pypi.org/project/image2layout-computer-vision/)

Features:

1. Text Detection
2. Color extraction (background and main foreground)

## Installations

### Install with `python`/`conda` [Linux]

1. (Optional) Conda

```bash
curl https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh -o ~/conda.sh
bash ~/conda.sh -b -f -p /opt/conda
rm ~/conda.sh
conda init --all --dry-run --verbose

conda create -n cv python=3.10 -y
conda activate cv
```

2. Tesseract

```bash
sudo apt install tesseract-ocr libtesseract-dev -y
```


3. Python libraries (python>=3.8)

```bash
python -m pip install 'torch>=2.0' torchvision torchaudio

python -m pip install Pillow pandas numpy scikit-learn pyyaml==5.1 chardet pytesseract
python -m pip install --upgrade datasets transformers

python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

python -m pip install --upgrade image2layout-computer-vision
```

### Install with `docker`

Replace `Dockerfile_cpu` with `Dockerfile` if running with GPU
API Implementation is in-progress
```bash
sudo docker build --tag cv -f Dockerfile_cpu .

sudo docker run -it -v $(pwd):/app cv bash
```

## Usage

1. Run this python code to pre-download model weights

```python
from image2layout_computer_vision import model_dispatch_layout
model_dispatch_layout._load()
```

2. Detect texts

```python
import image2layout_computer_vision as icv

# ImageBoxes object
imageboxes = icv.detect_text('path/to/image.png')

# boxes_merged = merged boxes (sentences), boxes_raw = all boxes (words)
boxes_merged, boxes_raw = icv.detect_text_boxes('path/to/image.png')
```

3. Extract colors
```python
import image2layout_computer_vision as icv

color_bg, color_fg = icv.extract_colors('path/to/image.png')
```



## Build
(for building and uploading this package)
```bash
python -m pip install --upgrade pip
python -m pip install --upgrade build twine

rm -rf dist
python -m build
python -m twine upload dist/* --verbose
```
