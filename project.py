import pandas as pd #mathematical functions for arrays
import numpy as np
import math
read=pd.read_excel(r'C:\Users\15878\Dropbox\My PC (DESKTOP-DM1H1IH)\Documents\School\4428 project\4428_C.xlsx')
print(read)

#print(read.loc[1]['x [A]'])

e=3.39373**-22
s=2.91225**-10
potentialE=0
N=1372



def calc(r):
    return 4*e*((s/(r**-10))**12)-((s/(r**-10))**6)


for index, row in read.iterrows():
    read['euc_dist'] = (row['x [A]'] - read['x [A]']) ** 2 + (row['y [A]'] - read['y [A]'])** 2 + (row['z [A]'] - read['z [A]']) ** 2
    
    read['euc_dist'] = np.sqrt(read['euc_dist'])
    proximity = read.loc[(read['euc_dist'] > 0) & (read['euc_dist'] <= 10)].copy(deep=True)
    proximity['calc'] = (4*e*((s/(proximity['euc_dist']**-10))**12)-((s/(proximity['euc_dist']**-10))**6))
    potentialE += sum(proximity['calc'])


# for i in range(1372):
#     for j in range(1372):
#         r=math.sqrt((read.loc[i]['x [A]']-(read.loc[j]['x [A]']))**2+((read.loc[i]['y [A]']-(read.loc[j]['y [A]']))**2)+((read.loc[i]['z [A]']-(read.loc[j]['z [A]']))**2))
#         if (r>0 and r<=10):
#             sum=float(sum)+(4*e*((s/(r**-10))**12)-((s/(r**-10))**6))
            
print("SUM:" + str(potentialE))
