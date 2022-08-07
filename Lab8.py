#Describing and accessing feature Classes

import arcpy
arcpy.env.workspace = r'D:\Spring2022\Geog 378\Worldcities'

fc = 'WorldCities.shp'
desc = arcpy.Describe(fc)

print('Path:', desc.path)
print('Extent:', desc.extent)
print('Feature Type:', desc.FeatureType)
print('Field Name:', desc.ShapeFieldName)
print('Shape Type:', desc.ShapeType)