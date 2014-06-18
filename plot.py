
dat = pd.read_csv('/home/april/projectfiles/squamates/squamates/dat', header=False)
dat['b'] = 'Transition rate of oviparity to viviparity'
dat['b'][34:] = 'Transition rate of viviparity to oviparity'
dat = dat.drop(dat.inddat[[33]])
dat = dat.dropna()
dat.columns = ['dattiction Rates','b']
dat['dattiction Rates'] = dat['dattiction Rates'].apply(float)
ggplot(dat, aes(x='dattinction Rates', fill='b')) + geom_density(alpha=.25) + geom_vline(x=7.529796e-04, color='salmon') + geom_vline(x=6.054965e-03, color='teal')


