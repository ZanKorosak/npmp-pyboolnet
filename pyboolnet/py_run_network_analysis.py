import pyboolnet
from pyboolnet.repository import get_primes
from pyboolnet.file_exchange import bnet2primes
from pyboolnet.file_exchange import bnet2primes
from pyboolnet.interaction_graphs import primes2igraph, igraph2image, local_igraph_of_state, add_style_interactionsigns
from pyboolnet.state_space import random_state
from pyboolnet.phenotypes import compute_phenotypes, compute_phenotype_diagram, create_phenotypes_piechart
from pyboolnet.attractors import compute_attractors, create_attractor_report
from pyboolnet.state_transition_graphs import create_stg_image
from pyboolnet.basins_of_attraction import weak_basin, strong_basin, cycle_free_basin
import json


import pprint
pp = pprint.PrettyPrinter(indent=4)
im_dir = './images/'


def reprissilator():
    bnet = """
        v1,    !v2
        v2,    !v3
        v3,    !v1
    """
    primes = bnet2primes(bnet)
    igraph = primes2igraph(primes)

    attractors = compute_attractors(primes, update='asynchronous', fname_json=im_dir + "attractors_repr.json")
    state = attractors["attractors"][0]["state"]["str"]

    weak = weak_basin(primes, "asynchronous", state)
    for key, value in weak.items():
        print(f"{key} = {value}")

    igraph2image(igraph, im_dir + "interaction_graph.pdf")

    create_stg_image(primes, update="asynchronous", fname_image=im_dir + "state_trans_graph.pdf")
    markers = ["WOX", "MGP"]

    phenos = compute_phenotypes(attractors, markers)

    compute_phenotype_diagram(phenos, fname_image=im_dir + "phenotype_diagram.pdf")


# Load the prostate cancer network
def prostate_cancer():
    # Read the text file and convert it to a primes dictionary
    # prost_cancer_primes = bnet2primes("./data/Montagud2021_Prostate_Cancer.bnet")

    primes = {}
    with open("data/Montagud2021_Prostate_Cancer_primes.json") as f:
        primes = json.load(f)

    #igraph = primes2igraph(primes)

    #attractors = compute_attractors(primes, update='asynchronous', fname_json=im_dir + "cancer_attr.json")

    create_attractor_report(primes, "cancer_attr_report.txt")

prostate_cancer()
