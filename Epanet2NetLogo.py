#-------------------------------------------------------------------------------
# Name:        Epanet2NetLogo
# Purpose:     Coverting EPANET Water Simulation Software inpout files to R (plain) files
#
# Author:      Saeed Hajebi
#
# Created:     28/06/2013
# Copyright:   (c) Saeed Hajebi 2013
# Licence:
#-------------------------------------------------------------------------------

import re
import sys

def main():
    epanet_file = open(sys.argv[1] + '.inp', 'r')

    while 1:
        line = epanet_file.readline()
        if not line:
            break

        match = re.search(r'JUNCTIONS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_junctions.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'RESERVOIRS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_reservoirs.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'TANKS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_tanks.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'PIPES', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_pipes.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'PUMPS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_pumps.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'VALVES', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_valves.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'DEMANDS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_demands.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)

        match = re.search(r'STATUS', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_status.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)


        '''
            To do: reading demand patterns is not like the other components,
            as demands for different nodes are different
        '''


        match_others = re.search(r'PATTERNS', line)
        if match_others:
            file = open(sys.argv[1] + '_others.dat', 'w')
            file.writelines(line)
            file.writelines('\n')
            line = epanet_file.readline()
            while 1:
                line = epanet_file.readline()
                if not line:
                    file.close()
                    break
                else:
                    file.writelines(line)

    '''
    Reading the coordiantes of the nodes, pumps, reservoirs, tanks, etc.
    '''
    epanet_file = open(sys.argv[1] + '.inp','r')
    while 1:
        line = epanet_file.readline()
        if not line:
            break

        match = re.search(r'COORDINATES', line)
        if match:
            line = epanet_file.readline()
            file = open(sys.argv[1] + '_coordinates.dat', 'w')
            while 1:
                line = epanet_file.readline()
                match = re.search(r'\[', line)
                if match:
                    file.close()
                    break
                else:
                    file.writelines(line)



if __name__ == '__main__':
    main()
