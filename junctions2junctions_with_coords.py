#-------------------------------------------------------------------------------
# Name:        junctions2junctions_with_coords
# Purpose:     Converts the junctions.dat to junctions_with_coords.dat
#              which will be imporetd into NetLogo model
#
# Author:      Saeed Hajebi
#
# Created:     28/06/2013
# Copyright:   (c) Saeed Hajebi 2013
# Licence:
#-------------------------------------------------------------------------------

import sys

def main():
    prefix = sys.argv[1] + '_'
    junctions = open(prefix + 'junctions.dat', 'r')
    coordinates = open(prefix + 'coordinates.dat', 'r')
    nodes = open(prefix + 'junctions_with_coords.dat', 'w')

    for junctions_line in junctions:
        if junctions_line.strip():
            junction_id, elevation, demand, pattern = junctions_line.strip().split()[:4]
            if pattern == ';' : pattern = '0'
            if not pattern.isdigit(): pattern = '"' + pattern + '"'
            for coordinates_line in coordinates:
                if coordinates_line.strip():
                    node_id , x_cor, y_cor = coordinates_line.strip().split()[:3]
                    if node_id == junction_id:
                        junction_id = '"' + junction_id + '"'
                        pattern = '"' + pattern + '"'

                        node_line = junction_id + ' ' + elevation + ' ' + demand + ' ' + pattern + ' ' + x_cor + ' ' + y_cor  + '\n'
                        nodes.write(node_line)
                        break
                break

    junctions.close()
    coordinates.close()
    nodes.close()

if __name__ == '__main__':
    main()
