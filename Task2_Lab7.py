'''Task 2: Print out the attribute names and attribute data types of the layer'''

from osgeo import ogr, gdalconst
import os, sys

#using relative paths
fileName = 'Parcels.shp'

driver = ogr.GetDriverByName('ESRI Shapefile')

#Opening and verfying the dataSource via driver by ogr
dataSource = driver.Open(fileName, gdalconst.GA_ReadOnly)
if dataSource is None:
    print('unable to open the file')
    sys.exit(1)

#Loading all the layer deatails into variable    
layer = dataSource.GetLayer(0)
layerType = layer.GetGeomType()
layerExtent = layer.GetExtent()
LayerName = layer.GetName()

#converting into text equivalents
layerTypeS = ogr.GeometryTypeToName(layerType)

print(LayerName, 'has an extent', layerExtent, 'is a', layerTypeS)

#obtaining feature count
featureCount = layer.GetFeatureCount()
print('\nNo of features:', featureCount)

#Getting field count from layer definition using ogr
featureDefn = layer.GetLayerDefn()
fieldCount = featureDefn.GetFieldCount()


print("The layer's feature definition has the following",fieldCount,"fields:")
print('\nField Name: Data type')
print('-----------------------')
for i in range(fieldCount):
    fieldDef      = featureDefn.GetFieldDefn(i) #Getting each field definitions

    fieldName       = fieldDef.GetNameRef() #retrieving name
    fieldType       = fieldDef.GetType() #retrieving DataType

    fieldTypeS = fieldDef.GetFieldTypeName(fieldType)
    
    values = (fieldName,fieldTypeS)
    fmt    = '%s: %s'
    print(fmt % values)
    

# dataSource = None