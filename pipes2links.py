#-------------------------------------------------------------------------------
# Name:        pipes2links
# Purpose:     Converts pipes.dat to links.dat to enable us reading EPANET pipes into NetLogo links
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
    pipes = open(prefix + 'pipes.dat', 'r')
    nodes = open(prefix + 'links.dat', 'w')

    for pipe in pipes:
        if pipe.strip():
            pipe_id , pipe_node1, pipe_node2, pipe_length, pipe_diameter, pipe_roughness, pipe_minorLoss, pipe_status = pipe.strip().split()[:8]
            pipe_id = '"' + pipe_id + '"'
            pipe_node1 = '"' + pipe_node1 + '"'
            pipe_node2 = '"' + pipe_node2 + '"'
            pipe_status = '"' + pipe_status + '"'
            link_line = pipe_id + ' ' + pipe_node1 + ' ' + pipe_node2 + ' ' + pipe_length + ' ' + \
                        pipe_diameter + ' ' + pipe_roughness + ' ' + pipe_minorLoss + ' ' + pipe_status + '\n'
            nodes.write(link_line)

    pipes.close()
    nodes.close()

if __name__ == '__main__':
    main()
