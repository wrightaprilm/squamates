model_fits: ./trees/*.tre bisse.r
	R CMD BATCH bisse.r 

plot_model_params: ./modelop.csv plot.py
	python plot.py

plot_model_params: ./modelop.csv plot_support.py
	python plot_support.py
