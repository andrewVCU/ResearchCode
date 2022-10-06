setwd("D:/IndependentStudy/Scripts/NotTheCreekData/")
library(scales)
hist(phiAGATE_rerunEntrez[phiAGATE_rerunEntrez$Org == "PHG",]$Perc,
     main = "phiAGATE Viral and Bacterial Blast Hits", xlab = "Percent Identity", ylim = c(0,3000), col =  alpha("blue", 0.4))
hist(phiAGATE_rerunEntrez[phiAGATE_rerunEntrez$Org == "BCT",]$Perc, 
     xlab = "Percent Identity", col = alpha("red", 0.4), add=TRUE, )
hist(phiAGATE_rerunEntrez[phiAGATE_rerunEntrez$Org == "ENV",]$Perc,
     col = alpha("yellow", 0.4), add=TRUE )

legend(70, 1500, title="Organisms", c("Viruses","Bacterial","Environmental"), fill=c("blue","red","yellow"))