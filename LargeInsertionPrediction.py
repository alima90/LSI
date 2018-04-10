import sys,os

if len(sys.argv) == 1:
	print 'python LargeInsertionPrediction.py W-contig U-contig num_threads Reference.fa'
	sys.exit()
whole_read_contigs=sys.argv[1]
both_unmapped_read_contig_longer_than_2k=sys.argv[2]
number_of_threads=sys.argv[3]
reference = sys.argv[4]
#bamfile = sys.argv[5]

name = sys.argv[1].split('/')[-1]
print 'python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/1.blastn_between.unmappedNwhole.py '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+name+'.blastn'
os.system('python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/1.blastn_between.unmappedNwhole.py '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+name+'.blastn')
print 'python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/2.ret_single_type.py '+sys.argv[1]+' '+sys.argv[2]+' '+name+'.blastn > '+ name+'.blastn.single_type'
os.system('python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/2.ret_single_type.py '+sys.argv[1]+' '+sys.argv[2]+' '+name+'.blastn > '+ name+'.blastn.single_type')
print 'python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/3.blastn_with_reference_genome.py '+reference+' '+name+'.blastn.single_type '+name+'.blastn.single_type.blastn '+sys.argv[3]
os.system('python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/3.blastn_with_reference_genome.py '+reference+' '+name+'.blastn.single_type '+name+'.blastn.single_type.blastn '+sys.argv[3])
print 'python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/4.ret_indel_candidates.py '+name+'.blastn.single_type.blastn > '+name+'.blastn.single_type.blastn.indel_candidates'
os.system('python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/4.ret_indel_candidates.py '+name+'.blastn.single_type.blastn > '+name+'.blastn.single_type.blastn.indel_candidates')
#print 'python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/5.read_evidence.py '+name+'.blastn.single_type.blastn.indel_candidates '+ bamfile +' '+reference + ' > '+name+'.blastn.single_type.blastn.indel_candidates.read_evidence'
#os.system('python '+'/'.join(sys.argv[0].split('/')[0:-1])+'/5.read_evidence.py '+name+'.blastn.single_type.blastn.indel_candidates '+ bamfile +' '+reference + ' > '+name+'.blastn.single_type.blastn.indel_candidates.read_evidence')



