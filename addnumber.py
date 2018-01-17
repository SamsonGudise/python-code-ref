#!/usrbin/python
import argparse

parser = argparse.ArgumentParser(description="Process some intergers.",prog="addup")
parser.add_argument('ints', metavar='N',type=int,nargs='+',help='an interger for the accumulator')
parser.add_argument('--sum',dest='addsup', action='store_const',const=sum,default=max,help='sum the integers(default: find the max)')
args = parser.parse_args()
print(args.addsup(args.ints))
