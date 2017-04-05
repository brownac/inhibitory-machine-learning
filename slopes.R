setwd("~/PycharmProjects/machine_learning/")
dat = read.csv("in.csv", header=F, col.names=c(1:101)); head(dat)
dat.slopes = c()
for (i in 1:nrow(dat)) {
	dat.slopes[i] = (dat$X55[i] - dat$X53[i]) / 2
}
dat.slopes
mean(dat.slopes)
