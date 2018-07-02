

# IMPORTS

from __future__ import print_function
from orphics import maps,io,cosmology,lensing
from enlib import enmap,lensing as enlensing,resample,bench
import numpy as np
import os,sys



# ARGPARSE

import argparse
# Parse command line
parser = argparse.ArgumentParser(description='Do a thing.')
parser.add_argument("positional", type=str,help='Positional arg.')
parser.add_argument("-N", "--nsim",     type=int,  default=None,help="A description.")
parser.add_argument("-f", "--flag", action='store_true',help='A flag.')
required_args = parser.add_argument_group('Required arguments')
required_args.add_argument("--region",     type=str,help="Region name from input/regions.yaml",required=True)
args = parser.parse_args()


# MPI

comm = mpi.MPI.COMM_WORLD
rank = comm.Get_rank()
numcores = comm.Get_size()
Nsims = args.nsims
Njobs = Nsims + 1
num_each,each_tasks = mpi.mpi_distribute(Njobs,numcores)
if rank==0: print ("At most ", max(num_each) , " tasks...")
my_tasks = each_tasks[rank]
if rank==0: print ("Rank 0 done with task ", task+1, " / " , len(my_tasks))


# PRINT TRACEBACK

import traceback
traceback.print_exc()


# PATHS
PathConfig = io.load_path_config()
