'''Task4: To export all the selected parcel within 250 ft from the
    powerline.shp (Buffer) and export them as new shape file'''

from osgeo import ogr, gdalconst
import os, sys

#Reading all the files
file1 = 'PowerLine.shp'
file2 = 'Parcels.shp'
outputFile = 'parcelBuffer.shp'

bufferWidth = 250 #ft #The map units are in state plane

#Step1: Load the driver that reads the input files
driver = ogr.GetDriverByName('ESRI Shapefile')

#Step2: Read all the files and test them for NoneType
powerDS = driver.Open(file1, gdalconst.GA_ReadOnly)
if powerDS is None:
    sys.exit('unable to open the file', powerDS)
parcelDS = driver.Open(file2, gdalconst.GA_ReadOnly)
if parcelDS is None:
    sys.exit('unable to open the file', parcelDS)
    
#Step3.1: Load all the layer properties of the PowerLine layer
powerLayer = powerDS.GetLayer(0)
powerFeature = powerLayer.GetNextFeature()
powerGeom = powerFeature.GetGeometryRef()

#Step3.2: Load all the layer properties of the Parcel layer
parcelLayer = parcelDS.GetLayer(0)
parcelFeatureCount = parcelLayer.GetFeatureCount()

#Step4: Checking if already present before creating outputfile
if os.path.exists(outputFile):
  try:
    os.remove(outputFile)
  except: #This handles the permission error
      print('File already in use, cannot run the program again')
 
#Loads the buffer of PowerLine into the variable as ogr object      
powerLineBuffer = powerGeom.Buffer(bufferWidth)
print('250 ft Buffer created along the BufferLine.shp')

#Step5: Creates output data source using ESRI Shapefile driver
try: 
    outputDS = driver.CreateDataSource(outputFile)   
except:
    print('Unable to create the outputfile>', outputFile)

#Step6: Setting spatial reference and creating layer with geometric type 
# WKB - well known binary polygon
SRS = parcelLayer.GetSpatialRef()    
newLayer = outputDS.CreateLayer('parcelBuffer',SRS,ogr.wkbPolygon)
if newLayer is None:
    print('parcelBuffer.shp is not a directory')
newLayerDefn = newLayer.GetLayerDefn() #loading layer definition

#looping the features into New Shapefile
print('Parcels within 250 ft are identified and shapefile is created')
counter = 0
featureID = 0
parcelFeature = parcelLayer.GetNextFeature()
while parcelFeature:
    parcelGeom = parcelFeature.GetGeometryRef()
    parcelBuffers = parcelGeom.Within(powerLineBuffer)
    
    if parcelBuffers:
        try:
            print(parcelFeature.GetField('SITUSADDR'), ": ", parcelFeature.GetField('AREA'))
            newFeature = ogr.Feature(newLayerDefn)
            newFeature.SetGeometry(parcelGeom)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
            counter = counter + 1
        except:
            print('Error printing ParcelBuffer.shp')
    else:
        pass
    parcelFeature = parcelLayer.GetNextFeature()  
    featureID += 1
print('No of Parcel features within the zone of Powerline 250 ft Buffer>', counter)
# powerDS = parcelDS = outputDS = None