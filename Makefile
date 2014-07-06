model_fits: ./trees/*.tre bisse.r
	R CMD BATCH bisse.r 

plot_model_params: ./model_params.csv plot_dist.py 
	python plot_dist.py model_params.csv

plot_model_params: ./model_params.csv plot_support.py
	python plot_support.py
