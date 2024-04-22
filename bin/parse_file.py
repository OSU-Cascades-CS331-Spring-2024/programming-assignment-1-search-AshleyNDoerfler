import re
from cities import City
from mapping import Mapping

class Parse_File:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.mapping = Mapping()

    def main(self):
        print('Parsing file...') # For testing purposes: Remove later

        for line in open(self.file_path, 'r'):
            # ex. line: nice 43 43 12 N 7 15 59 E --> va-marseille 197
            
            line = line.split(' ')
            # ex. line: ['nice', '43', '43', '12', 'N', '7', '15', '59', 'E', '-->', 'va-marseille', '197']
            
            city_name = line[0]

            lat = line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4]
            lon = line[5] + ' ' + line[6] + ' ' + line[7] + ' ' + line[8]

            connection_cities = []

            for i in range(10, len(line) - 1, 2):
                # TODO: remove va- from city name
                line[i] = re.sub(r'va-', '', line[i])
                print("connections", line[i]) # For testing purposes: Remove later

                # Remove end of line character from last city connection
                line[i + 1] = line[i + 1].replace('\n', '')
                
                connection_cities.append(line[i] + ' ' + line[i + 1])

            city = City(city_name, lat, lon)

            # For testing purposes: Remove later
            print(city_name)
            print(connection_cities)

            self.mapping.add_cities(city, connection_cities)

        print('File parsed.') # For testing purposes: Remove later

        return self.mapping

            




