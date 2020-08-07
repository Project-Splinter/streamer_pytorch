import tqdm
import argparse
import torch
import numpy as np
import cv2
import glob
import streamer_pytorch as streamer


parser = argparse.ArgumentParser(description='.')
parser.add_argument(
    '--camera', action="store_true", help="whether to use webcam.")
parser.add_argument(
    '--images', default="", nargs="*", help="paths of image.")
parser.add_argument(
    '--image_folder', default=None, help="path of image folder.")
parser.add_argument(
    '--videos', default="", nargs="*", help="paths of video.")
parser.add_argument(
    '--loop', action="store_true", help="whether to repeat images/video.")
parser.add_argument(
    '--vis', action="store_true", help="whether to visualize.")
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
    data_stream = streamer.CaptureStreamer(pad=False)
elif len(args.videos) > 0:
    data_stream = streamer.VideoListStreamer(
        args.videos * (10 if args.loop else 1))
elif len(args.images) > 0:
    data_stream = streamer.ImageListStreamer(
        args.images * (10000 if args.loop else 1))
elif args.image_folder is not None:
    images = sorted(glob.glob(args.image_folder+'/*.jpg'))
    images += sorted(glob.glob(args.image_folder+'/*.png'))
    data_stream = streamer.ImageListStreamer(
        images * (10 if args.loop else 1))


loader = torch.utils.data.DataLoader(
    data_stream, 
    batch_size=1, 
    num_workers=1, 
    pin_memory=False,
)


try:
    for data in tqdm.tqdm(loader):
        if args.vis:
            visulization(data)
except Exception as e:
    print (e)
    del data_stream
