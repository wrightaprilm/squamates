##For non-split BiSSE
##Load dependencies
library(diversitree)
library(ape)
#For this analysis, we use a data file that's been made a little smaller than the 8000-taxon data set. Load it.
data <- read.csv('/home/april/projectfiles/squamates/squam/PyronParityData.csv', row.names=1)
# Initialize vectors. These will be used for formatting output.
output_vector <- vector()
ovip_root_vector <- vector()
vivp_root_vector <- vector()

#File currently set up to accept input from Make, or if trees in working directory
a<- list.files(pattern="*tre")

#Main function to fit model to each tree in BS sample
model_fit <- function(tree_list){
for (x in tree_list){

#For each tree in our vector of trees, read it in and distill down the tree to the shared tips between it and the data set
	phy <- read.tree(x)
	pruned.tree<-drop.tip(phy, setdiff(phy$tip.label, row.names(data)))
	sorteddata <- data[phy$tip.label, ]
	no_na <- na.omit(sorteddata)
	names(no_na) <- pruned.tree$tip.label
	#Make the BiSSE function
	func <- make.bisse(pruned.tree, no_na)
	sp<-starting.point.bisse(pruned.tree)
	# Find MLE and use it to do ancestral state reconstruction 
	fit_bisse <- find.mle(func, sp)
	st <- asr.marginal(func, coef(fit_bisse))
	#Add root states to a vector of states  
	ovip_root_vector <- append(ovip_root_vector, c(st[,2][1], 'Oviparity'))
	vivp_root_vector <- append(ovip_root_vector, c(st[,2][2], 'Viviparity'))
	#Plot tree
	plot(pruned.tree, show.tip.label=FALSE)
	fit_plot <- nodelabels(pie=t(st), piecol=1:2, cex=.5)
	#Output various parameters: the model and ancestral states 
	output_vector <- append(vec, c(fit_bisse$par[1:6], fit_bisse$lnLik))
	lapply(output_vector, write, "model_params.csv", append=TRUE)
	lapply(ovip_root_vector, write, "ovip_support.csv", append=TRUE)
	lapply(vivip_root_vector, write, "vivip_support.csv", append=TRUE)
return(c(output_vector, ovip_root, vivip_root))
}
}

#Call the function if you want
model_fit(a)

