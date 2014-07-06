import pandas as pd
from ggplot import *
import sys

def data_clean():
	dat = pd.read_csv(sys.argv[1], header=False)
	dat1 = dat
	dat['Parity'] = 'Viviparity'
	dat1['Parity'] = 'Oviparity'
	dat = dat.drop(['q1','lambda1','mu1'], axis=1)
	dat1 = dat1.drop(['q0','lambda0','mu0'], axis=1)
	dat0.columns = ['Lambda','Mu','Q','Likelihood','Parity']
	dat1.columns = ['Lambda','Mu','Q','Likelihood','Parity']
	joined_mat = dat.append(dat1)
	return(joined_mat)

def plot_params():
	dat = data_clean()
	mle_dict_o = {'Lambda':4.242674e-02, 'Mu':8.908371e-07, 'Q':7.529796e-04, 'Likelihood':-16735.45 }
	mle_dict_v = {'Lambda':5.734688e-02, 'Mu':9.791236e-06, 'Q':6.054965e-03, 'Likelihood':-16735.45}
	columns =list(total_mat.columns)
#We don't want to try and plot parity mose. Pop it on out.
	columns.pop()
	for column in columns:
		total_mat[column] = total_mat[column].apply(float)
		plot = ggplot(total_mat, aes(x=column, fill='Parity')) + geom_density(alpha=.25) + geom_vline(x=mle_dict_o[column], color='salmon', size = 5) + geom_vline(x=mle_dict_v[column], color='teal', size = 5)
		ggsave(plot, column, 'png')

plot_params()


