import random
rnum=random.randint(1,100)
flag=True
while(flag):
    _input=int(input("請猜一個1~99的整數:"))
    if(_input>rnum):
        print("比",_input,"小")
    elif(_input<rnum):
        print("比",_input,"大")
    elif(_input==rnum):
        print("猜對了!")
        flag=0