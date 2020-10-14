# ROBin Infer

This code base contains only the inferencing part for ROBin. It was originally built on Raspberry Pi 4 (Raspbian Buster)

**Requires Python Version:** 3.7.+

**Requires Debian Packages:**

For numpy:
- libatlas-base-dev
- libatlas3-base

For Pillow:
- libjbig0
- libopenjp2-7
- libwebp6
- libtiff5
- liblcms2-2
- libwebpdemux2

## Installation
At the root of the project:
1. Create a virtual environment with `python3 -m venv .venv`
2. Activate the virtual environment with `source .venv/bin/activate`
3. Install dependencies with `pip install -r requirements.txt`
4. Install entry point script with `pip install -e .`

## To run ROBin
1. Activate the virtual environment with `source .venv/bin/activate`
2. At the root of the repo, run the command `robin`