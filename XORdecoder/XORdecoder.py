#coding: utf-8
#tests
import numpy as np

X = np.array([0x00])
keyword = ""

def XORE(file):
    s = 0
    #out = []
    count = 0
    file.seek(0)
    while True:
        data = file.read(1)
        if data == b'':
            break;
        b = int.from_bytes(data,"big")^X[0]
        print(hex(b))
        if(hex(b) == hex(ord(keyword[count]))):
            count += 1
        else:
            count = 0
        #out.append(hex(b))
        s+=1
        file.seek(s)
        if count == len(keyword):
            return 0
    return 1

if __name__ == "__main__":
    path = input("入力ファイル:")
    keyword = input("キーワードを入力:")

    file = open(path,"rb")
    outf = open(path+".x","wb")
    while True:
        print(hex(X[0]))
        out = XORE(file)
        if out != 0:
            if X[0] == 0xFF:
                print("fack")
                break;
            X[0] += 1
        else:
            print("thank")
            break
