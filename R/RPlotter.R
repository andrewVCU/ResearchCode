install.packages("ggpubr")
setwd("D:/IndependentStudy/Scripts/NotTheCreekData")

data <- read.table("NotTheCreek_TopHitsBactVirusTest.out", sep = "\t", header = FALSE, nrows = 538, col.names = paste0("C",1:13), stringsAsFactors = FALSE)

x <- data$C1
y <- data$C3
org <- data$C13

plot(x,y, main = "Top Hits, Bacteria vs Virus\n NotTheCreek", 
     xlab = "Gene", ylab = "Percent Identity of Hit", 
     pch = 20, ylim = c(0,120),col = ifelse(org == "PHG", "blue", "red"))
