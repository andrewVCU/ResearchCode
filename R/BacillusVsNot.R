library(scales)
hist(YungSlugWithTaxonNamesAndGenus[YungSlugWithTaxonNamesAndGenus$Org == "BCT",]$Perc,
     main = "YungSlug: Bacillus vs Not Bacillus", xlab = "Percent Identity",ylab = "Frequency", ylim = c(0,3000), col =  alpha("blue", 0.4))
hist(YungSlugWithTaxonNamesAndGenus[YungSlugWithTaxonNamesAndGenus$Genus == "Bacillus",]$Perc, 
     col = alpha("red", 0.4), add=TRUE)

legend(70, 1500, title="Genera", c("All","Bacillus"), fill=c("blue","red"))