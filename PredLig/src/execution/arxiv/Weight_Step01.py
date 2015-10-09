'''
Created on Aug 22, 2015

@author: cptullio
Analysing the results
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from calculating.VariableSelection import VariableSelection
from formating.FormatingDataSets import FormatingDataSets
import networkx
import mysql.connector
from calculating.GenerateWeights import GenerateWeigths

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/exemplomenorWeights/nowell_example_1994_1999.txt')
    myparams = Parameterization(keyword_decay= util.keyword_decay, lengthVertex = util.lengthVertex, t0 = util.t0, t0_ = util.t0_ , t1 = util.t1, t1_ = util.t1_, featuresChoice = util.FeaturesChoiced, filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, FullGraph = None, min_edges = util.min_edges, weightFeaturesChoiced = util.WeightFeaturesChoiced)
    
    myparams.generating_Training_Graph()
    AllNodes = VariableSelection(myparams.trainnigGraph, util.nodes_file,util.min_edges, True)
    
    weigths = GenerateWeigths(preparedParameter = myparams, fileAllNodes = util.nodes_file)
    
    
    