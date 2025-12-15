# variant-caller

Repository Contents: 
 
•	Simulated Mutant Genome: Validation code python file – 
•	How to use: 
•	Download dependencies (files and conda environment) 
•	Make current directory 
•	Run python file from command line with three input variables 
•	Name of reference file to be simulated for mutations (download) 
•	Output name of mutated genome (extension = .fasta)
•	Output name of mutant sites (extension = .txt) 

•	Python file for simulating depth – using bash  
•	How to use: 
•	Open terminal and run ./bash_script mutated_genome.fasta 
•	Mutated_genome coverage needs length of genome, use unix to do that 
•	Run wgsim (make sure “conda install samtools::wgsim”) 
•	Output wgsim is the two fastq files 
•	Test files 
•	Pipeline bash 
•	How to use: 
•	Receive fasta, fastq files (in total 3 variables) 
•	Output bam file for vcf calling (snippy and Bcftools per genome) 
