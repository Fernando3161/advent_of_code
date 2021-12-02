import os
from numpy import sign
import pandas as pd

df=pd.read_csv(os.path.join(
    os.getcwd(),"Day1","input.txt"),header=None, names=["data"])
data = df["data"]
# -1 = Goes higher
# +1 = goes lower
res = [0]
for x in range(1,len(data)):
    res.append(sign(data[x]-data[x-1]))
three_avg=[]
for x in range(len(data)-2):
    avg = (data[x]+data[x+1]+data[x+2])/3
    three_avg.append(avg)
res_three_avg=[0]
for x in range(1,len(three_avg)):
    res_three_avg.append(sign(three_avg[x]-three_avg[x-1]))



print(res.count(1))
print(res_three_avg.count(1))

