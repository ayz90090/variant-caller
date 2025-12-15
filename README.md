# variant-caller

<h1> Repository Contents: </h1>
 
<h4> 	Simulated Mutant Genome: Validation code python file </h4>
<p>Test files</p>
<ul>   
  <li> EcoliK12-MG1655.fasta</li>
  <li> NC320767.1.fasta </li>
 </ul>
<p> How to use: </p>
<ul> <li>Download dependencies (files and conda environment (samtools, bcftools, snippy)</li>
•	<li> Change to files directory </li>
<li> Run python file from command line with three input variables </li>
  <ol> Mandatory: Reference fasta to be mutated </ol>
  <ol> Mandatory: Output VCF file name (truth) </ol>
  <ol> -o output fasta file name </ol>
</ul>

<ul>
<h4> Bash script for simulating 100bp reads at 30x depth </h4>	
<p>How to use: </p>
<li> Open terminal and run with three input variables </li>
<li> Calculate number of reads required for simulating 30x coverage </li>
<li> Runs Wgsim (make sure “conda install samtools::wgsim”) </li>	
<li> Outputs two fastq files into your current directory </li>

<h4> Pipeline bash  </h4>
<p> How to use: </p>
<ul> 
<li> Receive fasta, fastq files (in total 3 variables) </li>
<li> Output bam file for vcf calling (snippy and Bcftools per genome) </li>
</ul>

