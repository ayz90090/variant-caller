#!/bin/bash 

vcf1=$1
vcf2=$2

bcftools sort "$vcf1" -Oz -o "${vcf1}.sorted.vcf"
bcftools index -t "${vcf1}.sorted.vcf"
  
bcftools sort "$vcf2" -Oz -o "${vcf2}.sorted.vcf"
bcftools index -t "${vcf2}.sorted.vcf"

bcftools merge --force-samples -m snp,ins,del \
    "${vcf1}.sorted.vcf" \
    "${vcf2}.sorted.vcf" \
    -Oz -o merged_vcf.vcf

bcftools index -t merged_vcf.vcf

echo "Merged VCF: merged_vcf.vcf"
