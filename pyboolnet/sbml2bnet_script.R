args = commandArgs(trailingOnly=TRUE)

library.path <- .libPaths()
install.packages('BoolNet')

print(library.path)
library('BoolNet', lib.loc=library.path)


net <- loadSBML(file + ".sbml")
saveNetwork(net, file+ ".bnet")

