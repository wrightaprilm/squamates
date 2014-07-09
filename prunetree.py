#! /usr/bin/env python

## start with trees that have been pruned of taxa without parity mode

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

## same operations as above
for tree in sqtrees:
	ang_mrca = tree.mrca(taxon_labels="Varanus_indicus", "Anniella_pulchra")
	gek_mrca = tree.mrca(taxon_labels="Phelsuma_ornata", "Delma_impar")
	igu_mrca = tree.mrca(taxon_labels="Iguana_iguana", "Chamaeleo_zeylanicus")
	lac_mrca = tree.mrca(taxon_labels="Bipes_biporus", "Teius_teyou")
	ser_mrca = tree.mrca(taxon_labels="Nerodia_rhombifer", "Liotyphlops_albirostris")
	sci_mrca = tree.mrca(taxon_labels="Plestiodon_fasciatus", "Acontias_percivali")


RF = [tree1.symmetric_difference(tree) for tree in sqtrees]



