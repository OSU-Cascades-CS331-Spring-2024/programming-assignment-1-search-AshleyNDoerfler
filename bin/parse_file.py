import re
from mapping import Mapping

class Parse_File:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.mapping = Mapping()

    def main(self):
        print('Parsing file...') # For testing purposes: Remove later

        for line in open(self.file_path, 'r'):
            print(line) # For testing purposes: Remove later
            # ex. line: nice 43 43 12 N 7 15 59 E --> va-marseille 197
            
            line = line.split(' ')
            # ex. line: ['nice', '43', '43', '12', 'N', '7', '15', '59', 'E', '-->', 'va-marseille', '197']
            
            city = line[0]

            lat = line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4]
            lon = line[5] + ' ' + line[6] + ' ' + line[7] + ' ' + line[8]

            connection_cities = []

            for i in range(10, len(line) - 1, 2):
                connection_cities.append(line[i] + ' ' + line[i + 1])

            print(connection_cities) # For testing purposes: Remove later

            return city, lat, lon, connection_cities


            




