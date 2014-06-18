##For non-split BiSSE

library(diversitree)
library(ape)
data <- read.csv('/home/april/projectfiles/squamates/squam/PyronSmallParityData.csv', row.names=1)
output_vector <- vector()
ovip_root_vector <- vector()
vivp_root_vector <- vector()

a<- list.files(pattern="*tre")

model_fit <- function(tree_list){
for (x in tree_list){
phy <- read.tree(x)
pruned.tree<-drop.tip(phy, setdiff(phy$tip.label, row.names(data)))
sorteddata <- data[phy$tip.label, ]
no_na <- na.omit(sorteddata)
names(no_na) <- pruned.tree$tip.label
func <- make.bisse(pruned.tree, no_na)
sp<-starting.point.bisse(pruned.tree)
fit_bisse <- find.mle(func, sp)
st <- asr.marginal(func, coef(fit_bisse))
ovip_root_vector <- append(ovip_root_vector, c(st[,2][1], 'Oviparity'))
vivp_root_vector <- append(ovip_root_vector, c(st[,2][2], 'Viviparity'))
outname <- paste('./bisse/', x, '.pdf', sep='')
plot(pruned.tree, show.tip.label=FALSE)
fit_plot <- nodelabels(pie=t(st), piecol=1:2, cex=.5)
output_vector <- append(vec, c(fit_bisse$par[1:6], fit_bisse$lnLik))
lapply(output_vector, write, "model_params.csv", append=TRUE)
lapply(ovip_root_vector, write, "ovip_support.csv", append=TRUE)
lapply(vivip_root_vector, write, "vivip_support.csv", append=TRUE)
return(c(bisse_fits,st))
}
}

model_fit(a)

