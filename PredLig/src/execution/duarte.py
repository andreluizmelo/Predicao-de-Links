'''
Created on Aug 2, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil

from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
#from calculating.CalculateMultiProcessing import CalculateMultiProcessing
from analysing.Analyse import Analyse
from datetime import datetime
from calculating.Calculate import Calculate

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/duarte/config_muna.txt')
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    #myparams.generating_Training_Graph()
    #selection = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    calc = Calculate(myparams, util.nodes_notlinked_file, util.calculated_file, util.ordered_file, util.maxmincalculated_file)
    #calc.Separating_calculateFile()
    calc.Ordering_separating_File()
    myparams.generating_Test_Graph()
    for OrderingFilePath in calc.getfilePathOrdered_separeted():
        analise = Analyse(myparams, OrderingFilePath, OrderingFilePath + '.analised.txt' )