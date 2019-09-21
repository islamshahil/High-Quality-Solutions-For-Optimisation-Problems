import sys


class AlgoNarrator(object):

    def __init__(self, algo):

    	if (algo == 'tsp'):
    		import Travel_Sales_Person

    	elif (algo == 'mga'):
    		import Microbial_Genetic_Algorithm

    	elif (algo == 'mp'):
    		import Match_Phrase

    	elif (algo == 'demo'):
    		import neural_application



if __name__ == '__main__':

	script, algo  = sys.argv

	expander = AlgoNarrator(algo)