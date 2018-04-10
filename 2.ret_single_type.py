import sys

if len(sys.argv) == 1:
	print 'python 2.ret_single_type.py Ordinary_contigs Orphan_contigs>=2k blast_output_from_step1'
	sys.exit()

whole_read_contig=open(sys.argv[1]).readlines()
both_unmapped_read_contig=open(sys.argv[2]).readlines()
blastfile = open(sys.argv[3]).readlines()

bu_length={}
wr_length={}
wr_seq={}
for bu in both_unmapped_read_contig:
	if '>' in bu:
		bu_length[bu.split()[0].split('>')[1]] = bu.split()[1]
for wr in whole_read_contig:
	if '>' in wr:
		name = wr.split()[0].split('>')[1]
		wr_length[wr.split()[0].split('>')[1]] = wr.split()[1]
	else:
		wr_seq[name]=wr.strip()
for line in blastfile:
	cell = line.strip().split('\t')
	query = cell[0]
	subject = cell[1]
	identity = cell[2]
	if identity != '100.00':continue
	length = cell[3]
	chk = 0
	sub_start = cell[8]
	sub_end = cell[9]
	if sub_start == '1' or sub_end == '1':continue
	if length == bu_length[query] and wr_length[subject] != sub_start and wr_length[subject] != sub_end:
		print '>'+subject+';'+wr_length[subject]+';'+str(min([int(sub_start),int(sub_end)]))+'-'+str(max([int(sub_start),int(sub_end)]))
		print wr_seq[subject]	
			
