model_fits: *dated.tre BISSE.rmd
	R CMD BATCH BISSE.rmd 

split_model_fit: *dated.tre splitbisse.r
	R CMD BATCH splitbisse.t
