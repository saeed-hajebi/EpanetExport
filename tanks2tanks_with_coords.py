#-------------------------------------------------------------------------------
# Name:        tanks2tanks_with_coords
# Purpose:     Converts tanks.dat to tanks_with_coords.dat to enable us reading EPANET tanks into NetLogo tanks
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
    tanks = open(prefix + 'tanks.dat', 'r')
    coordinates = open(prefix + 'coordinates.dat', 'r')
    tanks_with_coords = open(prefix + 'tanks_with_coords.dat', 'w')

    for tank in tanks:
        if tank.strip():
            tank_id, elevation, initLevel, minLevel, maxLevel, diameter, minVol = tank.strip().split()[:7]
            # I ignored reading volCurve as it is empty in most of the cases
            for coordinates_line in coordinates:
                if coordinates_line.strip():
                    node_id , x_cor, y_cor = coordinates_line.strip().split()[:3]
                    if node_id == tank_id:
                        tank_id = '"' + tank_id + '"'
                        tanks_with_coord = tank_id + ' ' + elevation + ' ' + initLevel + ' ' + minLevel + ' ' +\
                                           maxLevel + ' ' + diameter + ' ' + minVol + ' ' + \
                                           x_cor + ' ' + y_cor + '\n'
                        tanks_with_coords.write(tanks_with_coord)
                        break




if __name__ == '__main__':
    main()
