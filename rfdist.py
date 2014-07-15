import dendropy
import csv

## import ml tree and sample of trees to compare against it
ang_ml = dendropy.Tree.get_from_path('mltree/ang_ml.tre','nexus')
angtrees = dendropy.TreeList.get_from_path('subtrees/angtrees.tre','newick')
angrf = []
for tree in angtrees:
	angrf.append(ang_ml.symmetric_difference(tree))

## what happens when you remove lineterminator?
with open('angrf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in angrf:
		writer.writerow([val])

## repeat for other subtrees
gek_ml = dendropy.Tree.get_from_path('mltree/gek_ml.tre','nexus')
gektrees = dendropy.TreeList.get_from_path('subtrees/gektrees.tre','newick')
gekrf = []
for tree in gektrees:
	gekrf.append(gek_ml.symmetric_difference(tree))
with open('gekrf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in gekrf:
		writer.writerow([val])

igu_ml = dendropy.Tree.get_from_path('mltree/igu_ml.tre','nexus')
igutrees = dendropy.TreeList.get_from_path('subtrees/igutrees.tre','newick')
igurf = []
for tree in igutrees:
	igurf.append(igu_ml.symmetric_difference(tree))
with open('igurf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in igurf:
		writer.writerow([val])

lac_ml = dendropy.Tree.get_from_path('mltree/lac_ml.tre','nexus')
lactrees = dendropy.TreeList.get_from_path('subtrees/lactrees.tre','newick')
lacrf = []
for tree in lactrees:
	lacrf.append(lac_ml.symmetric_difference(tree))
with open('lacrf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in lacrf:
		writer.writerow([val])

ser_ml = dendropy.Tree.get_from_path('mltree/ser_ml.tre','nexus')
sertrees = dendropy.TreeList.get_from_path('subtrees/sertrees.tre','newick')
serrf = []
for tree in sertrees:
	serrf.append(ser_ml.symmetric_difference(tree))
with open('serrf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in serrf:
		writer.writerow([val])

sci_ml = dendropy.Tree.get_from_path('mltree/sci_ml.tre','nexus')
scitrees = dendropy.TreeList.get_from_path('subtrees/scitrees.tre','newick')
scirf = []
for tree in scitrees:
	scirf.append(sci_ml.symmetric_difference(tree))
with open('scirf.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for val in scirf:
		writer.writerow([val])


