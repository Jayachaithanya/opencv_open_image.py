#  used to remove the background of the image by uploading the files

from rembg import remove
import easygui as eg
from PIL import Image

input_path = eg.fileopenbox(title='Select image file')
output_path = 'output_image.png'

input_image = Image.open(input_path)

output_image = remove(input_image)
output_image.save(output_path)

print("Successfully removed `background`.")

image = Image.open(output_path)
image.show()
