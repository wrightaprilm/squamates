import dendropy
from dendropy.utility.fileutils import find_files

flist = find_files(top='.', filename_filter='*')
sqtrees = [dendropy.Tree.get_from_path(filename,"newick") for filename in flist]

i = 1
for tree in sqtrees:
    for edge in tree.preorder_edge_iter():
        if edge.length is not None:
            edge.length = edge.length*.6
#            edge.length = edge.length*1.3736721506706522
    print tree.length()
    tree.write_to_path('./rescaled/%s' % i, 'newick')
    i  = i + 1
