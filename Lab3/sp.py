from topo import Topo
import numpy as np

start = 0

myTopo = Topo('input.txt')

N = np.zeros((myTopo.numNodes, 1))
D = np.zeros((myTopo.numNodes, 1))
p = np.zeros((myTopo.numNodes, 1))

for i in range(myTopo.numNodes):
    D[i] = np.inf
    p[i] = np.inf
    N[i] = np.inf

N[0] = start
D[start] = 0
p[start] = start

# TODO: your codes here
dist = {node:{'D':np.inf,'P':-1} for node in range(myTopo.numNodes)}
dist[start]['D'] = 0
node_now = start
start += 1
while start != myTopo.numNodes:
    for node_next in range(myTopo.numNodes):
        if myTopo.links[node_now][node_next] != 0:
            if node_next not in N:
                dist_from_now = dist[node_now]['D'] + myTopo.links[node_now][node_next]
                if dist_from_now < dist[node_next]['D']:
                    dist[node_next]['D'] = dist_from_now
                    dist[node_next]['P'] = node_now
    tmp = np.inf
    for i in range(myTopo.numNodes):
        if i not in N:
            if dist[i]['D'] < tmp:
                tmp = dist[i]['D']
                node_now = i
                N[start] = node_now
                D[node_now] = tmp
                p[node_now] = dist[node_now]['P']
    start += 1
for i in range(1, myTopo.numNodes):
    print(int(p[i]), ' --> ', i, ' cost = ', int(D[i]))


