all : unoptimized_model_fits branch_length_optimized_model_fits total_optimized_model_fits colorizer colorizerBL colorizerTotal counter counterBL counterTotal

unoptimized_model_fits: ./Trees/MLE/Dated/test* ./Scripts/bisseunopt.r
	R CMD BATCH ./Scripts/bisseunopt.r 
	
branch_length_optimized_model_fits: ./Trees/BranchLengthOptimized/Dated/test* ./Scripts/bisseBLopt.r
	R CMD BATCH ./Scripts/bisseBLopt.r 	

total_optimized_model_fits: ./Trees/TotalOptimization/Dated/test* ./Scripts/bisseTotalopt.r
	R CMD BATCH ./Scripts/bisseTotalopt.r 

colorizer: ./tip_annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'tip_annotated_*dated'

colorizerBL: ./tip_annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'tip_annotatedBL_*dated'
	
colorizerTotal: ./tip_annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'tip_annotatedTotal_*dated'

counter: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*.dated  

counterBL: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*BL*.dated
	
counterTotal: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*Total*.dated
