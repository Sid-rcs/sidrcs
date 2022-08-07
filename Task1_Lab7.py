'''Task 1: Calculation of Length of PowerLine in miles'''



from osgeo import ogr, gdalconst
import sys, math

#using relative path
fileName = 'Powerline.shp'

driver = ogr.GetDriverByName('ESRI Shapefile')

#opening the dataSource with help of driver
dataSource = driver.Open(fileName, gdalconst.GA_ReadOnly)

#checking whether the file opened or not
if dataSource is None:
    print('unable to open the file')
    sys.exit(1)


 #Reading only layer into layer variable   
layer = dataSource.GetLayer(0)

#yielding the Geometry type, Extent and Name of the layer
layerType = layer.GetGeomType()
layerExtent = layer.GetExtent()
LayerName = layer.GetName()

#Converting to text equivalents
layerTypeS = ogr.GeometryTypeToName(layerType)

print(LayerName, ' has an extent', layerExtent, 'is a', layerTypeS)

#Getting the feature count of the layer
featureCount = layer.GetFeatureCount()
print('\nNo of features', featureCount)


#Getting the layer definition which inturn reads the field (column count)
featureDefn = layer.GetLayerDefn()
fieldCount = featureDefn.GetFieldCount()

#From feature reading the geometry and calculating the length
feature  = layer.GetFeature(0)
LineGeometry = feature.GetGeometryRef()
length = LineGeometry.Length()
print('Length in US feet: %.2f' % length)

length = length*0.000189394
print('The length in miles of the powerline is %.2f'%length)


#distance based on the extent (manual checking of the answer)

#Getting the point count
nPts = LineGeometry.GetPointCount()
print('No of points available>',nPts)

total_length = 0 #initializing the total_length of powerLine

for i in range(nPts-1): #looping from 0 to 3
    
    pt1 = LineGeometry.GetPoint(i)
    pt2 = LineGeometry.GetPoint(i+1)
    
    x1 = pt1[0]
    x2 = pt2[0]
    
    y1 = pt1[1]
    y2 = pt2[1]
    
    total_length = total_length + math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))

total_length = total_length*0.000189394
print('Length of powerline: %.2f miles by GetPoint method'%total_length)

if total_length == length:
    print('Both Length() and GetPoint methods yielded same value')
else:
    print('Both length() and GetPoint methods yielded different value')

# dataSource = None