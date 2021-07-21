# HYJ
# TIME: 2021-7-16 10:34

import numpy as np


class Model():
    def __init__(self,
                 LEARNING_RATE = 0.0001,
                 epoch = 300,
                 N = 64,
                 D_in = 100,
                 H = 1000,
                 D_out = 10,
                 data_x = None,
                 data_y = None
    ):
        self.LEARNING_RATE = LEARNING_RATE
        self.epoch = epoch
        self.N = N
        self.D_in = D_in
        self.H = H
        self.D_out = D_out
        if data_x != None:
            self.x = data_x
        else:
            self.generate_x()
        if data_y != None:
            self.y = data_y
        else:
            self.generate_y()
        self.w1 = np.random.randn(D_in, H)
        self.w2 = np.random.randn(H, D_out)

    def train(self):
        for i in range(self.epoch):
            # forward
            h = self.x.dot(self.w1)
            h_relu = np.maximum(h, 0)
            y_pred = h_relu.dot(self.w2)

            # loss
            # MSE
            loss = np.square(y_pred - self.y).sum()
            if i % 10 == 0:
                print('epoch:', i, 'loss:', loss)
                if loss < 1000:
                    self.LEARNING_RATE = self.LEARNING_RATE * 0.1

            # backward
            # d(loss)/d(w1)
            # d(loss)/d(w2)

            grad_y_pred = 2.0 * (y_pred - self.y)
            grad_w2 = h_relu.T.dot(grad_y_pred)

            grad_h_relu = grad_y_pred.dot(self.w2.T)
            grad_h = grad_h_relu.copy()
            grad_h[h < 0] = 0
            grad_w1 = self.x.T.dot(grad_h)

            # 更新
            self.w1 = self.w1 - grad_w1 * LEARNING_RATE
            self.w2 = self.w2 - grad_w2 * LEARNING_RATE
        print('final loss: {}'.format(loss))

    def generate_x(self):
        self.x = np.random.randn(self.N, self.D_in)

    def generate_y(self):
        self.y = np.random.randn(self.N, self.D_out)


# 超参数 D_in特征数
N, D_in, H, D_out = 64, 100, 1000, 10
LEARNING_RATE = 0.000001
epoch = 300

model = Model(LEARNING_RATE=LEARNING_RATE, epoch=epoch, N=N, D_in=D_in, H=H, D_out=D_out)
model.train()


