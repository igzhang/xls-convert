import argparse
import pyexcel

parser = argparse.ArgumentParser(description='This is a excel converter')
parser.add_argument("-i ",'--input', type=str, help='resource file', required=True)
parser.add_argument('-o', "--output", type=str, help='dest file', required=True)

args = parser.parse_args()

pyexcel.save_as(file_name=args.input, dest_file_name=args.output)
