import dendropy
import sys
import pandas as pd
import os
from dendropy.utility.fileutils import find_files


data = pd.read_csv('./Data/PyronParityData.csv', index_col=0, header=False)

taxa = dendropy.TaxonSet()
flist = find_files(top=sys.argv[1], filename_filter=sys.argv[2])
sqtrees = [dendropy.Tree.get_from_path(filename,"newick",taxon_set=taxa, preserve_underscores=True,extract_comment_metadata=True) for filename in flist]

def check_labeling(trees):
    labeled_trees = []
    for mle in sqtrees:     
        for idx, nd in enumerate(mle.postorder_node_iter()):
            if nd.label is None:
                lookup = '{}'.format(nd.taxon)
                nd.label = int(data.ix[lookup])
                labeled_trees.append(mle)
            else: 
                pass
                labeled.trees.append(mle)
    return(labeled_trees)

def counting(labeled_trees):    
    putative_c = []
    putative_co = []
    mega_list = []
    for mle in sqtrees:
        for index, node in enumerate(mle.postorder_node_iter()):
            total.append(index)
            if node.parent_node is None:
                pass
            elif .5 < float(node.label) < 1 or float(node.label) == 0:    #Is likely oviparous 
                if float(node.parent_node.label) < .5 : #List of nodes that demonstrate change away from oviparity. 
                    if node.taxon is not None :
                        putative_co.append([node.parent_node.label, node.taxon])
                    else:
                        putative_co.append(node.parent_node.label)
                        for nd in node.child_nodes():
#                       print nd.taxon
                            pass
            elif 0 < float(node.label) < .5 or float(node.label) == 1: 
                if float(node.parent_node.label) > .5: 
                    putative_c.append([node.parent_node.label,node.taxon])     
    mega_list.append((len(putative_c))
    rev_mat = pd.DataFrame(mega_list)
#    rev_mat.index = flist
    return(rev_mat)
    
if __name__ == '__main__':
    labeled_trees = check_labeling(sqtrees)
    output_matrix = counting(labeled_trees)
    output_matrix.to_csv('%s/%s_changes.csv' % (sys.argv[1], sys.argv[2]))
    


# Copyright (c) <2014> <April Wright, wright.aprilm@gmail.com>
# 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the #"Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, #distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the #following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF #  #MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY #  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE # #SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
