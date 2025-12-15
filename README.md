# variant-caller

<h1> Repository Contents: </h1>
 
<h4> 	Simulated Mutant Genome: Validation code python file </h4>
<p> How to use: </p>
<ul> <li>Download dependencies (files and conda environment)</li>
•	<li> Make current directory </li>
<li> Run python file from command line with three input variables</li> 
<li> Name of reference file to be simulated for mutations (download) </li>	
<li> Output name of mutated genome (extension = .fasta) </li>
<li> Output name of mutant sites (extension = .txt) </li>	
</ul>
<ul>
<h4> Python file for simulating depth – using bash  </h4>	
<p>How to use: </p>
<li> Open terminal and run ./bash_script mutated_genome.fasta </li>
<li> Mutated_genome coverage needs length of genome, use unix to do that  </li>
<li> Run wgsim (make sure “conda install samtools::wgsim”) </li>	
<li> Output wgsim is the two fastq files  </li>

 <p>Test files</p>
 <ul>
  <li> EcoliK12-MG1655.fasta</li>
  <li> NC320767.1.fasta </li>
 </ul>

<h4> Pipeline bash  </h4>
<ul> 
<li> How to use: </li>
<li> Receive fasta, fastq files (in total 3 variables) </li>
<li> Output bam file for vcf calling (snippy and Bcftools per genome) </li>
</ul>

