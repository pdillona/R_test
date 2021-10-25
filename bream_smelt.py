import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

bream_data = np.column_stack((bream_length, bream_weight))
smelt_data = np.column_stack((smelt_length, smelt_weight))

print(bream_data)
print(smelt_data)

plt.scatter(bream_data[:,0], bream_data[:,1])
plt.scatter(smelt_data[:,0], smelt_data[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()