#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saeed
#
# Created:     02/07/2013
# Copyright:   (c) Saeed 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
     prefix = sys.argv[1] + '_'
     pumps = open(prefix + 'pumps.dat', 'r')

     pumps4NetLogo = open(prefix + 'pumps4NetLogo.dat', 'w')

     for pumps_line in pumps:
        if pumps_line.strip():
            pump_id, node1, node2, parameters = pumps_line.strip().split()[:4]
            if not pump_id.isdigit(): pump_id = '"' + pump_id + '"'
            node1 = '"' + node1 + '"'
            node2 = '"' + node2 + '"'
            if not parameters.isdigit(): parameters = '"' + parameters + '"'
            pump_line = pump_id + ' ' + node1 + ' ' + node2 + ' ' + parameters + '\n'
            pumps4NetLogo.write(pump_line)

if __name__ == '__main__':
    main()
