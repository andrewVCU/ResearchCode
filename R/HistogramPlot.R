library(scales)
hist(YungSlug_BlastWithTaxon[YungSlug_BlastWithTaxon$Org == "PHG",]$Perc,
     main = "YungSlug Viral and Bacterial Blast Hits", xlab = "Percent Identity", ylim = c(0,6000), col =  alpha("blue", 0.4))
hist(YungSlug_BlastWithTaxon[YungSlug_BlastWithTaxon$Org == "BCT",]$Perc, 
     xlab = "Percent Identity", col = alpha("red", 0.4), add=TRUE, )
hist(YungSlug_BlastWithTaxon[YungSlug_BlastWithTaxon$Org == "ENV",]$Perc,
     col = alpha("yellow", 0.4), add=TRUE)

legend(70, 2700, title="Organisms", c("Viruses","Bacterial","Environmental"), fill=c("blue","red","yellow"))