all : unoptimized_model_fits branch_length_optimized_model_fits total_optimized_model_fits colorizer colorizerBL colorizerTotal counter counterBL counterTotal

unoptimized_model_fits: ./Trees/MLE/Dated/test* ./Scripts/bisseunopt.r
	R CMD BATCH ./Scripts/bisseunopt.r 
	
branch_length_optimized_model_fits: ./Trees/BranchLengthOptimized/Dated/test* ./Scripts/bisseBLopt.r
	R CMD BATCH ./Scripts/bisseBLopt.r 	

total_optimized_model_fits: ./Trees/TotalOptimization/Dated/test* ./Scripts/bisseTotalopt.r
	R CMD BATCH ./Scripts/bisseTotalopt.r 

colorizer: ./annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'annotatedUnopt_*dated'

colorizerBL: ./annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'annotatedBL_*dated'
	
colorizerTotal: ./annotated* ./Scripts/TipColoring.py
	python ./Scripts/TipColoring.py . 'annotatedTotal_*dated'

counter: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*Unopt*.dated  

counterBL: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*BL*.dated
	
counterTotal: ./annotated* ./Scripts/ChangeCounter.py
	python ./Scripts/ChangeCounter.py . colorized*Total*.dated
