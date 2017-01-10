# gbdx.Task('tile-strips', images)

import os, subprocess

from shutil import move
from gbdx_task_interface import GbdxTaskInterface


class TileStrips(GbdxTaskInterface):

    def __init__(self):
        GbdxTaskInterface.__init__(self)

        # Get inputs
        self.image_dir = self.get_input_data_port('images')
        self.images = [img for img in os.listdir(self.image_dir) if img.endswith('.tif')]

        # Make output directory
        self.out_dir = self.get_output_data_port('tiled_images')
        os.makedirs(self.out_dir)


    def invoke(self):

        os.chdir(self.image_dir)

        # Tile each image and move to output
        for img in self.images:
            cmd = 'gdal_translate -co TILED=YES {} tiled_{} --config GDAL_TIFF_INTERNAL_MASK YES'.format(img, img)
            subprocess.call(cmd, shell=True)

            move('tiled_' + img, os.path.join(self.out_dir, img))


if __name__ == '__main__':
    with TileStrips() as task:
        task.invoke()
