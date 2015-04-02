# -*- coding: utf-8 -*-
import os
import subprocess
import argparse


__version__ = '0.0.1'

def parse_args():
    parser = argparse.ArgumentParser(description="srst2 analyzing pipeline")
    parser.add_argument('--version', action='version', version='%(prog)s ' +  __version__)
    parser.add_argument('--accessions', type=str, required=True, help='NCBI SRA accessions')

def run_pipeline(accessions):
	with open(accessions, 'r') as fi:
		accs = fi.read().split("\n")

def main():
	args = parse_args()
	run_pipeline(args.)

if __name__ == '__main__':
	main()
