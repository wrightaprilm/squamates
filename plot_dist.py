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
	mypb_mle_dict_o = {'Lambda':3.126341e-02, 'Mu':8.043702e-06, 'Q':6.693207e-04, 'Likelihood':-18088.72 }
	mypb_mle_dict_v = {'Lambda':3.554580e-02, 'Mu':9.342949e-07, 'Q':2.932465e-03, 'Likelihood':-18088.72}
	pb_mle_dict_o = {'Lambda':0.0628, 'Mu':0.0000, 'Q':0.0007, 'Likelihood':-16735.45 }
	pb_mle_dict_v = {'Lambda':0.0848, 'Mu':0.0270, 'Q':0.0059, 'Likelihood':-16735.45}
	columns =list(joined_mat.columns)
#We don't want to try and plot parity mose. Pop it on out.
	columns.pop()
	for column in columns:
		joined_mat[column] = joined_mat[column].apply(float)
		plot = ggplot(joined_mat, aes(x=column, fill='Parity')) + geom_density(alpha=.25) + geom_vline(x=pb_mle_dict_o[column], color='salmon', size = 5) + geom_vline(x=pb_mle_dict_v[column], color='teal', size = 5)
		ggsave(plot, column, 'png')

plot_params()



