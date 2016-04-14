'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
import networkx
import matplotlib


if __name__ == '__main__':
    #arquivoPath = '/grafos/teste.txt'
    arquivoPath = '/grafos/nowell/gr-qc.txt'
    
    graph = networkx.MultiGraph()
        
    arquivo = open(arquivoPath, 'r')
    id_edge = 0
    for line in arquivo:
        id_edge = id_edge + 1
        cols = line.strip().split('\t')
        myAresta = { 'id_edge': int(id_edge),  'time' : int(cols[0])}
        autores = cols[1].split('&')
        if len(autores) == 1:
            graph.add_edge(autores[0].strip(), autores[0].strip(),attr_dict=myAresta)
            
        for autor in autores:
            outrosAutores =  set(n for n in autores if n > autor)
            if (len(outrosAutores) == 0):
                graph.add_edge(autor.strip(), autor.strip(),attr_dict=myAresta)
                
            for outro in outrosAutores:
                #print autor, outro
                graph.add_edge(autor.strip(), outro.strip(),attr_dict=myAresta)
                
    #networkx.write_graphml(graph, '/grafos/teste-graph.txt') 
    networkx.write_graphml(graph, '/grafos/gr-qc-graph.txt') 
    
    
    #matplotlib.pyplot.show()
        
    
            
   
    
