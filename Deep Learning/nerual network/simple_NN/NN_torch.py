# HYJ
# TIME: 2021-7-16 9:27
import torch
# 超参数 D_in特征数
N, D_in, H, D_out= 128, 100, 1000, 1
LEARNING_RATE = 0.0001
epoch = 300

# 输入数据和标签
x = torch.rand(N, D_in)
y = torch.rand(N, D_out)

# 定义模型
w1 = torch.rand(D_in, H, requires_grad=True)
w2 = torch.rand(H, D_out, requires_grad=True)

import torch.nn as nn

model = nn.Sequential(
    nn.Linear(D_in, H, bias=False),
    nn.ReLU(),
    nn.Linear(H, D_out, bias=False)
)

loss_fn = nn.MSELoss(reduction='sum')  # sum or mean
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

for it in range(epoch):
    # forward
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    loss.backward()
    print('Epoch:', epoch, 'Los:', loss)
    """with torch.no_grad():
        for para in model.parameters():
            para -= para.grad * LEARNING_RATE"""
    optimizer.step()
    # 清零
    model.zero_grad()
