import sys,os
if len(sys.argv) == 1:
	print 'python 1.blastn_between.unmappedNwhole.py Ordinary_contigs Orphan_contigs>=2k num_threads output_name'
	sys.exit()
whole_read_contig=sys.argv[1]
both_unmapped_read_contig=sys.argv[2]
number_of_threads=sys.argv[3]
output_name = sys.argv[4]

os.system('makeblastdb -in '+sys.argv[1]+' -dbtype nuc')
os.system('blastn -db '+sys.argv[1]+' -query '+sys.argv[2]+' -evalue 1e-100 -outfmt 6 -num_alignments 1 -num_threads '+sys.argv[3]+' -out '+sys.argv[4])
