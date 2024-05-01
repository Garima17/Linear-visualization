#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:44:50 2024

@author: garimajindal
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Thu Feb  3 12:39:26 2022

#@author: garima
#"""

import networkx as nx
import os
import community
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import json
import treelib as tree
from collections import deque
import datetime

def heatmap_data_generator(partition, link_df_sym):
    source = list(set(partition.values()))
    target = list(set(partition.values()))
    combined =[source, target]
    community_combinations = pd.DataFrame(columns = ['source', 'target'], data=list(itertools.product(*combined)))
    community_combinations = community_combinations.merge(link_df_sym, how='left').fillna(0)
    return community_combinations

def heighest_degree(new_data, partition):
    no_of_communities =  len(set(partition.values()))
    #initialize lists
    community = []
    heigest_degree = []
    #get index_of_hdegree
    index_of_hdegree =0
    #update index of data_frame
    newdata= new_data.reset_index(drop=True)
    for i in range(0,  no_of_communities):
        community.append(i)
        heigest_degree.append(newdata._get_value(index_of_hdegree, 'centrality'))
        #print(new_data._get_value(sum_size, 'node'))
        size_of_each_community =len([k for k,v in partition.items() if v == i])
        #print(size_of_each_community)
        index_of_hdegree =index_of_hdegree + size_of_each_community
    dict = {'community': community, 'h_degree': heigest_degree} 
    df = pd.DataFrame(dict)
    return df
        
        

def density_of_subgraph(G_sub):
    n = len(G_sub.nodes())
    max_edges= n*(n-1)/2
    edges_present = len(G_sub.edges())
    density = edges_present / max_edges
    return density


def ordering_nodes(df):
    df = df.sort_values(by=["community", "centrality"], ascending=[True,True])
    return df

def nodes_in_communities(partition):
    unique_communitites= list(set(partition.values()))
    number_of_nodes=[]
    for community in unique_communitites:
        count = sum(x==community for x in partition.values())
        number_of_nodes.append(count)
    dict = {'community': unique_communitites, 'count': number_of_nodes} 
    df = pd.DataFrame(dict)
    return df

def density_in_communities(partition):
    unique_communitites= list(set(partition.values()))
    density=[]
    for community in unique_communitites:
        subgraph = G.subgraph([k for k,v in partition.items() if v == community])
        d= density_of_subgraph(subgraph)
        density.append(d)
    dict = {'community': unique_communitites, 'density': density} 
    df = pd.DataFrame(dict)
    return df
    
        
        
    
    
def data_transformation(G, partition):
    node= list(partition.keys())
    centrality =[]
    community = list(partition.values())
    density_comm= []
   
    

    for i in range(0, len(node)):
        centrality.append(G.degree(node[i]))
        
    dict = {'node': node, 'centrality': centrality, 'community':community} 
 
    df = pd.DataFrame(dict)
    
    df = ordering_nodes(df)
        
    no_of_communities =  len(set(partition.values()))
        
    #populate id, centrality and community list
    for i in range(0,  no_of_communities):
        size_of_each_community =len([k for k,v in partition.items() if v == i])
        print(size_of_each_community)

        subgraph = G.subgraph([k for k,v in partition.items() if v == i])
        d= density_of_subgraph(subgraph)
        
        density_list = [d] * size_of_each_community
        #print(density_list)
        density_comm.extend(density_list)
    #print (density_comm)
    #print (len(density_comm))
    
    df['density'] = density_comm
        
    #dict = {'node': node, 'centrality': centrality, 'community':community, 'density':density_comm} 

    
    return df


def get_labels(G):
    label_dict = {}
    for u,v,a in G.edges(data=True):  
        label_dict[u]= u
    return label_dict


#positions of coarse graph 
def coarse_graph_node_positions_to_df(pos):
    node=[]
    x_pos=[]
    y_pos=[]

    for i in  range(0, len(pos)):
        node.append(i)
        x_pos.append(pos[i][0])
        y_pos.append(pos[i][1])
    dict = {'node': node, 'x_pos': x_pos, 'y_pos':y_pos} 
    df = pd.DataFrame(dict)
    return df


#visualize coarse graph()
def visualize(G, label_dict, pos):   
    nx.draw(G, pos, labels=label_dict)
    plt.show()
    
def link_data_community(induced_coarse_graph):
    source=[]
    target=[]
    weight=[]
    #printing weights of edges 
    for u,v,a in induced_coarse_graph.edges(data=True):
        if (u!=v):
            source.append(u)
            target.append(v)
            weight.append( a['WEIGHT'])
            print (u,v,a)
    
    dict = {'source': source, 'target': target, 'weight':weight} 
    df = pd.DataFrame(dict)
    return df

def link_data(graph):
    source=[]
    target=[]
    #printing weights of edges 
    for u,v,a in graph.edges(data=True):
        if (u!=v):
            source.append(u)
            target.append(v)            
    
    dict = {'source': source, 'target': target} 
    df = pd.DataFrame(dict)
    return df

def link_data_symmetry(induced_coarse_graph):
    source=[]
    target=[]
    weight=[]
    #printing weights of edges 
    for u,v,a in induced_coarse_graph.edges(data=True):
        if (u!=v):
            source.append(u)
            target.append(v)
            weight.append( a['WEIGHT'])
            source.append(v)
            target.append(u)
            weight.append( a['WEIGHT'])
    
    dict = {'source': source, 'target': target, 'weight':weight} 
    df = pd.DataFrame(dict)
    return df

def adding_centrality_measures_to_data(new_data):
    betw= nx.betweenness_centrality(G)
    clo= nx.closeness_centrality(G)
    eig = nx.eigenvector_centrality(G)
    
    betw_df = pd.DataFrame(list(betw.items()))
    clo_df = pd.DataFrame(list(clo.items()))
    eig_df = pd.DataFrame(list(eig.items()))
    
    betw_df.columns = ['node', 'betwness']
    clo_df.columns = ['node', 'closeness']
    eig_df.columns = ['node', 'eign']
    
    new_data = pd.merge(betw_df, new_data, on='node')
    new_data = pd.merge(clo_df, new_data, on='node')
    new_data = pd.merge(eig_df, new_data, on='node')
    
    new_data = ordering_nodes(new_data)
    
    #sorting the data and node index based on node id
    #new_data["node"] = pd.to_numeric(new_data["node"])
    #new_data= new_data.sort_values(by = 'node')
    #new_data = new_data.reset_index(drop=True)
    
    
    return new_data
    
  
def create_dictionary_of_connections(G):
    connections = {}
    for node in list(G.nodes()):
        neighbour_list =[]
        for neighbour in G.neighbors(node):
            neighbour_list.append(int(neighbour))
        connections[int(node)] = neighbour_list
    return connections


    

def findOutlierRangeForInputCemtrality(centrality):
    range_list=[]
    
    sorted(centrality)

    quartile1 = centrality.quantile(.25)
    quartile3 = centrality.quantile(.75)
    IQR= quartile3 - quartile1

    lowerBondValue= quartile1 - (1.5* IQR)
    upperBondValue = quartile3 + (1.5* IQR)
    
    if lowerBondValue <= min(centrality):
        range_list.append(min(centrality))
    else: 
        range_list.append(lowerBondValue)
        
    if upperBondValue >= max(centrality):
        range_list.append(max(centrality))
    else: 
        range_list.append(upperBondValue)
        
    return range_list

def dictAfterOutlierRemovalFromDifferentCentralitities(data):
    degree_range = findOutlierRangeForInputCemtrality(data['centrality'])
    eign_range = findOutlierRangeForInputCemtrality(data['eign'])
    closeness_range = findOutlierRangeForInputCemtrality(data['closeness'])
    betwness_range = findOutlierRangeForInputCemtrality(data['betwness'])
    dict_range ={}
    dict_range['degree_range'] = degree_range
    dict_range['eign_range'] = eign_range
    dict_range['closeness_range'] = closeness_range
    dict_range['betwness_range'] = betwness_range
    return dict_range
    
    
def generate_files_for_graph(graph, this_id):
    #apply community detection algorithm
    partition = community.community_louvain.best_partition(graph)
    #coarse graph
    induced_coarse_graph = community.induced_graph(partition, graph, weight='WEIGHT')
    #inset here
    #positions of spring layout
    pos = nx.spring_layout(induced_coarse_graph, k=10,weight='WEIGHT') 
    #labes of nodes
    label_dict = get_labels(induced_coarse_graph) 
    #result = label_dict.to_json(orient="records")  
    #visualize coarse_graph 
    #bhanu visualize(induced_coarse_graph,label_dict, pos)   

    connection_dict = create_dictionary_of_connections(graph)
    with open(str(this_id) + "_connection_list.json", "w") as outfile:
        json.dump(connection_dict, outfile)

    #second
    #converting link data to a dataframe
    link_df=link_data_community(induced_coarse_graph)
    link_df_sym=link_data_symmetry(induced_coarse_graph)
    link_df.to_csv(str(this_id) +'_link_data.csv')
    #find node to node link data
    node_to_node_link_df=link_data(graph)
    node_to_node_link_df.to_csv(str(this_id) + '_node_to_node_link_data.csv')

    #first 
    df= coarse_graph_node_positions_to_df(pos)
    #saving caorse graph to csv file
    df.to_csv(str(this_id) +'_coarse_graph_pos.csv')
    #saving node data
    new_data = data_transformation(graph, partition)

    new_data = adding_centrality_measures_to_data(new_data)

    new_data.to_csv(str(this_id) +'_facebook_data_transformed_new.csv')

    extent_of_centralitties_after_removing_outliers = dictAfterOutlierRemovalFromDifferentCentralitities(new_data)
    #extent_of_centralitties_after_removing_outliers = pd.DataFrame(extent_of_centralitties_after_removing_outliers)
    #extent_of_centralitties_after_removing_outliers.to_csv('new_extent_without_outliers_for_colorcoding.csv')
    with open(str(this_id) +"_new_extent_without_outliers_for_colorcoding.json", "w") as outfile:
        json.dump(extent_of_centralitties_after_removing_outliers, outfile)


    number_of_nodes_in_communities = nodes_in_communities(partition)
    number_of_nodes_in_communities.to_csv(str(this_id) +'_commuity_count.csv')


    density_in_comms = density_in_communities(partition)
    density_in_comms.to_csv(str(this_id) +'_commuity_density.csv')

    h_degree_in_communities = heighest_degree(new_data, partition)
    h_degree_in_communities.to_csv(str(this_id) +'_commuity_h_degree.csv')

    heatmap_data = heatmap_data_generator(partition, link_df_sym)
    heatmap_data.to_csv(str(this_id) +'_heatmap_data.csv')
    return partition



def process_queue_node(this_id):
    print ("entered process_queue_node")
    global id
    global Q
    global G
    global T
    global M
    global Flat_tree_parent_list
    global Flat_tree_community_list
    
    graph = M.get(this_id)
    
    next_partition = generate_files_for_graph(graph, this_id)
    
    print ("partion created for " + str (this_id))

    unique_communitites= list(set(next_partition.values()))
    local_coomunity_number_fir_this_partition = []
    
    # give file number prefix fpr each local community
    parent_comm_global_ids = []
    
    for community in unique_communitites:
        print ("entered loop " + str(id))
        subgraph = G.subgraph([k for k,v in next_partition.items() if v == community])
        print ("subgraph created " + str(id))
        id+=1
        local_coomunity_number_fir_this_partition.append(community)
        
        Flat_tree_community_list.append(id)
        Flat_tree_parent_list.append(this_id)
        
        if len(subgraph.nodes()) > Sprial_size_threshold:
            print ("subgraph added in queue " + str(id))
            M[id]=subgraph
            Q.append(id)
            T.create_node(id, id, parent=this_id)
            parent_comm_global_ids.append(id)
        else:
            print ("subgraph ignored " + str(id))
            T.create_node(id, id, parent=this_id)
            parent_comm_global_ids.append(this_id)
            
            
    parent_comm_global_id_map = {'local_cmm_number': local_coomunity_number_fir_this_partition, 'comm_id': parent_comm_global_ids}
    
    pd.DataFrame(parent_comm_global_id_map).to_csv(str(this_id) +'_parent_comm_global_id_map.csv')
            

#Main function  
#read graph data
G =  nx.read_edgelist("facebook_combined.txt")

new_dir = "run_"+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.makedirs(new_dir)
os.chdir(new_dir)

Sprial_size_threshold = 500

id = 0

Flat_tree_parent_list = []
Flat_tree_community_list = []

# dendogram of communitities, where each community have more than 
# Sprial_size_threshold nodes will have childern
T = tree.Tree()
T.create_node(id, id)


# Map of community and Graph of all nodes part of that community, 
# first item is graph of all nodes.
M = dict()

# Queue for breath first traversal of community graphs
Q = deque()
Q.append(id)

M[id]=G

while Q:
    process_queue_node(Q.popleft())

print ("process queue finished")



community_parent_flat_tree = {'comm_id': Flat_tree_community_list, 'parent_comm_id': Flat_tree_parent_list}

pd.DataFrame(community_parent_flat_tree).to_csv('all_community_parent_flat_tree.csv')



print (M.items())
print (Q)
print (T.__str__())


    
    
    
    








 

