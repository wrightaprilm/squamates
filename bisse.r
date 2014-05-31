##For non-split BiSSE

library(diversitree)
library(ape)
data <- read.csv('/home/april/projectfiles/squamates/squam/PyronSmallParityData.csv', row.names=1)
lk <- vector(mode="list")
lkp <- vector(mode="list")
bisse_fits <- vector(mode="list")
stat_list <- vector(mode="list")
fit_plots <- vector(mode="list")
a<- list.files(pattern="*tre")

model_fit <- function(tree_list){
for (x in tree_list){
phy <- read.tree(x)
pruned.tree<-drop.tip(phy, setdiff(phy$tip.label, row.names(data)))
sorteddata <- data[phy$tip.label, ]
no_na <- na.omit(sorteddata)
names(no_na) <- pruned.tree$tip.label
func <- make.bisse(pruned.tree, no_na)
lk <- append(lk, func)
sp<-starting.point.bisse(pruned.tree)
lkp <- append(lkp, sp)
fit_bisse <- find.mle(func, sp)
bisse_fits <- append(bisse_fits, fit_bisse)
st <- asr.marginal(func, coef(fit_bisse))
stat_list <- append(stat_list, st)
outname <- paste('./bisse/', x, '.pdf', sep='')
plot(pruned.tree, show.tip.label=FALSE)
fit_plot <- nodelabels(pie=t(st), piecol=1:2, cex=.5)
jpeg(outname)
print(bisse_fits)
dev.off()
return(bisse_fits)
}
}

model_fit(a)

