# Pytorch Streamer

Pytorch based data streamer. (Capture, Video & Image).

## Install

```
pip install git+https://github.com/liruilong940607/streamer_pytorch --upgrade
```

## Usage

```
import tqdm
import argparse
import torch
import numpy as np
import cv2
import streamer_pytorch as streamer

parser = argparse.ArgumentParser(description='.')
parser.add_argument(
    '--camera', action="store_true")
parser.add_argument(
    '--images', default="", nargs="*")
parser.add_argument(
    '--videos', default="", nargs="*")
parser.add_argument(
    '--loop', action="store_true")
args = parser.parse_args()

def visulization(data):
    window = data[0].numpy()
    window = window.transpose(1, 2, 0)
    window = (window * 0.5 + 0.5) * 255.0
    window = np.uint8(window)
    window = cv2.cvtColor(window, cv2.COLOR_BGR2RGB) 
    window = cv2.resize(window, (0, 0), fx=2, fy=2)

    cv2.imshow('window', window)
    cv2.waitKey(1)

if args.camera:
    data_stream = streamer.CaptureStreamer()
elif len(args.videos) > 0:
    data_stream = streamer.VideoListStreamer(
        args.videos * (100 if args.loop else 1))
elif len(args.images) > 0:
    data_stream = streamer.ImageListStreamer(
        args.images * (100 if args.loop else 1))

loader = torch.utils.data.DataLoader(
    data_stream, 
    batch_size=1, 
    num_workers=1, 
    pin_memory=False,
)

try:
    for data in tqdm.tqdm(loader):
        visulization(data)
        pass
except Exception as e:
    print (e)
    del data_stream

```

## API

- CaptureStreamer(id=0, width=512, height=512, pad=True)
- VideoListStreamer(files, width=512, height=512, pad=True)
- ImageListStreamer(files, width=512, height=512, pad=True)
