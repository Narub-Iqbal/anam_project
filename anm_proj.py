import numpy as np
import pandas as pd
numb=[]
char=[]
file=open('anam.txt','r')
lines=file.readlines()
print(lines)
for line in (lines):
    for c in line:
        if c.isdigit()==True:
            num=c
            numb.append(num)
    for d in line:
        if d.isalpha()==True:
            cha=d
            char.append(cha)
str1=" "
msg=str1.join(char)
print("message from the file is: ",msg)
sorted_char=np.sort(char)
sorted_numb=np.sort(numb)
print(sorted_char)
print(sorted_numb)
df=pd.DataFrame({"Sorted Characters":sorted_char,"Sorted Numbers":sorted_numb})
print(df)
df.to_csv("sorted_dt.csv",index=False)