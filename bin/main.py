##############################################
#               Ashley Doerfler              #
#       Collaborator: Bennett Hamilton       #
#                 04-17-2024                 #
#              Project 1: Search             #
#                                            #
# Description: This program will find paths  #
# between cities provided by a given source  #
# file using BFS, Iterative deepening depth- #
# limited search, uniform cost search, and A*#
##############################################

# What is the main function?:
#   - Type of search passed in as parameter (bfs default)
#   - Other parameters: start city (-A), end city (-B), and
#                       source file

import argparse
import sys
from parse_file import Parse_File
from mapping import Mapping

def main():
    parser = setup_parser()
    args = parse_arguments(parser)

    parse_the_file = Parse_File(args.input)
    mapping = Mapping()

    city, lat, lon, connection_cities = parse_the_file.main()

    mapping.add_city(city, lat, lon, connection_cities)

def setup_parser():
    parser = argparse.ArgumentParser()
    # I took this from some code I wrote in my current research project
    # Add parser arguments. ex: parser.add_argument('-l', '--long_name', help='What is it for?', required=True/False)
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-A', '--start', help='Start city', required=True)
    parser.add_argument('-B', '--end', help='End city', required=True)
    parser.add_argument('-s', '--search', help='Search type: bfs, dls, ucs, or astar', default='bfs')
    return parser
  
def parse_arguments(parser):
    args = parser.parse_args()
    # Place any messages you may want
    return args

if __name__ == "__main__":
    sys.exit(main())