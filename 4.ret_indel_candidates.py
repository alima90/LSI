import sys

if len(sys.argv) == 1:
	print 'python 4.ret_indel_candidates blast_out_from_step3'
	sys.exit()

blastfile = open(sys.argv[1]).readlines()

contig = ''
tmp = []
chk = 0
for line in blastfile:
	cell = line.strip().split('\t')
	if contig != '' and contig != cell[0]:
		if len(tmp) != 1:
			if tmp[0].split('\t')[1] == tmp[1].split('\t')[1]:
				if int(tmp[0].split('\t')[6]) >= int(tmp[1].split('\t')[7]) or int(tmp[0].split('\t')[7]) <= int(tmp[1].split('\t')[6]):
					if (int(tmp[0].split('\t')[9])-int(tmp[0].split('\t')[8]) > 0 and int(tmp[1].split('\t')[9])-int(tmp[1].split('\t')[8]) > 0) or (int(tmp[0].split('\t')[9])-int(tmp[0].split('\t')[8]) < 0 and int(tmp[1].split('\t')[9])-int(tmp[1].split('\t')[8]) < 0):
						pos=[int(tmp[1].split('\t')[6]), int(tmp[1].split('\t')[7]), int(tmp[0].split('\t')[6]), int(tmp[0].split('\t')[7])]
						pos.remove(max(pos))
						pos.remove(min(pos))
						if abs(pos[0] - pos[1]) < 1000000:
							umcstart = tmp[0].split('\t')[0].split(';')[2].split('-')[0]
							umcend = tmp[0].split('\t')[0].split(';')[2].split('-')[1]
							start1 = tmp[0].split('\t')[6]
							end1 = tmp[0].split('\t')[7]
							start2 = tmp[1].split('\t')[6]
							end2  = tmp[1].split('\t')[7]
							if int(start1) > int(start2):
								if int(end2) - int(umcstart) <= 300 and int(umcend)-int(start1) <= 300:
									chk = 1
							elif int(start2) > int(start1):
								if int(end1) - int(umcstart) <= 300 and int(umcend)-int(start2) <= 300:
									chk = 1
							if chk == 1:
								print tmp[0]
								print tmp[1]
		tmp = []
		chk = 0	
	contig = cell[0]
	tmp.append(line.strip())

if len(tmp) != 1:
	if tmp[0].split('\t')[1] == tmp[1].split('\t')[1]:
		if int(tmp[0].split('\t')[6]) >= int(tmp[1].split('\t')[7]) or int(tmp[0].split('\t')[7]) <= int(tmp[1].split('\t')[6]):
			if (int(tmp[0].split('\t')[9])-int(tmp[0].split('\t')[8]) > 0 and int(tmp[1].split('\t')[9])-int(tmp[1].split('\t')[8]) > 0) or (int(tmp[0].split('\t')[9])-int(tmp[0].split('\t')[8]) < 0 and int(tmp[1].split('\t')[9])-int(tmp[1].split('\t')[8]) < 0):
				pos=[int(tmp[1].split('\t')[6]), int(tmp[1].split('\t')[7]), int(tmp[0].split('\t')[6]), int(tmp[0].split('\t')[7])]
				pos.remove(max(pos))
				pos.remove(min(pos))
				if abs(pos[0]-pos[1]) < 1000000:
					umcstart = tmp[0].split('\t')[0].split(';')[2].split('-')[0]
					umcend = tmp[0].split('\t')[0].split(';')[2].split('-')[1]
					start1 = tmp[0].split('\t')[6]
					end1 = tmp[0].split('\t')[7]
					start2 = tmp[1].split('\t')[6]
					end2  = tmp[1].split('\t')[7]
					if int(start1) > int(start2):
						if int(end2) - int(umcstart) <= 300 and int(umcend)-int(start1) <= 300:
							chk = 1
					elif int(start2) > int(start1):
						if int(end1) - int(umcstart) <= 300 and int(umcend)-int(start2) <= 300:
							chk = 1
					if chk == 1:
						print tmp[0]
						print tmp[1]
