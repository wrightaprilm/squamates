import pandas as pd
import ggplot

def plot_params():
	dat = pd.read_csv('/home/april/projectfiles/squamates/squamates/modelop_indexed.csv', header=False)
	dat = dat.dropna()
	dat.columns = ['Lambda','Mu','Q','Likelihood','Parity']
	mle_dict_o = {'Lambda':5, 'Mu':5, 'Q':5, 'Likelihood':5 }
	mle_dict_v = {'Lambda':5, 'Mu':5, 'Q':5, 'Likelihood': 5}
	columns =list(dat.columns)
#We don't want to try and plot parity mose. Pop it on out.
	columns.pop()
	for column in columns:
		dat[column] = dat[column].apply(float)
		li = list(dat[column])
		plot = ggplot(dat, aes(x=li, fill='Parity')) + geom_density(alpha=.25) + geom_vline(x=mle_dict_o[column], color='salmon', size = 5) + geom_vline(x=mle_dict_v[column], color='teal', size = 5)
		ggsave(plot, column, 'png')

plot_params()


