'''Task3:  Program to print out the owners address ("SITUSADDR") and the area ("AREA") of 
    every parcel crossed by the power line'''

from osgeo import ogr, gdalconst
import sys

#reading file names of shape files
fileName_Parcel = 'Parcels.shp'
fileName_Power = 'PowerLine.shp'

#Loading the driver by name from ogr module
driver = ogr.GetDriverByName('ESRI Shapefile')

#Opening the Parcels.shp via driver
parcelDS = driver.Open(fileName_Parcel, gdalconst.GA_ReadOnly)
if parcelDS is None:
    print('unable to open the file')
    sys.exit(1)

#Loading Parcel layer properties
parcel_layer = parcelDS.GetLayer(0)
parcel_featureDefn = parcel_layer.GetLayerDefn()

#Opening the PowerLine.shp via driver
powerDS = driver.Open(fileName_Power, gdalconst.GA_ReadOnly)
if powerDS is None:
    print('unable to open the file')
    sys.exit(1)
    
#Loading Parcel layer properties    
power_layer = powerDS.GetLayer(0)
power_feature = power_layer.GetFeature(0)
powerGeom = power_feature.GetGeometryRef() #Getting geometry of PowerLine - LINESTRING

powerLineGeom = str(powerGeom)
print('Geometry of powerline as per ogr is> %s' %powerLineGeom[0:10])

parcelFeatureCount = parcel_layer.GetFeatureCount() #FeatureCount in Parcel Layer

print('\nAddress : Area (Square feet)')
print('----------------------------')

counter = 0
for i in range(parcelFeatureCount):
    parcel_feat = parcel_layer.GetFeature(i) #loads each feature via index number
    parcelGeom = parcel_feat.GetGeometryRef() #loads the geometry - POLYGON
    if parcelGeom.Crosses(powerGeom):
        address = parcel_feat.GetField('SITUSADDR')
        area = parcel_feat.GetField('AREA')
        values = (address, area)
        fmt = '%s: %.2f Sq ft'
        print(fmt % values)
        counter = counter +1 
    else:
        pass

print('\nParcel attributes that crosses with PowerLine are>', counter)

# parcelDS = powerDS = None #closing access to all dataSources