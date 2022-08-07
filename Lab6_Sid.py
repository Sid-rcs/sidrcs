''' This program calculates Normalized Difference Vegetation Index values 
    from Landsat images of Red band and Near IR
    giving an NDVI.tif as an output'''

#importing all the required modules
import os
import sys
from osgeo import gdal, gdalconst
import numpy as np

#Setting the path to current or working directory
os.chdir(r'D:\Spring2022\Geog 378\labscripts\g378_lab6\landsat\landsat')

#Setting the file names
file1 = r'L71026029_02920000609_B30_CLIP.TIF'
file2 = r'L71026029_02920000609_B980_CLIP.TIF'

#Checking whether the files are present in the path
if os.path.exists(file1) == True and os.path.exists(file2) == True:
    print('Required files are available in path>', file1, '\n', file2)
else:
    sys.exit('set to the current working directory by os.chdir(path)')


#Opening each file using relative paths in read only modes
red = gdal.Open(file1,gdalconst.GA_ReadOnly)
if red is None: #if the file is None
    print('Could not open file>',file1)
    sys.exit()
NIR = gdal.Open(file2,gdalconst.GA_ReadOnly)
if NIR is None:
    print('Could not open file>',file2)
    sys.exit()

#Reading gdalobjects as array and type casting as float values
red_ary = red.ReadAsArray().astype(float)
NIR_ary = NIR.ReadAsArray().astype(float)


#Printing info to have idea about pixels available per image
print('\n --------Information about the input files----------')
print('\n',file1,'has band count of', red.RasterCount, 'with cols * row>',
      red.RasterXSize, red.RasterYSize)
print('\n',file2,'has band count of', NIR.RasterCount, 'with cols * row>',
      NIR.RasterXSize, NIR.RasterYSize)



cols = red.RasterXSize #loads columnar pixel count
rows = red.RasterYSize #loads row wise pixel count


#Checks for Zero presence in both arrays as 0/0 is undefined
#Logical_and requires both conditions to be true
zero_check = np.logical_and(red_ary>0,NIR_ary>0) 

#numpy where has a condition, calculation method, if true (1) - boolean
NDVI = np.where(zero_check, (NIR_ary - red_ary) /(NIR_ary + red_ary),1)


output_file = 'NDVI.TIF'
if os.path.exists(output_file):
    os.remove(output_file) #removes the file if already present
    
#As each image has a driver which is accessed bu GDAL in opening the file    
output_driver = gdal.GetDriverByName('GTiff')
dtype = gdalconst.GDT_Byte #value type utilized GDT_float32 also used

#create a raster output from the variable values
NDVI_file = output_driver.Create(output_file,cols,rows,1,dtype)

#setting the GeoTransform from the file1/red image
#creating relation between pixel value and project data
NDVI_file.SetGeoTransform(red.GetGeoTransform())

#setting the projection data from the existing file1/red
NDVI_file.SetProjection(red.GetProjection())

#setting raster band to gray scale, hence 1
band = NDVI_file.GetRasterBand(1)
band.SetColorInterpretation(gdalconst.GCI_Undefined)

#writing the calculated array into the NDVI.tif
band.WriteArray(NDVI)
band.FlushCache()

#closing all the opened files
NDVI_file = red = NIR = None

print('\n %s has been created in the current directory' %output_file)




