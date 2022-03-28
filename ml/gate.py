import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

import pickle
from PIL import Image

class NNmnist:
    """mnistの計算
    分類精度を出すところまで

    """

    def __init__(self):
        path = "path/to/csv"
        with open(path, "rb") as f:
            self.network = pickle.load(f)
        
        (self.x_train, self.t_train), (self.x_test, self.t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=True)
    
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def softmax(self, a):
        c = np.max(a)
        exp_a = np.exp(a-c)
        sum_exp_a = np.sum(exp_a)

        return exp_a / sum_exp_a

    def predict(self, X):
        W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
        b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']

        a1 = np.dot(X, W1) + b1
        z1 = self.sigmoid(a1)

        a2 = np.dot(z1, W2) + b2
        z2 = self.sigmoid(a2)

        a3 = np.dot(z2, W3) + b3
        y = self.softmax(a3)

        return y

    def draw_image(self, img):
        img = img.reshape(28, 28)
        # uint8; 符号なし8ビット整数型にcast
        pil_image = Image.fromarray(np.uint8(img))
        pil_image.show()

nn = NNmnist()
batch_size = 100
acc = 0

x = nn.x_test
t = nn.t_test

# rangeのstepがbatch_sizeなので、
# x[i: i+batch_size] は x[0:99], x[100:199]. x[200:299], ...
for i in range(0, len(x), batch_size):
    x_batch = x[i: i+batch_size]
    y_batch = nn.predict(x_batch)
    # 各画像が長さ10のnp.arrayを持つ (728 x 10)
    # 10この数字の中で、最大の数のindexを返す(728 x 1)
    p = np.argmax(y_batch, axis=1)
    t_idx = np.argmax(t[i: i+batch_size], axis=1)
    # p == t[i: i+batch_size] : p と t[i: i+batch_size] が同じ要素はTrue, 違うならFalseという配列
    # そのうち、Trueの数をカウント
    acc += np.sum(p == t_idx)

print("Accuracy: ", str(float(acc / len(x))))

class NN3:
    """クラスの説明タイトル

        クラスについての説明文

    """
    def __init__(self):
        self.network = {}
        self.network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        self.network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        self.network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
        self.network['b1'] = np.array([0.1, 0.2, 0.3])
        self.network['b2'] = np.array([0.1, 0.2])
        self.network['b3'] = np.array([0.1, 0.2])

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def identity_function(self, x):
        return x

    def forward(self, X):
        """入力信号を出力に変換

        Parameters:
        X -> input(np.array: 2 dim)
    
        Returns:
        y -> output(np.array: 2 dim)

        """
        W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
        b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']


        a1 = np.dot(X, W1) + b1
        z1 = self.sigmoid(a1)

        a2 = np.dot(z1, W2) + b2
        z2 = self.sigmoid(a2)

        a3 = np.dot(z2, W3) + b3
        y = self.identity_function(a3)

        return y