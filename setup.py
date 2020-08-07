import setuptools

INSTALL_REQUIREMENTS = ['numpy', 'torch', 'opencv-python', 'tqdm', 'imageio']

setuptools.setup(
    name='streamer_pytorch',
    url='https://github.com/Project-Splinter/streamer_pytorch',
    description='Pytorch based data streamer. (Capture, Video & Image).',    
    version='0.0.2',
    author='Ruilong Li',
    author_email='ruilongl@usc.edu',    
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIREMENTS,
)

