setwd("D:/IndependentStudy/Scripts/NotTheCreekData/")
library(scales)
hist(NotTheCreekWTaxonNamesTest[NotTheCreekWTaxonNamesTest$Org == "PHG",]$Perc,
     main = "NotTheCreek Viral and Bacterial Blast Hits", xlab = "Percent Identity", col =  alpha("blue", 0.4))
hist(NotTheCreekWTaxonNamesTest[NotTheCreekWTaxonNamesTest$Org == "BCT",]$Perc, 
     xlab = "Percent Identity", col = alpha("red", 0.4), add=TRUE, )

legend(70, 1500, title="Organisms", c("Virus", "Bacteria"), fill=c("blue", "red"))