import re
from mapping import Mapping

class Parse_File:
    
    def __init__(self, file_path):
        self.file_path = file_path
        mapping = Mapping()

    def main(self):
        print('Parsing file...\n') # For testing purposes: Remove later

        for line in open(self.file_path, 'r'):
            print(line) # For testing purposes: Remove later

            # ex. line: nice 43 43 12 N 7 15 59 E --> va-marseille 197
            line = line.split(' ')
            for word in line:
                print(word) # For testing purposes: Remove later
                



