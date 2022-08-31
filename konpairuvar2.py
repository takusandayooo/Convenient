#c言語を個別にコンパイルしていく。（入力することができる)
import os
import glob
c=__file__
c=c.replace('/konpairuvar2.py','')#このコードの名前を書く
files = glob.glob(c+"/*.c")
name=os.path.splitext(c+"/*.c")
for file in files:
    b=file.replace('.c','')
    a='gcc '+file
    a=str(a)
    os.system(a)
    print(file,'をコンパイルしました\n')

    