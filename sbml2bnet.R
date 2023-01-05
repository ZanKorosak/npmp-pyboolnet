library('BoolNet')

file='Montagud2021_Prostate_Cancer'

net <- loadSBML(paste(file,".sbml", sep=""))
saveNetwork(net, paste(file,".bnet", sep=""))
