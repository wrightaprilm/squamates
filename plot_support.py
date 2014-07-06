import pandas
from ggplot import *
import sys

my_supp_est = {'oviparity':.93, 'viviparity':.07}
pb_est = {'oviparity':.05, 'viviparity':.95}

def data_clean():
	dat = pandas.read_csv(sys.argv[1], header=False)
 	dat.columns = ['Support Value']
	vivip_supp = [1-x for x in dat['Support Value']]
	dat1 = pandas.DataFrame(vivip_supp)
	dat1['Parity'] = 'Viviparity'
	dat['Parity'] = 'Oviparity'
	dat1.columns = ['Support Value', 'Parity']
	joined_mat = dat.append(dat1)
	joined_mat = joined_mat.dropna()
	return(joined_mat)


def plot_params():
	dat = data_clean()
	dat['Support Value'] = dat['Support Value'].apply(float)
	plot = ggplot(dat, aes(x='Support Value', fill='Parity')) + geom_density(alpha=.25) + geom_vline(x=supp_dict['viviparity'], color='teal', size = 5) + geom_vline(x=supp_dict['oviparity'], color='salmon', size = 5)
	ggsave(plot, 'support', 'png')

plot_params()


