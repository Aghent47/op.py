from argparse import ArgumentParser
from sys import argv
import os

parser = ArgumentParser(description='programa de conjunto')
parser.add_argument('-v','--variable', help="variables",nargs=2)
parser.add_argument('-p','--union', help="union", type=int, default=2)
args = parser.parse_args()
if args.variable and args.union:
      print(args.variable)
      print(args.union)



 
 