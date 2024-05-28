#  used to remove the background of the image by uploading the files
# import statement
from rembg import remove
import easygui as eg
from PIL import Image

input_path = eg.fileopenbox(title='Select image file')
output_path = 'output_image.png'
#  adding location and file open box for fetching the image.

input_image = Image.open(input_path)
#  open(read) the image

output_image = remove(input_image)
output_image.save(output_path)
#  removing the background and saving it.

print("Successfully removed `background`.")

image = Image.open(output_path)
image.show()
