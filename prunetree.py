#! /usr/bin/env python

import dendropy
from dendropy.utility.fileutils import find_files

## operations for the ml tree
ml = dendropy.Tree.get_from_path("filename", "format")
print(ml.description())
node_D = ml.find_node_with_taxon_label("Sphenodon punctatus")
ml.reroot_at_edge(node_D.edge, update_splits=True)
ml.write_to_path("filenamererooted", "newick")

## clone rerooted tree for pruning
ml0 = dendropy.Tree(ml)
ml1 = dendropy.Tree(ml)
ml2 = dendropy.Tree(ml)
ml3 = dendropy.Tree(ml)
ml4 = dendropy.Tree(ml)
ml5 = dendropy.Tree(ml)

## get mrca nodes for clades
ang_mrca = ml0.mrca(taxon_labels=["Varanus indicus", "Anniella pulchra"])
gek_mrca = ml1.mrca(taxon_labels=["Phelsuma ornata", "Delma impar"])
igu_mrca = ml2.mrca(taxon_labels=["Iguana iguana", "Chamaeleo zeylanicus"])
lac_mrca = ml3.mrca(taxon_labels=["Bipes biporus", "Teius teyou"])
ser_mrca = ml4.mrca(taxon_labels=["Nerodia rhombifer", "Liotyphlops albirostris"])
sci_mrca = ml5.mrca(taxon_labels=["Plestiodon fasciatus", "Acontias percivali"])

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

## empty tree lists for pruned trees
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
	tree.write_to_path("treelistrerooted.tre","newick")

## clone tree list for pruning, will take a while
sq0 = dendropy.TreeList(sqtrees)
sq1 = dendropy.TreeList(sqtrees)
sq2 = dendropy.TreeList(sqtrees)
sq3 = dendropy.TreeList(sqtrees)
sq4 = dendropy.TreeList(sqtrees)
sq5 = dendropy.TreeList(sqtrees)

## pruning from lists of trees
for tree in sq0:
	rep_ang_mrca = tree.mrca(taxon_labels=["Varanus indicus", "Anniella pulchra"])
	ang_tree=dendropy.Tree()
	ang_tree.seed_node = rep_ang_mrca
	angtrees.append(ang_tree)
for tree in sq1:	
	rep_gek_mrca = tree.mrca(taxon_labels=["Phelsuma ornata", "Delma impar"])
	gek_tree=dendropy.Tree()	
	gek_tree.seed_node = rep_gek_mrca
	gektrees.append(gek_tree)
for tree in sq2:
	rep_igu_mrca = tree.mrca(taxon_labels=["Iguana iguana", "Chamaeleo zeylanicus"])
	igu_tree=dendropy.Tree()
	igu_tree.seed_node = rep_igu_mrca
	igutrees.append(igu_tree)
for tree in sq3:
	rep_lac_mrca = tree.mrca(taxon_labels=["Bipes biporus", "Teius teyou"])
	lac_tree=dendropy.Tree()
	lac_tree.seed_node = rep_lac_mrca
	lactrees.append(lac_tree)
for tree in sq4:
	rep_ser_mrca = tree.mrca(taxon_labels=["Nerodia rhombifer", "Liotyphlops albirostris"])
	ser_tree=dendropy.Tree()	
	ser_tree.seed_node = rep_ser_mrca
	sertrees.append(ser_tree)
for tree in sq5:
	rep_sci_mrca = tree.mrca(taxon_labels=["Plestiodon fasciatus", "Acontias percivali"])
	sci_tree=dendropy.Tree()
	sci_tree.seed_node = rep_sci_mrca
	scitrees.append(sci_tree)


## write tree lists
angtrees.write_to_path("angtrees.tre", "newick")
gektrees.write_to_path("gektrees.tre", "newick")
igutrees.write_to_path("igutrees.tre", "newick")
lactrees.write_to_path("lactrees.tre", "newick")
sertrees.write_to_path("sertrees.tre", "newick")
scitrees.write_to_path("scitrees.tre", "newick")




