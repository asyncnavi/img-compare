from imgcompare import *
from PIL import *

def compare_img(image_a,image_b):
	percentage = image_diff_percent(image_a, image_b)
	
	return (100 - percentage)
