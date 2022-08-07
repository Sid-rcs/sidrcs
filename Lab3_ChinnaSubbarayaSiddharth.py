import os 
import math 
if os.path.exists(r'CityPop.csv') == False:
    print('The file does not exists in the path / Wrong file name')
else:
   print('CityPop.csv exists !!')
   city_dict = {}; header = []
   f = open('CityPop.csv','r')
   header = f.readline()
   header = header.strip().split(',')
   f_main = f.readlines()

   for i in f_main:
       read_list = i.strip().split(',')
       read_list[1] = float(read_list[1]); read_list[2] = float(read_list[2])
       for k in range(5,14):
           read_list[k]=float(read_list[k])
       city = read_list[3]
       city = city.title(); city = city.replace(' ', '_')
       base_dict = dict(zip(header,read_list))
       city_dict[city] = base_dict
   f.close()


while True:
    try:
        print('\nKindly input with a single space between words\n')
        city_name = input('Enter city name(hit enter to exit)> ')
        if len(city_name)<1: break
        city_name = city_name.title(); city_name = city_name.replace(' ', '_')
        if city_name[0:3] == 'St.':
                city_name = city_name.replace('St.', 'Saint')
                city_name = city_name.replace(' ','_')
        else:
                city_name = city_name.replace('St', 'Saint')
                city_name = city_name.replace(' ','_')
        if city_name not in city_dict: 
            print('Warning: Entered city name not available')
            continue
        year = str(input('Enter year(hit enter to exit)> '))
        if len(year)<1: break
        if ('yr'+year) not in city_dict[city_name]: 
            print('Warning: Entered year not available')
            continue
        if city_name in city_dict: 
            if ('yr'+year) in city_dict[city_name]:   
                print('The population of',city_name,'in',year, 'is', city_dict[city_name]['yr'+year],'million') 
    except:
        print('consider re-entering warnings carefully and restart again')
        

while True:
    try:
        print('\n Hit enter at any input to exit or Enter inputs with single space\n')
        city1 = input('Enter a source city>')
        if len(city1)<1: break
        city1= city1.title(); city1 = city1.replace(' ', '_')
        if city1[0:3] == 'St.':
                city1 = city1.replace('St.', 'Saint')
                city1 = city1.replace(' ','_')
        else:
                city1 = city1.replace('St', 'Saint')
                city1 = city1.replace(' ','_')
                
        if city1 not in city_dict: 
            print('Warning: Entered city name not available')
            continue
        

        city2 = input('Enter a target city>')
        if len(city1)<1: break
    
        city2 = city2.title(); city2 = city2.replace(' ', '_')
        if city2[0:3] == 'St.':
                city2 = city2.replace('St.', 'Saint')
                city2 = city2.replace(' ','_')
        else:
                city2 = city2.replace('St', 'Saint')
                city2 = city2.replace(' ','_')
                
        if city2 not in city_dict: 
            print('Warning: Entered city name not available')
            continue

        if (city1 in city_dict) and (city2 in city_dict):
            lat1 = city_dict[city1]['latitude']; lon1 = city_dict[city1]['longitude']
            lat2 = city_dict[city2]['latitude']; lon2 = city_dict[city2]['longitude']
            phi1 = math.radians(lat1) #math.radians convert degrees to radians
            phi2 = math.radians(lat2)
            lam1 = math.radians(lon1)
            lam2 = math.radians(lon2)
            dl = abs(lam1-lam2) 
            d = math.acos((math.sin(phi1)*math.sin(phi2))+(math.cos(phi1)*math.cos(phi2)*math.cos(dl))) 
            spheric_dist = round(d*6300) 
            print('\n Spherical distance between %s and %s is %.f Kms'%(city1,city2,spheric_dist))       
    except:
        print('look out for warning and please restart !')
    

while True:
    try:
        year1 = ('yr'+ input('Enter start year(Hit Enter to exit)>'))
        if len(year1)<3:break
        if year1 not in header: 
            print('Start year is not available')
            print('Available list of years>',list(range(1970,2015,5)))
            continue
        
        year2 = ('yr'+ input('Enter end year(Hit enter to exit)>'))
        if len(year2)<3:break
        if year2 not in header: 
            print('End year is not available')
            print('Available list of years>',list(range(1970,2015,5)))
            continue
        
        if year1 in header and year2 in header:
            f_out = open('CityPopChg.csv',"wt")
            column_header = 'id, city, population_change\n'
            f_out.write(column_header)
            for city in city_dict:
                pop_change=abs((city_dict[city][year1]-city_dict[city][year2]))
                pop_change = round(pop_change,2)
                values = city_dict[city]['id'] + ',' + \
                          city + ',' + str(pop_change)
                f_out.write(values+'\n') 
            f_out.close()
            
            print('\n CityPopchg.csv for the %s and %s is created in the path'%(year1,year2))
            
    except:
            print('\nDont enter any characters or years out of range\n')
