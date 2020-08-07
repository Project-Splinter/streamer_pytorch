# Pytorch Streamer

Pytorch based data streamer. (Capture, Video & Image).

## Install

```
pip install git+https://github.com/Project-Splinter/streamer_pytorch --upgrade
```

## Usage

```
# images
python demo.py --images <IMAGE_PATH> <IMAGE_PATH> <IMAGE_PATH> --loop --vis
# image folder
python demo.py --image_folder <IMAGE_FOLDER_PATH> --loop --vis
# videos
python demo.py --videos <VIDEO_PATH> <VIDEO_PATH> <VIDEO_PATH> --vis
# capture device
python demo.py --camera --vis
```

## API

- CaptureStreamer(id=0, width=512, height=512, pad=True)
- VideoListStreamer(files, width=512, height=512, pad=True)
- ImageListStreamer(files, width=512, height=512, pad=True)
- aug_matrix(w1, h1, w2, h2, pad=True)