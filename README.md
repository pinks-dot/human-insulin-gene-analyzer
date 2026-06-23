


 # HUMAN INSULIN GENE ANALYZER 

A Python tool for performing basic sequence analysis on the human insulin gene(INS).
This project reads a raw nucleotide sequence and computes key descriptive statistics commonly used in introductory bioinformatics workflows.


# #Overview
The Human Insulin Gene Analyzer takes a FASTA/text sequence file as an input and performs fundamental sequence-level computations - nucleotide composition, GC/AT content, start codon detection, and reverse sequence generation.
This project uses a partial sequence of the human insulin gene(INS), not the whole gene, and was built as hands-on introduction to programmatic sequence analysis.


# FEATURES
  
  * Reads a gene sequence directly from a file.
  * Calculates sequence length.
  * Counts individual nucleotides (A,T,G,C).
  * Calculates GC content and AT content (%).
  * Detects start codons(ATG).
  * Generates reverse sequence.

# TECH 
1. LANGUAGE = Python 3
2. EDITOR = VS Code

PREREQUISITES
 * Python 3.x installed on your system (Modern standard, unicode by default).


# Sample Output
  
  sequence length : 349 bp
  GC content      : 63.32 % 
  AT content      : 36.68 % 
  start codon     : 1


# PROJECT STRUCTURE

      human-insulin-gene-analyzer/
          main.py                # Main Python program
          insulin_gene.txt       # Human insulin gene sequence
          README.md              # Project documentation


# Future improvements 
  
   ~ codon usage frequecy analysis
   ~ visualize nucleotide composition with charts
   ~ DNA to RNA transcription
   ~ protien translation
   ~ mutation detection
   ~ add unit tests


 AUTHOR

 S.SHERYL 

LICENSE
  For educational purposes.









    

