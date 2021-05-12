import numpy as np

f = open('graph_ind.txt', 'r')
nn = [[]]  # nn[i][:]=graph i에 속하는 node 들의 index
n2g = np.zeros(372475, int)  # n2g[i]=node_number i가 어떤 그래프에 속하는가
i = 1
gn = []  # graph_number
imsi = []  # 각 그래프 넘버에 들어가는

line = f.readline()
item = line.split(" ")
imsi.append(int(item[0].rstrip(',')))
gn = int(item[1].rstrip('\n'))
n2g[int(item[0].rstrip(','))] = gn


while True:
    line = f.readline()
    if not line:
        nn.append(imsi)
        break
    item = line.split(" ")
    gn2 = int(item[1].rstrip('\n'))
    if gn != gn2:
        nn.append(imsi)
        imsi = []
    imsi.append(int(item[0].rstrip(',')))
    gn = gn2
    n2g[int(item[0].rstrip(','))] = gn

# 가장 node를 많이 가지고 있는 graph의 node 개수는?
"""
nnn = np.zeros(5001, int)
for i in range(1, 5001):
    nnn[i] = len(nn[i])
print(max(nnn))

# 결과는 492
"""


# Are all edges paired?
"""
f = open('graph.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    item = line.split(" ")
    fn1 = int(item[0].rstrip(','))  # first node
    sn1 = int(item[1].rstrip('\n'))  # second node
    line = f.readline()
    if not line:
        break
    item = line.split(" ")
    fn2 = int(item[0].rstrip(','))
    sn2 = int(item[1].rstrip('\n'))
    if (fn1 != sn2) or (fn2 != sn1):
        print('not paired')
        print(fn1, sn1)
        print(fn2, sn2)
print('end')

# 결과는 'not paired' 가 프린트 되지 않았고, 전부 paired 임을 알 수 있었다.
"""

# Are all graphs distinct?
"""
f = open('graph.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    item = line.split(" ")
    fn = int(item[0].rstrip(','))  # first node
    sn = int(item[1].rstrip('\n'))  # second node
    if n2g[fn] != n2g[sn]:
        print('monaigun')
print('end')

# 결과는 'monaigun' 가 프린트 되지 않았고, 각 그래프들 간에는 연결관계가 없음을 알 수 있다.
"""

# Let's make matrix

f = open('graph.txt', 'r')
i = 1
AM = np.zeros((5001, 492, 492), int)
ln = 1
while True:
    line = f.readline()
    if not line:
        break
    item = line.split(" ")
    fn1 = int(item[0].rstrip(','))  # first node
    sn1 = int(item[1].rstrip('\n'))  # second node
    if n2g[fn1] != i:
        i = i+1
        ln = int(nn[i][0])  # graph i 의 노드 넘버중 가장 작은 것
    else:
        AM[i][fn1-ln][sn1-ln] = AM[i][fn1-ln][sn1-ln]+1

np.save('AM.npy', AM)


# 이렇게 주어진 AM은 모든 graph index 에 대해서 492*492의 행렬로 주어진다.
# 이보다 작은 크기의 node를 가진 graph의 경우 남은 항들이 0으로 채워진다. 이를 없애려면 아래와 같은 방식이 가능하다.
# AM 으로부터 j번째 graph의 0처리를 하지 않은 진짜 AML을 뽑아 올때마다 아래 코드를 실행하면 된다.
"""
nnn = np.zeros(5001, int)     #graph별 노드 개수에 관한 함수
for i in range(1, 5001):
    nnn[i] = len(nn[i])
    
j=15      # 가져오고 싶은 graph 의 번호
AML = AM[j][0:nnn[j], 0:nnn[j]]
"""
