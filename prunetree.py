#! /usr/bin/env python

## start with trees that have been pruned of taxa without parity mode (using R)

import dendropy

## operations for the ml tree
ml = dendropy.Tree.getfrompath(filename, "newick")
print(ml.description())
node_D = ml.find_node_with_taxon_label("Sphenodon punctatus")
ml.reroot_at_edge(node_D.edge, update_splits=True)
print(ml.description())

## get mrca nodes for clades
ang_mrca = ml.mrca(taxon_labels="Varanus_indicus", "Anniella_pulchra")
gek_mrca = ml.mrca(taxon_labels="Phelsuma_ornata", "Delma_impar")
igu_mrca = ml.mrca(taxon_labels="Iguana_iguana", "Chamaeleo_zeylanicus")
lac_mrca = ml.mrca(taxon_labels="Bipes_biporus", "Teius_teyou")
ser_mrca = ml.mrca(taxon_labels="Nerodia_rhombifer", "Liotyphlops_albirostris")
sci_mrca = ml.mrca(taxon_labels="Plestiodon_fasciatus", "Acontias_percivali")

## pruning and writing trees goes here
ang_ml.seed_node = ang_mrca
ang_ml.write.to.path("ang_ml.tre","newick")
ml.update_splits()
gek_ml.seed_node = gek_mrca
gek_ml.write.to.path("gek_ml.tre","newick")
ml.update_splits()
igu_ml.seed_node = igu_mrca
igu_ml.write.to.path("igu_ml.tre","newick")
ml.update_splits()
lac_ml.seed_node = lac_mrca
lac_ml.write.to.path("lac_ml.tre","newick")
ml.update_splits()
ser_ml.seed_node = ser_mrca
ser_ml.write.to.path("ser_ml.tre","newick")
ml.update_splits()
sci_ml.seed_node = sci_mrca
sci_ml.write.to.path("sci_ml.tre","newick")
ml.update_splits()

## import list of trees of type newick from filepath and verify number of trees with print
flist = find_files(top=o_file, filename_filter='*.con')
sqtrees = [dendropy.TreeList.getfrompath(filename,"newick") for filename in flist]
print(sqtrees.description())

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
	print(tree.description())
	
	rep_ang_mrca = tree.mrca(taxon_labels="Varanus_indicus", "Anniella_pulchra")
	ang_tree.seed_node = rep_ang_mrca
	angtrees.append(ang_tree)
	tree.update_splits()	

	rep_gek_mrca = tree.mrca(taxon_labels="Phelsuma_ornata", "Delma_impar")
	gek_tree.seed_node = rep_gek_mrca
	gektrees.append(gek_tree)
	tree.update_splits()

	rep_igu_mrca = tree.mrca(taxon_labels="Iguana_iguana", "Chamaeleo_zeylanicus")
	igu_tree.seed_node = rep_igu_mrca
	igutrees.append(igu_tree)
	tree.update_splits()

	rep_lac_mrca = tree.mrca(taxon_labels="Bipes_biporus", "Teius_teyou")
	lac_tree.seed_node = rep_lac_mrca
	lactrees.append(lac_tree)
	tree.update_splits()
	
	rep_ser_mrca = tree.mrca(taxon_labels="Nerodia_rhombifer", "Liotyphlops_albirostris")
	ser_tree.seed_node = rep_ser_mrca
	sertrees.append(ser_tree)
	tree.update_splits()

	rep_sci_mrca = tree.mrca(taxon_labels="Plestiodon_fasciatus", "Acontias_percivali")
	sci_tree.seed_node = rep_sci_mrca
	scitrees.append(sci_tree)
	tree.update_splits()


## looking at distance with subclades from a point estimate and a sample of trees
RF = [tree1.symmetric_difference(tree) for tree in sqtrees]



