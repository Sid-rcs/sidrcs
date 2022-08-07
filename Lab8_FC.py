import arcpy

arcpy.env.workspace = r'D:\Spring2022\Geog 378\AIRPORTS'

fc = 'airports.shp'
desc = arcpy.Describe(fc)

for field in desc.fields:
    fldName = field.name
    fldWidth = field.length

    fldPrecision = field.precision
    fldTypeS = field.type
    values = (fldName,fldTypeS,fldWidth,fldPrecision)
    fmt    = '%s: %s (%d.%d)'
    print(fmt % values)

cursor = arcpy.da.SearchCursor(fc, "Name")
for row in cursor:
    print(row[0])


cursor  = arcpy.da.SearchCursor(fc, ['name','quadname','lon','lat','SHAPE@XY'])
for feature in cursor:
   fmt = '%s of the %s Quad at lon, lat (%.6f,%.6f)'
   print(fmt % feature[:-1])

   shape = feature[-1]

   print('has coordinates (%.2f,%.2f)\n' % shape)