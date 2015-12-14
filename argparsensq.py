#!/bin/bash
import argparse
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('--size',nargs="+",required=True,help="num")
	args=parser.parse_args()
	print(args.accumulate(args.integers))
def main():
	parse()
if _name_=="_main_"
	exit(main())
