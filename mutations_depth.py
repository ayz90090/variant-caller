import os
from indel_sites import indel_sites
from snps import repeat_point
from pathlib import Path
import argparse 
from argparse import ArgumentParser

def file_in_cwd(file_path):
    """Custom type: ensures file exists in current directory"""
    cwd_file = Path.cwd() / file_path
    if cwd_file.is_file():
        return str(cwd_file.absolute())  # Return absolute path
    else:
        raise argparse.ArgumentTypeError(f"'{file_path}' not found in {Path.cwd()}")

# Create parser
parser = argparse.ArgumentParser(description="Process FASTA files")
parser.add_argument("input_fasta", 
                   type=file_in_cwd, 
                   help="Input FASTA file (in current directory)")
parser.add_argument("-o", "--output", 
                   default="output.fasta",
                   type=str,
                   help="Output file (default: output.fasta in current dir)")
parser.add_argument("output_vcf", 
                    type=str,
                    help="Output file for stores of indels and SNPs")

args = parser.parse_args()

with open(args.input_fasta, 'r') as f:
    lines = f.readlines()
    header = lines[0]
    sequence_joined = ''.join(line for line in lines[1:])

new_sequence, store = repeat_point(sequence_joined, 10) # list object of two items [0] = sequence and [1] = store of snps 
mutated_indels_genome, indel_storage = indel_sites(new_sequence)

## write indels.fasta with output of snps
with open(args.output, 'x') as f: # how to handle filenameexists error ???????????
    f.write(f"{header}{mutated_indels_genome}")

## write text file 
with open(args.output_vcf, 'w') as c:
    c.write('SNP sites: \n')
    for i, x in store.items(): 
        c.write(f'Site \t Original/Mutant \n {i}:{x} \n')
    c.write(f'\n INDEL sites: \n')
    for i, x in indel_storage.items(): 
        c.write(f'Site \t Original/Mutant \n {i}:{x} \n')

