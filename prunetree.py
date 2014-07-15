#! /usr/bin/env python

import dendropy
from dendropy.utility.fileutils import find_files

## operations for the ml tree
ml = dendropy.Tree.get_from_path("filename", "newick")
print(ml.description())
node_D = ml.find_node_with_taxon_label("Sphenodon punctatus")
ml.reroot_at_edge(node_D.edge, update_splits=True)

## get mrca nodes for clades
ang_mrca = ml.mrca(taxon_labels=["Varanus indicus", "Anniella pulchra"])
gek_mrca = ml.mrca(taxon_labels=["Phelsuma ornata", "Delma impar"])
igu_mrca = ml.mrca(taxon_labels=["Iguana iguana", "Chamaeleo zeylanicus"])
lac_mrca = ml.mrca(taxon_labels=["Bipes biporus", "Teius teyou"])
ser_mrca = ml.mrca(taxon_labels=["Nerodia rhombifer", "Liotyphlops albirostris"])
sci_mrca = ml.mrca(taxon_labels=["Plestiodon fasciatus", "Acontias percivali"])

## pruning and writing trees goes here
ang_ml=dendropy.Tree()
ang_ml.seed_node = ang_mrca
ang_ml.write_to_path("ang_ml.tre","newick")

gek_ml=dendropy.Tree()
gek_ml.seed_node = gek_mrca
gek_ml.write_to_path("gek_ml.tre","newick")

igu_ml=dendropy.Tree()
igu_ml.seed_node = igu_mrca
igu_ml.write_to_path("igu_ml.tre","newick")

lac_ml=dendropy.Tree()
lac_ml.seed_node = lac_mrca
lac_ml.write_to_path("lac_ml.tre","newick")

ser_ml=dendropy.Tree()
ser_ml.seed_node = ser_mrca
ser_ml.write_to_path("ser_ml.tre","newick")

sci_ml=dendropy.Tree()
sci_ml.seed_node = sci_mrca
sci_ml.write_to_path("sci_ml.tre","newick")


## uncomment if trees are in separate files, import list of trees of type newick
##flist = find_files(top='trees', filename_filter='*.dated.tre')
##sqtrees = [dendropy.TreeList.get_from_path(filename,"newick") for filename in flist]
##print(sqtrees.description(2))

## empty lists for pruned trees
angtrees = dendropy.TreeList()
gektrees = dendropy.TreeList()
igutrees = dendropy.TreeList()
lactrees = dendropy.TreeList()
sertrees = dendropy.TreeList()
scitrees = dendropy.TreeList()

## same operations as above but for a sample of trees
for tree in sqtrees:
	rep_node_D = tree.find_node_with_taxon_label("Sphenodon punctatus")
	tree.reroot_at_edge(rep_node_D.edge, update_splits=True)
	rep_ang_mrca = tree.mrca(taxon_labels=["Varanus indicus", "Anniella pulchra"])
	ang_tree=dendropy.Tree()
	ang_tree.seed_node = rep_ang_mrca
	angtrees.append(ang_tree)
	tree.update_splits()	
	rep_gek_mrca = tree.mrca(taxon_labels=["Phelsuma ornata", "Delma impar"])
	gek_tree=dendropy.Tree()	
	gek_tree.seed_node = rep_gek_mrca
	gektrees.append(gek_tree)
	tree.update_splits()
	rep_igu_mrca = tree.mrca(taxon_labels=["Iguana iguana", "Chamaeleo zeylanicus"])
	igu_tree=dendropy.Tree()
	igu_tree.seed_node = rep_igu_mrca
	igutrees.append(igu_tree)
	tree.update_splits()
	rep_lac_mrca = tree.mrca(taxon_labels=["Bipes biporus", "Teius teyou"])
	lac_tree=dendropy.Tree()
	lac_tree.seed_node = rep_lac_mrca
	lactrees.append(lac_tree)
	tree.update_splits()
	rep_ser_mrca = tree.mrca(taxon_labels=["Nerodia rhombifer", "Liotyphlops albirostris"])
	ser_tree=dendropy.Tree()	
	ser_tree.seed_node = rep_ser_mrca
	sertrees.append(ser_tree)
	tree.update_splits()
	rep_sci_mrca = tree.mrca(taxon_labels=["Plestiodon fasciatus", "Acontias percivali"])
	sci_tree=dendropy.Tree()
	sci_tree.seed_node = rep_sci_mrca
	scitrees.append(sci_tree)
	tree.update_splits()

## empty lists for RF distance by subclade
allrf = []
angrf = []
gekrf = []
igurf = []
lacrf = []
serrf = []
scirf = []


## looking at distance with subclades from a point estimate and a sample of trees

allrf.append[ml.symmetric_difference(tree) for tree in sqtrees]
angrf.append[ang_ml.symmetric_difference(tree) for tree in angtrees]
gekrf.append[gek_ml.symmetric_difference(tree) for tree in gektrees]
igurf.append[igu_ml.symmetric_difference(tree) for tree in igutrees]
lacrf.append[lac_ml.symmetric_difference(tree) for tree in lactrees]
serrf.append[ser_ml.symmetric_difference(tree) for tree in sertrees]
scirf.append[sci_ml.symmetric_difference(tree) for tree in scitrees]


