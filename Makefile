model_fits: ../squam/scaled/*dated.tre bisse.r
	R CMD BATCH bisse.r 

split_model_fit: ../squam/scaled/*dated.tre splitbisse.r
	R CMD BATCH splitbisse.r

plot_model_params: ./modelop.csv plot.py
	python plot.py

plot_model_params: ./modelop.csv plot_support.py
	python plot_support.py
