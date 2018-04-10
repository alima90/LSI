# LSI
The pipeline for Large Sequence Insertion prediction

This pipeline is developed for Linux environment

For large sequence insertion prediction, you need prepare high quality reference genome and Illumina sequencing data equal or higher than 20X

# Prerequisite
  BLAST+ package

# Download
git-clone https://github.com/alima90/LSI

# Usage
python LargeInsertionPrediction.py Ordinary_contigs Orphan_contigs>=2k num_threads Reference_genome.fa

# Post-processing
You should check LSI candidates manually. If LSIs were BLASTed in ambiguous regions("Ns"), it is false positive. So, please filter out them

# Contact
If you have any question about LSI pipeline, please contact to me (alima9002@gmail.com)
