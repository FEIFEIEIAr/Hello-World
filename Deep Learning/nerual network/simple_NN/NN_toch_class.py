# HYJ
# TIME: 2021-7-16 9:38
import torch
import torch.nn
# 超参数 D_in特征数
N, D_in, H, D_out= 128, 100, 1000, 1
LEARNING_RATE = 0.001
epoch = 300

# 输入数据和标签
x = torch.rand(N, D_in)
y = torch.rand(N, D_out)

# 模型参数
w1 = torch.rand(D_in, H, requires_grad=True)
w2 = torch.rand(H, D_out, requires_grad=True)


# model
class MyNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        # define the model architecture
        super(MyNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H, bias=False)
        self.linear2 = torch.nn.Linear(H, D_out, bias=False)
        self.activation = torch.nn.Sigmoid()

    def forward(self, x):
        y_pred = self.linear2(self.activation(self.linear1(x)))
        return y_pred


model = MyNet(D_in, H, D_out)
loss_fn = torch.nn.MSELoss(reduction='sum')  # sum or mean
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

for it in range(epoch):
    # forward
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    loss.backward()
    if it % 10 == 0:
        print('Epoch:', it, 'Los:', loss)
    """with torch.no_grad():
        for para in model.parameters():
            para -= para.grad * LEARNING_RATE"""
    optimizer.step()
    # 清零
    model.zero_grad()
