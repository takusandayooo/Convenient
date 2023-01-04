#ファイルをRAWという名前にする。
import os
import glob
c=__file__
c=c.replace('/te.py','')
files = glob.glob(c+"/*.JPG")
ARWfile=c+"/RAW/"
#print(ARWfile)
#print(files)
files=sorted(files)
for file in files:
    b=file.replace('.JPG','.ARW')
    ARWs=b.replace(c+"/","")
    a='cp '+ARWfile+ARWs+" "+b
    print(a)
    a=str(a)
    os.system(a)
