from astropy.io import fits
import os
import pandas as pd

'''
THIS CODE WILL READ A FITS FILE AND THESE SPECIFIC KEYWORDS:
FILENAME
OBSTYPE
OBJECT
FILTERS

IT WILL TAKE THE VALUE OF THOSE KEYWORDS INTO A CSV FILE
'''

#empty array for specific keyword from fits file that will be appended here
fits_file = [] 
fits_obstype = []
fits_obj = []
fits_filter = []

path = input('Enter your path: ') 
#path of directory; must put input in string form
#/Users/admin/homeumd/fits_files/

for filename in os.listdir(path):
 #if os.listdir('.') -> accessing current directory
 
	newpath = os.path.join(path, filename) 
	#takes any number of pathname elements and joins them together according to the rules of the operating system
	
	if filename[-5:] == '.fits': 
		#only give the files which last 5 characters are '.fits'
		
		try:
			hdulist = fits.open(newpath)
			#open the fits file in this path
			
			file = hdulist[0].header['filename']
			fits_file.append(file)
			#looking into the first header and taking out the value for this specific keyword
			
			obstype = hdulist[0].header['obstype']
			fits_obstype.append(obstype)
			
			object_name = hdulist[0].header['object']
			fits_obj.append(object_name)
			
			filter_type = hdulist[0].header['filters']
			fits_filter.append(filter_type)

		except IOError:
			pass 
			#pass a file that has na IOError: file corrupt or does not have existing values
	

#Start making the dataset by zipping together the lists -> their respective indexes will be associated with each other


DataSet = list(zip(fits_file, fits_obstype, fits_obj, fits_filter))

dataframe = pd.DataFrame(data = DataSet, columns=['Filename', 'Object Type', 'Object', 'Filter(s)'])

dataframe.to_csv('Fits_200_346.csv', index=False, header=False) 



		


