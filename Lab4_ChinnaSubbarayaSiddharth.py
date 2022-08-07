''' The program creates class city and uses methods for calculating distance
between cities, calculating the population change between two cities.
The program uses the data from the CityPop.csv'''

#importing sys and math modules
import sys
import math

#Open the file it exists in path or else it would exist
fileName = 'CityPop.csv'
try:
    f = open(fileName,'r')
except:
    print('The entered filename is not present:' + fileName)
    sys.exit()
   
#creating a class city and defining methods for distance between cities 
#and a method for calculating population changes over two years for a city    
class City:
    def __init__(self,name='',label='',latitude=-999,longitude=-999,population='N/A'):
        self.name = name #assigning each self element into a variable name
        self.label = label
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        
    def printDistance(self, othercity):
            try:
                self_lat = math.radians(self.latitude)
                self_lon = math.radians(self.longitude)
                other_lat = math.radians(othercity.latitude)
                other_lon = math.radians(othercity.longitude)
                spherical_dist = round(6300*(math.acos(math.sin(self_lat)*math.sin(other_lat) + 
                                           math.cos(self_lat)*math.cos(other_lat)*
                                           math.cos(self_lon-other_lon))))
                
                fmt = 'The distance between %s and %s is %d kms'
                val = (self.label, othercity.label, spherical_dist)
                print(fmt % val)
            except:
                print('Input cities are not available available in CityPop.csv')
        
    def printPopChange(self,year1,year2):
            pop_data = self.population
            if year1 in pop_data and year2 in pop_data:
                yr1 = pop_data[year1]
                yr2 = pop_data[year2]
                pop_difference = abs(yr1-yr2)
                print('The population change for %s city is %.2f million.'%(self.name, pop_difference))
            else:
                print("Sorry, the year(s) you have input does not exist in our file.")
        
        
#read the file in read mode as f and opens the file
with open(fileName,'r') as f:
    #reads the 1st line as header, strips \n and splits with comma as delimeter
    header = f.readline().strip().split(',')
    #reads the next line after the header informations
    f_main = f.readlines()
    city_data = []
    
#reading each line and stripping the \n and reading them into read_list
    for line in f_main:
        read_list = line.strip().split(',')
        name = read_list[header.index('city')] #index is used to find the position of element
        label = read_list[header.index('label')]
        latitude = float(read_list[header.index('latitude')])
        longitude = float(read_list[header.index('longitude')])
        
#instead of reading it as single variable this reads as a dictionary and elements are
#converted into a float
        pop_dict = {} #empty dict is created to load values from the for loop output
        
#years starts from the 5th index position and continues upto 14th index position
#Therefore, the loop is given a range of 5 to 14.
        for i in range(5,14):
            pop_dict[header[i]] = float(read_list[i]) #key-value pairs are assigned
#assigning all the values from the read_list and 
        city_inst = City(name = name, label = label, latitude = latitude, longitude = longitude, population = pop_dict)
        city_data.append(city_inst) #appending each instance into the city_data empty list
        
#printing the city_data with name, latitude, longitude and population           
for i in city_data:
    fmt = 'Name:%s, (Longitude,latitude):(%.2f,%.2f) \n %s \n'
    values = (i.name,i.longitude,i.latitude,i.population)
    print(fmt%values)

#checking the methods of city class for inputs    
City.printDistance(city_data[0],city_data[1])
City.printPopChange(city_data[0],'yr1970','yr1975')
    
        
        