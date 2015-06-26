'''
Created on Jun 15, 2015

@author: cptullio
'''
import unittest
 
import matplotlib.pyplot as plt
import networkx as networkx

from parametering.Parameterization import Parameterization
from featuring.AASFeature import AASFeature
from featuring.JCFeature import JCFeature
from featuring.PAFeature import PAFeature
from calculating.Result import Result
from calculating.Calculate import Calculate
from networkx.classes.graph import Graph

from featuring.FeatureBase import FeatureBase, NoLinkedNodes
from featuring.CNFeature import CNFeature
import matplotlib

class Test(unittest.TestCase):

    def creategraph(self):
        graph = Graph()
        a1 = 'author_1'
        a2 = 'author_2'
        a3 = 'author_3'
        a4 = 'author_4'
        a5 = 'author_5'
        
        p1 = 'paper_1'
        p2 = 'paper_2'
        p3 = 'paper_3'
        p4 = 'paper_4'
        
        graph.add_node(a1, {'node_type': 'N' })
        graph.add_node(a2, {'node_type': 'N' })
        graph.add_node(a3, {'node_type': 'N' })
        graph.add_node(a4, {'node_type': 'N' })
        graph.add_node(a5, {'node_type': 'N' })
        
        graph.add_node(p1, {'node_type': 'E', 'time': 1994})
        graph.add_node(p2, {'node_type': 'E', 'time': 1995})
        graph.add_node(p3, {'node_type': 'E', 'time': 1996})
        graph.add_node(p4, {'node_type': 'E', 'time': 1996})
        
        graph.add_edge(p1,a1)
        graph.add_edge(p1,a2)
        graph.add_edge(p2,a2)
        graph.add_edge(p2,a4)
        graph.add_edge(p3,a3)
        graph.add_edge(p4,a5)
        graph.add_edge(p4,a4)
        
        return graph
    
    def createbestgraph(self):
        graph = Graph()
        a1 = 'author_1'
        a2 = 'author_2'
        a3 = 'author_3'
        a4 = 'author_4'
        a5 = 'author_5'
        
        
        graph.add_edge(a1,a2, {'paper':1, 'time':1950})
        graph.add_edge(a1,a5, {'paper':2, 'time':1980})
        graph.add_edge(a5,a4, {'paper':3, 'time':1990})
        graph.add_edge(a3,a3, {'paper':5, 'time':1990})
            
        return graph
    
    def test_usingbestGraph(self):
        graph = self.createbestgraph()
        feature = CNFeature()
        feature.graph = graph
        result = set()
        for no in graph.nodes():
            vizinhos = feature.all_neighbors(no)
            vizinhos = set(graph.nodes()) - vizinhos
            vizinhos.remove(no)
            for other in vizinhos:
                isAlreadyThere = set(n for n in result if (n.first_node == no or n.first_node == other) and (n.second_node == no or n.second_node == no))
                if len(isAlreadyThere) == 0:
                        result.add(NoLinkedNodes(no, other))
        
                
        for item in result:
            print  feature.execute(feature.all_neighbors(item.first_node), feature.all_neighbors(item.second_node))
                
            
        #networkx.draw_networkx(graph)
        #plt.show()
    
    
    def test_writeGraph(self):
        graph = self.creategraph()
        networkx.write_graphml(graph, '/Users/cptullio/mygraph.gml')
    
    def test_readGraph(self):
        graph = networkx.read_graphml( '/Users/cptullio/mygraph.gml')
    
    def test_somethingnew(self): 
        graph =  graph = networkx.read_graphml( '/Users/cptullio/ai_graph.txt')
        all_Authors = set(n for n,d in graph.nodes(data=True) if d['type'] == 'N')
        all_Papers = set(n for n,d in graph.nodes(data=True) if d['type'] == 'E')
        fb = FeatureBase()
        fb.graph = graph
        print len(all_Authors)
        print len(fb.get_pair_node_not_linked(all_Authors))
        
    def testGraphCreating(self):
        graph = self.creategraph()
        
        all_Authors = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        cn= CNFeature()
        cn.graph = graph
        
        for result in cn.get_pair_node_not_linked(all_Authors):
            
            print str(result.first_node) + ";" + str(result.second_node) + ";" + str(cn.execute(cn.all_node_neighbors(result.first_node), cn.all_node_neighbors(result.second_node)))
            
        #networkx.draw_networkx(graph)
        #plt.show()
            
   
    def testCalculating(self):
        featuresBase = []
        aas = AASFeature()
        jc = JCFeature()
        pa = PAFeature()
        featuresBase.append(aas)
        featuresBase.append(jc)
        featuresBase.append(pa)
        
        myfile = '/Users/cptullio/ai_graph.txt'
        p = Parameterization(0 , 0, featuresBase , myfile)
        calculate = Calculate(p)
        
        myfileResult = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor_result.txt'
        with open(myfileResult, 'w') as fauthorarticleout:
            for r in calculate.results:
                strcalcs = ''
                for c in r.calcs:
                    strcalcs = strcalcs + str(c) +';'  
                fauthorarticleout.write(str(r.node1) + ';' + str(r.node2)+ ';'  +   str(r.current_neighbor_node1)+ ';'  +   str(r.current_neighbor_node2)+ ';'  + strcalcs + '\r\n')
       

            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()