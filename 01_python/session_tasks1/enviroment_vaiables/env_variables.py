import os

x=os.environ

for key,value in x.items():
    print(f"{key} : {value}")