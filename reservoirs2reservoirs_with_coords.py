#-------------------------------------------------------------------------------
# Name:        reservoirs2reservoirs_with_coords.py
# Purpose:     Converts reservoirs.dat to reservoirs_with_coords.dat to enable us reading EPANET reservoirs into NetLogo
#
# Author:      Saeed Hajebi
#
# Created:     01/07/2013
# Copyright:   (c) Saeed Hajebi 2013
# Licence:
#-------------------------------------------------------------------------------

import sys

def main():
    prefix = sys.argv[1] + '_'
    reservoirs = open(prefix + 'reservoirs.dat', 'r')
    coordinates = open(prefix + 'coordinates.dat', 'r')
    reservoirs_with_coords = open(prefix + 'reservoirs_with_coords.dat', 'w')
    elevation = '-100'
    
    for reservoir in reservoirs:
        if reservoir.strip():
            reservoir_id, head = reservoir.strip().split()[:2]
            # I ignored reading pattern as in most of the cases it's empty. it should: be reservoir_id, head, pattern
            for coordinates_line in coordinates:
                if coordinates_line.strip():
                    node_id , x_cor, y_cor = coordinates_line.strip().split()[:3]
                    if node_id == reservoir_id:
                        reservoir_id = '"' + reservoir_id + '"'
                        reservoir_with_coord = reservoir_id + ' ' + elevation + ' ' + head + ' ' + x_cor + ' ' + y_cor + '\n'
                        reservoirs_with_coords.write(reservoir_with_coord)
                        break

    reservoirs.close()
    coordinates.close()
    reservoirs_with_coords.close()


if __name__ == '__main__':
    main()
