import numpy as np
import pandas as pd

def getFishDataTrain():
    dl = pd.read_csv("bream_length.csv", header=None)
    dw = pd.read_csv("bream_weight.csv", header=None)
    sl = pd.read_csv("smelt_length.csv", header=None)
    sw = pd.read_csv("smelt_weight.csv", header=None)

    dl1 = pd.DataFrame(dl);
    bream_length = dl1.to_numpy()

    dw1 = pd.DataFrame(dw);
    bream_weight = dw1.to_numpy()

    sl1 = pd.DataFrame(sl);
    smelt_length = sl1.to_numpy()

    sw1 = pd.DataFrame(sw);
    smelt_weight = sw1.to_numpy()

    bream_length = np.array(bream_length)
    bream_weight = np.array(bream_weight)

    smelt_length = np.array(smelt_length)
    smelt_weight = np.array(smelt_weight)

    bream_length = bream_length.flatten().tolist()
    bream_weight = bream_weight.flatten().tolist()

    smelt_length = smelt_length.flatten().tolist()
    smelt_weight = smelt_weight.flatten().tolist()

    fish_length = np.array(bream_length + smelt_length)
    fish_weight = np.array(bream_weight + smelt_weight)
    fish_target = np.concatenate((np.ones(35), np.zeros(14)))

    index = np.arange(49)
    np.random.shuffle(index)

    train_target = fish_target[index[:35]]
    train_length = fish_length[index[:35]]
    train_weight = fish_weight[index[:35]]

    train = np.column_stack((train_target, train_length, train_weight))

    train_dataFrame = pd.DataFrame(train, columns=["train_target", "train_length", "train_weight"])

    return train_dataFrame