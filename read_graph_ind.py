import numpy as np

f = open('graph_ind.txt', 'r')
nn = []  # node_number
gn = []  # graph_number
imsi = []  # 각 그래프 넘버에 들어가는 노드들

line = f.readline()
item = line.split(" ")
imsi.append(item[0].rstrip(','))
gn = item[1].rstrip('\n')

while True:
    line = f.readline()
    if not line:
        nn.append(imsi)
        break
    item = line.split(" ")
    gn2 = item[1].rstrip('\n')
    if gn != gn2:
        nn.append(imsi)
        imsi = []
    imsi.append(item[0].rstrip(','))
    gn = gn2

