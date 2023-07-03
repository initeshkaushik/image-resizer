# Image Resizer

This repository contains a simple image resizer application built using Python. It allows you to resize images to a specified width and height.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

To use the image resizer, follow these steps:

1. Clone this repository to your local machine:

git clone https://github.com/initeshkaushik/image-resizer.git


2. Navigate to the project directory:

cd image-resizer


## Usage

To resize an image, run the following command:

``` python resize_image.py <input_image_path> <output_image_path> --width <desired_width> --height <desired_height> ```


Replace `<input_image_path>` with the path to the input image file, `<output_image_path>` with the desired path for the resized image file, `<desired_width>` with the desired width in pixels, and `<desired_height>` with the desired height in pixels.

For example, to resize an image named `example.jpg` to a width of 800 pixels and a height of 600 pixels, you can use the following command:

``` python resize_image.py example.jpg resized_example.jpg --width 800 --height 600 ```


The resized image will be saved at the specified output path.
