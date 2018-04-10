import sys,os 

if len(sys.argv) == 1:
	print 'python 3.blastn_with_reference_genome.py reference_genome single_type output_name num_threads'
	sys.exit()

reference = sys.argv[1]
single_type = sys.argv[2]
output_name = sys.argv[3]
number_of_threads = sys.argv[4]

os.system('blastn -db '+sys.argv[1]+' -query '+sys.argv[2]+' -evalue 1e-100 -outfmt 6 -out '+sys.argv[3]+' -num_threads '+sys.argv[4])
