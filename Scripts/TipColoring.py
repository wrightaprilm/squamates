# Purpose: This script melds together your node labels from Diversitree with the tip-based data you've save in a csv. This allows you to appropriately colorize the tree in FigTree. If you don't use this script, the tree will have colors that extend to the parent node of the tips, leaving the tips black.
import dendropy
import sys
import pandas as pd
import os
from dendropy.utility.fileutils import find_files


# Import tree with node labels. Because we'll use a pandas dataframe to associate the tip data with the tree, we want to preserve the underscores, assuming they exist in your data file of tip states. If not, set to false.
taxa = dendropy.TaxonSet()
filter = sys.argv[2]
flist = find_files(top=sys.argv[1], filename_filter='%s*' % filter)
sqtrees = [dendropy.Tree.get_from_path(filename,"newick",taxon_set=taxa, preserve_underscores=True,extract_comment_metadata=True) for filename in flist]
data = pd.read_csv('./Data/PyronParityData.csv', index_col=0)


def label_nodes(sqtrees, data):
    '''Iterate over nodes, associating them with the tip states in the 
    pandas dataframe.'''
    for mle in sqtrees:
        for idx, nd in enumerate(mle.postorder_node_iter()):
            if nd.label is None:
                lookup = '{}'.format(nd.taxon)
                nd.label = int(data.ix[lookup])
            else: 
                pass

def colorize(labeled_trees):
    '''Associate value ranges with colors.'''
    for mle in sqtrees:
        for nd in mle.postorder_node_iter():    
            if nd.label == None:
                pass
            elif float(nd.label) == 0:
                nd.annotations.add_new(name = '!color', value = '#0000FF') #Dark blue, zeroes
            elif float(nd.label) > 0 and float(nd.label) < 0.5:
                nd.annotations.add_new(name = '!color', value = '#ff0000') #Red, strongly viviparous  
        mle.write_to_path('%s/tip_annotated_%s' % (sys.argv[1], 
        os.path.basename(filename)), 'nexus', suppress_annotations = False, 
        annotations_as_nhx=False, suppress_taxa_block=True,
        suppress_internal_taxon_labels=True)

if __name__ == '__main__':
    labeled_trees = label_nodes(sqtrees, data)
    colorize(labeled_trees)

# You now have a FigTree-readable nexus with node and tip annotations.

# 
# 
#     Copyright (c) <2014> <April Wright, wright.aprilm@gmail.com>
# 
# 
#     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
