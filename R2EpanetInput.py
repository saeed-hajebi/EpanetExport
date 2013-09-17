#-------------------------------------------------------------------------------
# Name:        R2EpanetInput
# Purpose:     Coverting R (plain) files to EPANET Water Simulation Software inpout files
#
# Author:      Saeed Hajebi
#
# Created:     28/06/2013
# Copyright:   (c) Saeed Hajebi 2013
# Licence:
#-------------------------------------------------------------------------------
import sys

def main():
    rexport = open(sys.argv[1]+'_.inp', 'w')
    prefix = sys.argv[1] + '_'

    junctions = open(prefix + 'junctions.dat','r');
    rexport.writelines('[JUNCTIONS]\n')
    rexport.writelines(';ID              	Elev        	Demand      	Pattern\n')
    for line in junctions:
        rexport.writelines(line)
    junctions.close()

    reservoirs = open(prefix + 'reservoirs.dat','r');
    rexport.writelines('[RESERVOIRS]\n')
    rexport.writelines(';ID              	Head        	Pattern         \n')
    for line in reservoirs:
        rexport.writelines(line)
    reservoirs.close()

    tanks = open(prefix + 'tanks.dat','r');
    rexport.writelines('[TANKS]\n')
    rexport.writelines(';ID              	Elevation   	InitLevel   	MinLevel    	MaxLevel    	Diameter    	MinVol      	VolCurve\n')
    for line in tanks:
        rexport.writelines(line)
    tanks.close()

    pipes = open(prefix + 'pipes.dat','r');
    rexport.writelines('[PIPES]\n')
    rexport.writelines(';ID              	Node1           	Node2           	Length      	Diameter    	Roughness   	MinorLoss   	Status\n')
    for line in pipes:
        rexport.writelines(line)
    pipes.close()

    pumps = open(prefix + 'pumps.dat','r');
    rexport.writelines('[PUMPS]\n')
    rexport.writelines(';ID              	Node1           	Node2           	Parameters\n')
    for line in pumps:
        rexport.writelines(line)
    pumps.close()

    valves = open(prefix + 'valves.dat','r');
    rexport.writelines('[VALVES]\n')
    rexport.writelines(';ID              	Node1           	Node2           	Diameter    	Type	Setting     	MinorLoss   \n')
    for line in valves:
        rexport.writelines(line)
    valves.close()

    valves = open(prefix + 'demands.dat','r');
    rexport.writelines('[DEMANDS]\n')
    rexport.writelines(';Junction        	Demand      	Pattern         	Category\n')
    for line in valves:
        rexport.writelines(line)
    valves.close()

    valves = open(prefix + 'status.dat','r');
    rexport.writelines('[STATUS]\n')
    rexport.writelines(';ID              	Status/Setting\n')
    for line in valves:
        rexport.writelines(line)
    valves.close()

    others = open(prefix + 'others.dat','r');
    rexport.writelines('\n\n;Other EPANET file contents. \n')
    for line in others:
        rexport.writelines(line)
    others.close()


if __name__ == '__main__':
    main()
