import sys
print(sys.path)

from pyboolnet import  attractors
bnet = """
    v1,    !v2
    v2,    !v3
    v3,    !v1
"""
# Print all methods of the pbnet module
print(dir(pyboolnet))
print(pyboolnet.__loader__)

primes = pyboolnet.file_exchange.bnet2primes(bnet)

pyboolnet.interaction_graphs.create_image(primes, "./images/interaction_graph.pdf")