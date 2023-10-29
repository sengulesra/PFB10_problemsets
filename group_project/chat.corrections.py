#!/usr/bin/env python3
import vcf
import pyVCF

def extract_information_from_vcf(vcf_file):
    # Open the VCF file
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    vcf_writer = vcf.Writer(open('output_annotated.vcf', 'w'), vcf_reader)

    for record in vcf_reader:
        # Extract SNP information
        if record.is_snp:
            print("SNP - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
                record.CHROM, record.POS, record.REF, record.ALT))

        # Extract INDEL information
        if record.is_indel:
            print("INDEL - Chromosome: {}, Position: {}, Reference: {}, Alt: {}".format(
                record.CHROM, record.POS, record.REF, record.ALT))

        # Extract CNV information (assuming copy number is available in the INFO field)
        if 'CN' in record.INFO:
            print("CNV - Chromosome: {}, Position: {}, Copy Number: {}".format(
                record.CHROM, record.POS, record.INFO['CN']))
        
        vcf_writer.write_record(record)

if __name__ == "__main__":
    vcf_file_path = 'tester_vcf.vcf'
    extract_information_from_vcf('/Users/pfb10/problemsets/group_project/tester_vcf.vcf')

