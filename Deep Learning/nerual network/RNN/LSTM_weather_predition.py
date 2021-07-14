import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib as mpl


# 归一化处理
def normalize(dataset):
    data_mean = dataset.mean(axis=0)
    data_std = dataset.std(axis=0)

    return (dataset-data_mean)/data_std
# 获取data和label，
def generate_data_and_labels(dataset, x_length = 20, y_length = 1):
    data = []
    labels = []

    # 计算最后一个能取到的下标
    end_index = len(dataset) - x_length - y_length + 1

    for i in range(0, end_index):
        # 从i开始拿x_length条记录，作为其中一个data
        data.append(np.expand_dims(dataset[i: i+x_length], -1))
        # 拿第i + x_length条数据，就是data之后的一条数据作为label
        labels.append(dataset[i + x_length])
    return np.array(data), np.array(labels)


mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# 从origin下载压缩包，命名为fname，自动解压，最后返回zip的下载路径
zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)
# 得到csv的路径
csv_path, _ = os.path.splitext(zip_path)
df = pd.read_csv(csv_path)
df.head()

# 读取温度那一列的数据
uni_data = df['T (degC)']
# 时间为行的名称，去时间的前5个字符，只拿到月份和日期信息
uni_data.index = [date[:5] for date in df['Date Time']]

# 画图
plt.title('Show temperature in one year')
plt.xlabel('Date(day.month)')
plt.ylabel('Temperature(degC)')
# 一小时有6个记录点，这里代表一年的记录
uni_data[:6*24*365].plot()

# 归一化处理
uni_data = normalize(uni_data.values)

# 数据集样本数（我们只训练一年即可）
DATASET_COUNT = 6*24*365
# 数据集中测试集合的占比
TEST_SIZE = 0.2
# 数据集中训练样本数
TRAIN_DATASET_COUNT = DATASET_COUNT * (1 - TEST_SIZE)

data, labels = generate_data_and_labels(uni_data[:DATASET_COUNT], 20, 1)
# 使用train_test_split函数把数据集分成训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=TEST_SIZE)
print("x train shape: {}, y train shape: {} x test shape: {} y test shape: {}".format(x_train.shape, y_train.shape, x_test.shape, y_test.shape))


def show_plot(plot_data, title):
    labels = ['History', 'True Future', 'Model Prediction']
    marker = ['.-', 'rx', 'go']
    
    for i, x in enumerate(plot_data):
        if i:
            future = 0
            plt.plot(future, plot_data[i], marker[i], markersize=10,
                     label=labels[i])
        else:
            history = list(range(-len(x), 0))
            plt.plot(history, plot_data[i].flatten(), marker[i], label=labels[i])
    plt.legend()
    plt.title(title)
    plt.xlabel('Time-Step')
    return plt
show_plot([x_train[0], y_train[0]], 'Sample Example')

BATCH_SIZE = 256
BUFFER_SIZE = 10000

# shuffle打乱数据，制作成batch_size大小的批数据
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
val_dataset = val_dataset.batch(BATCH_SIZE).repeat()

# model
simple_lstm_model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(8, input_shape=x_train.shape[-2:]), # input_shape=(20,1) 不包含批处理维度
    tf.keras.layers.Dense(1) 
])

simple_lstm_model.compile(optimizer='adam', loss='mae')
simple_lstm_model.summary()

EPOCHS = 10

simple_lstm_model.fit(train_dataset, epochs=EPOCHS,
                      steps_per_epoch= TRAIN_DATASET_COUNT / BATCH_SIZE,
                      validation_data=val_dataset, validation_steps=50)

for x, y in val_dataset.take(3):
    plot = show_plot([x[0].numpy(), y[0].numpy(),
                    simple_lstm_model.predict(x)[0]], 'Simple LSTM model')
    plot.show()
