import dendropy

t = dendropy.Tree()
t.read_from_path('pyron_Scaledtree.tre','newick')
node_D = t.find_node_with_taxon_label("Sphenodon punctatus")
t.reroot_at_edge(node_D.edge, update_splits=True)
skinks = ['Plestiodon fasciatus', 'Acontias percivali']
skink_mrca = t.mrca(taxon_labels=skinks)
ig = ['Iguana iguana', 'Chamaeleo roperi']
ig_mrca = t.mrca(taxon_labels=ig)
gek = ['Phelsuma ornata', 'Delma impar']
gek_mrca = t.mrca(taxon_labels=gek)
serp = ['Nerodia rhombifer', 'Liotyphlops albirostris']
serp_mrca = t.mrca(taxon_labels=serp)
ang = ['Varanus indicus', 'Anniella pulchra']
ang_mrca = t.mrca(taxon_labels=ang)
lac = ['Bipes biporus', 'Teius teyou']
lac_mrca = t.mrca(taxon_labels=lac)

skink_tree = t.prune_subtree(ig_mrca)
skink_tree = t.prune_subtree(gek_mrca) 
skink_tree = t.prune_subtree(serp_mrca) 
skink_tree = t.prune_subtree(ang_mrca) 
skink_tree = t.prune_subtree(lac_mrca)
skink_tree.write_to_path('skink_treepb', 'nexus')


ig_tree = t.prune_subtree(skink_mrca)
ig_tree = t.prune_subtree(gek_mrca) 
ig_tree = t.prune_subtree(serp_mrca) 
ig_tree = t.prune_subtree(ang_mrca) 
ig_tree = t.prune_subtree(lac_mrca)
ig_tree.write_to_path('ig_treepb', 'nexus')

gek_tree = t.prune_subtree(skink_mrca)
gek_tree = t.prune_subtree(ig_mrca) 
gek_tree = t.prune_subtree(serp_mrca) 
gek_tree = t.prune_subtree(ang_mrca) 
gek_tree = t.prune_subtree(lac_mrca)
gek_tree.write_to_path('ig_treepb', 'nexus')
 
serp_tree = t.prune_subtree(skink_mrca)
serp_tree = t.prune_subtree(ig_mrca) 
serp_tree = t.prune_subtree(gek_mrca) 
serp_tree = t.prune_subtree(ang_mrca) 
serp_tree = t.prune_subtree(lac_mrca)
serp_tree.write_to_path('serp_treepb', 'nexus')

ang_tree = t.prune_subtree(skink_mrca)
ang_tree = t.prune_subtree(ig_mrca) 
ang_tree = t.prune_subtree(gek_mrca) 
ang_tree = t.prune_subtree(serp_mrca) 
ang_tree = t.prune_subtree(lac_mrca)
ang_tree.write_to_path('ang_treepb', 'nexus')

lac_tree = t.prune_subtree(skink_mrca)
lac_tree = t.prune_subtree(ig_mrca) 
lac_tree = t.prune_subtree(gek_mrca) 
lac_tree = t.prune_subtree(ang_mrca) 
lac_tree = t.prune_subtree(serp_mrca)
lac_tree.write_to_path('lac_treepb', 'nexus')





