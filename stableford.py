import sys
d = {
	-4:6,
	-3:5,
	-2:4,
	-1:3,
	0:2,
	1:1
}
golfers = {}
lines = sys.stdin.readlines()
pars = lines[0].strip().split()
indices = lines[1].strip().split()

i = 2
longest_name = 0
while i < len(lines):
	
	line = lines[i].strip().split()
	name = ' '.join(line[:-19])
	if len(name) > longest_name:
		longest_name = len(name)
	golfers[name] = 0
	stats = []
	j = 0
	while j < 18:
		stats.append([pars[len(pars)-1-j],indices[len(indices)-1-j],line[-1-j],0])
		j += 1
	stats = sorted(stats,key= lambda x:int(x[1]))
	handicap = int(line[-19])
	extra_shots = int(handicap / 18)
	leftover_shots = int(handicap % 18)
	for k in range(0,leftover_shots):
		stats[k][3] += 1
	for stat in stats:
		stat[3] += extra_shots
		try:
			total_score =   int(stat[2]) - int(stat[0]) - int(stat[3])
			if total_score in d:
				golfers[name] += d[total_score]
				
		except ValueError:
			pass
	i += 1
tuples = []
for key in golfers:
	tuples.append((key,golfers[key]))
tuples = reversed(sorted(tuples,key= lambda x:x[1]))
for(k,v) in tuples:
	sentence = "{:>{}} : {:>2}".format(k,longest_name,v)
	print(sentence)
