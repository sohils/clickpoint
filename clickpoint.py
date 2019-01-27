"""
Author: Sohil Savla
Date: 01/26/2019

This snippet creates a CSV with the pixel coordinates of the point clicked on the image.
The CSV format is 
[image_name],[x],[y]
"""

import cv2
import glob
import matplotlib.pyplot as plt
import csv
import sys

def main():
	if(len(sys.argv[1:])!=3):
			print("Incorrect number of arguments.\nExample: python pointclick.py [images_folder_name] [image(s)_extension] [CSV_file_name]")
			return 0

	folder_name = sys.argv[1]
	extension = sys.argv[2]
	save_file = sys.argv[3]
	
	with open(save_file+'.csv', mode='w') as data_file:
		point_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		for filepath in glob.iglob(folder_name+'/*.'+extension):
			img = cv2.imread(filepath,-1)
			_, ax = plt.subplots(figsize=(9, 9))
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			imgplot = ax.imshow(img)
			x, y = plt.ginput(1, mouse_stop=2)[0]
			print(filepath, x,y)
			point_writer.writerow([filepath,x,y])

if __name__ == "__main__":
    main()