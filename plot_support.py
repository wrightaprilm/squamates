import pandas as pd
import ggplot

def plot_params():
	dat = pd.read_csv('/home/april/projectfiles/squamates/squamates/supproot_indexed.csv', header=False)
	dat = dat.dropna()
	dat.columns = ['Support Value', 'Parity']
	dat['Support Value'] = dat['Support Value'].apply(float)
	plot = ggplot(dat, aes(x='Support Value', fill='Parity')) + geom_density(alpha=.25) + geom_vline(x=.07, color='teal', size = 5) + geom_vline(x=.93, color='salmon', size = 5)
	ggsave(plot, 'support', 'png')



plot_params()


