import pandas as pd
from ggplot import *
import sys

def data_clean():
	dat = pd.read_csv(sys.argv[1], header=False)
	dat1 = dat
	dat = dat.drop(['q1','lambda1','mu1'], axis=1)
	dat1 = dat1.drop(['q0','lambda0','mu0'], axis=1)
	dat['Parity'] = 'Viviparity'
	dat1['Parity'] = 'Oviparity'
	dat.columns = ['Lambda','Mu','Q','Likelihood','Parity']
	dat1.columns = ['Lambda','Mu','Q','Likelihood','Parity']
	joined_mat = dat.append(dat1)
	return(joined_mat)


def plot_params():
	joined_mat = data_clean()
	mypb_examl_o = {'Lambda':0.03776491, 'Mu':6.542256e-06, 'Q':0.001180185, 'Likelihood':-17446.8 } #0 -> 1 rate
	mypb_examl_v = {'Lambda':0.03881011, 'Mu':4.199473e-07, 'Q':0.001060784, 'Likelihood':-17446.8} # 1 -> 0 rate
	pb_mle_dict_o = {'Lambda':0.0628, 'Mu':0.0000, 'Q':0.0007, 'Likelihood':-16735.45 } # 0 -> 1 rate
	pb_mle_dict_v = {'Lambda':0.0848, 'Mu':0.0270, 'Q':0.0059, 'Likelihood':-16735.45} # 1 -> 0 rate
	scale_1 = {'Lambda' : 2.740322e-02, 'Mu' : 4.477777e-05, 'Q' : 4.967371e-04 }
	scale_2 = {'Lambda' : 2.866520e-02, 'Mu' : 8.101550e-05, 'Q' : 2.706007e-03 }
	pb_rescale_o = {'Lambda' : 2.507966e-02, 'Mu': 9.610080e-09, 'Q'  4.431603e-04 }
	pb_rscale_v = { 'Lambda' : 3.398085e-02, 'Mu': 5.505829e-08, 'Q': 3.567300e-03}	
	
	     
	columns =list(joined_mat.columns)
#We don't want to try and plot parity mose. Pop it on out.
	columns.pop()
	for column in columns:
		joined_mat[column] = joined_mat[column].apply(float)
		plot = ggplot(joined_mat, aes(x=column, fill='Parity')) + geom_density(alpha=.25) + geom_vline(xintercept=scale_v[column], color='salmon', size = 5) + geom_vline(xintercept=scale_o[column], color='teal', size = 5) + theme_bw()
		ggsave(plot, column, 'png')

plot_params()


