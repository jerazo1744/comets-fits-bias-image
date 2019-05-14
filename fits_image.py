import os
import sys
import argparse
import numpy as np
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt

	
path = input('Enter your path: ')
#path of directory; must put input in string form
#/Users/admin/...
	
def lingray(x, a=None, b=None):
	if a == None:
		a = np.min(x)
	if b == None:
		b = np.max(x)
	return 255.0 * (x-float(a))/(b-a)
	
def loggray(x, a=None, b=None):
	if a == None:
		a = np.min(x)
	if b == None:
		b = np.max(x)
	linval = 10.0 + 990.0 * (x-float(a))/(b-a)
	return (np.log10(linval)-1.0)*0.5 * 255.0	
	
	
#Open the fits file and create an hdulist
for filename in os.listdir(path):
	newpath = os.path.join(path, filename)
	hdulist1 = fits.open(newpath, 'lmi.0001.fits')
	hdulist2 = fits.open(newpath,'lmi.0002.fits')
	hdulist4 = fits.open('lmi.0004')
	hdulist5 = fits.open('lmi.0005')
	hdulist6 = fits.open('lmi.0006')
	hdulist7 = fits.open('lmi.0007')
	hdulist8 = fits.open('lmi.0008')
	hdulist9 = fits.open('lmi.0009')
	hdulist10 = fits.open('lmi.0010')
	hdulist11 = fits.open('lmi.0011')
	hdulist12 = fits.open('lmi.0012')
	hdulist13 = fits.open('lmi.0013')
	hdulist14 = fits.open('lmi.0014')
	hdulist15 = fits.open('lmi.0015')
	hdulist16 = fits.open('lmi.0016')
	hdulist17 = fits.open('lmi.0017')
	hdulist18 = fits.open('lmi.0018')
	hdulist19 = fits.open('lmi.0019')
	hdulist20 = fits.open('lmi.0020')
	hdulist323 = fits.open('lmi.0323')
	hdulist324 = fits.open('lmi.0324')
	hdulist325 = fits.open('lmi.0325')
	hdulist326 = fits.open('lmi.0326')
	hdulist327 = fits.open('lmi.0327')
	hdulist328 = fits.open('lmi.0328')
	hdulist329 = fits.open('lmi.0329')
	hdulist330 = fits.open('lmi.0330')
	hdulist331 = fits.open('lmi.0331')
	hdulist332 = fits.open('lmi.0332')
	image_data1 =  hdulist1[0].data
	image_data2 =  hdulist2[0].data
	image_data3 =  hdulist3[0].data
	image_data4 =  hdulist4[0].data
	image_data5 =  hdulist5[0].data
	image_data6 =  hdulist6[0].data
	image_data7 =  hdulist7[0].data
	image_data8 =  hdulist8[0].data
	image_data9 =  hdulist9[0].data
	image_data10 =  hdulist10[0].data
	image_data11 =  hdulist11[0].data
	image_data12 =  hdulist12[0].data
	image_data13 =  hdulist13[0].data
	image_data14 =  hdulist14[0].data
	image_data15 =  hdulist15[0].data
	image_data16 =  hdulist16[0].data
	image_data17 =  hdulist17[0].data
	image_data18 =  hdulist18[0].data
	image_data19 =  hdulist19[0].data
	image_data20 =  hdulist20[0].data
	beg_stack = np.array([image_data1, image_data2, image_data3, image_data4, image_data5, image_data6, image_data7, image_data8, image_data9, image_data10, image_data11, image_data12, image_data13, image_data14, image_data15, image_data16, image_data17, image_data18, image_data19, image_data20])
	beg_median = np.median(beg_stack, axis=0)
	image_data323 =  hdulist323[0].data
	image_data324 =  hdulist324[0].data
	image_data325 =  hdulist325[0].data
	image_data326 =  hdulist326[0].data
	image_data327 =  hdulist327[0].data
	image_data328 =  hdulist328[0].data
	image_data329 =  hdulist329[0].data
	image_data330 =  hdulist330[0].data
	image_data331 =  hdulist331[0].data
	image_data332 =  hdulist332[0].data
	end_stack = np.array([image_data323, image_data324, image_data325, image_data326, image_data327, image_data328, image_data329, image_data330, image_data331, image_data332])
	end_median = np.median(end_stack, axis=0)
	whole_stack = np.array([beg_median, end_median])
	whole_median = np.median(whole_stack, axis=0)
	

#Assign the input header in case it is needed later
hdr = hdulist[0].header

#Assign image data to a numpy array
image_data = hdulist[0].data

#Print information about the image
print('Side: ', image_data.size)
print('Shape: ', image_data.shape)

#Show the image
new_image_data = lingray(image_data)
new_image_min = 0.
new_image_max = np.max(new_image_data)
plt.imshow(new_image_data, vmin = new_image_min, vmax = new_image_max, cmap = 'gray')
plt.show()

#close the input image file and exit
hdulist.close()
exit()