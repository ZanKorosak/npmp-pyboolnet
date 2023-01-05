import pyboolnet
from pyboolnet.repository import get_primes
from pyboolnet.file_exchange import bnet2primes
from pyboolnet.interaction_graphs import primes2igraph, igraph2image, local_igraph_of_state, add_style_interactionsigns
from pyboolnet.state_space import random_state
from pyboolnet.phenotypes import compute_phenotypes, compute_phenotype_diagram, create_phenotypes_piechart
from pyboolnet.attractors import compute_attractors
from pyboolnet.state_transition_graphs import create_stg_image

im_dir = './images/'

bnet = """
    v1,    !v2
    v2,    !v3
    v3,    !v1
"""

primes = bnet2primes(bnet)
primes = get_primes("remy_tumorigenesis")


print(primes)

"""
create_stg_image(primes, update="asynchronous", fname_image=im_dir + "igraph.pdf")
create_stg_image(primes, update="asynchronous", fname_image=im_dir + "igraph2.pdf", styles=["anonymous", "sccs"])

igraph = primes2igraph(primes)
for x in igraph.nodes:
    if "GF" in x:
        igraph.nodes[x]["shape"] = "square"
        igraph.nodes[x]["fillcolor"] = "lightblue"

igraph2image(igraph, im_dir + "igraph3.pdf")

print(igraph.nodes(), igraph.edges())
"""