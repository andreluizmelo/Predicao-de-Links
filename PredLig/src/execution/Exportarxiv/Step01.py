'''
Created on Aug 22, 2015

@author: cptullio

First Step is the generation of the graph from the database informations.
We will need the file of parameter to indicate the place where the graph will be saved

'''
from parametering.ParameterUtil import ParameterUtil

from formating.arxiv.Formating import Formating

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/pankaj_condmat_2004_2012/config/configuration.txt')
    astroPh = Formating(util.graph_file)
    astroPh.subject = 'cond-mat'
    astroPh.yearstoRescue = [2004,2005,2006,2007,2008,2009, 2010, 2011, 2012]
    astroPh.readingOrginalDataset()
    #astroPh.generating_graph()
    astroPh.saveGraph()