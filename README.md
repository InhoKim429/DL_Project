# Deep Learning Project  
## Abstract  
주어진 주제들 중 팀원 모두 가장 생소하게 다가오는 주제가 그래프 분류였다.  
그래프는 3D mesh 영상이나 분자 구조 그래프 또는 문제 단순화 등으로 다양한 학문에서 사용되고 있으므로 그 중요도가 매우 높다.  
따라서 이번 기말 프로젝트를 기회로 삼아  
1)그래프 이론에 대한 간단한 이해  
2) 그래프를 코드 상에서 다루는 방법에 대한 이해  
3) 그래프 데이터들을 가공하여 뉴럴 네트워크에 적용하는 방법에 대한 탐구를 진행할 예정이다.  
## Method  
그래프를 인접 행렬로 변환하여 이미지처럼 고정된 사이즈의 데이터로 변환한 다음,  
뉴럴 네트워크에 적용하여 분류하는 것을 기본적인 계획으로 삼아,  
1)그래프 분류에 대한 다양한 논문을 읽어 인접 행렬 변환 이외의 다른 embedding 방법이 있는지 조사  
2) 그래프 분류를 위한 네트워크 구조 및 기타 테크닉에는 어떤 것이 가장 적합할지 조사한 뒤 적용하여 
분류 정확도를 높인다.  
# Usage
```
dataset = GraphList("./data/AM.npy", "./data/train.txt", "./data/test.txt")
train_list, valid_list, test_list = dataset.make_dataset()

batch_size = 8
train_dataset = GraphDataset(train_list, batch_size)
valid_dataset = GraphDataset(valid_list, batch_size)
test_dataset  = GraphDataset(test_list, batch_size)

train_loader  = DataLoader(train_dataset, batch_size = batch_size, shuffle = True, drop_last = True)
valid_loader  = DataLoader(valid_dataset, batch_size = batch_size, shuffle = False, drop_last = True)
test_loader   = DataLoader(test_dataset, batch_size = batch_size, shuffle = False, drop_last = True)
```
# Will...  
```
1. 모델 정의 (나이브한 접근은 인접 행렬에 MLP를 취하는 방법)  
2. 학습 루프는 notebook_example.ipynb 참고  

Pusedo Code

define Net
define optimizer
define loss

model     = Net()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
criterion = nn.CrossEntropyLoss()

for epoch in 100:

    set_train()
    for graph, label in train_dataloader:
        predict = model(graph)
        loss    = criterion(predict, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    set_valid()
    for graph, label in valid_dataloader:
        with torch.no_grad():
            predict = model(graph)
            loss    = criterion(predict, label)
    
    print("train data에 대한 로스 및 정확도")
    print("valid data에 대한 로스 및 정확도")
```