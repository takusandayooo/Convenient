#c言語を実行ファイルにコンパイルと個別に実行することができる二つ
import os
import glob
c=__file__
c=c.replace('/konpairuvar3.py','')
files = glob.glob(c+"/*.c")
name=os.path.splitext(c+"/*.c")
for file in files:
    b=file.replace('.c','')
    a='gcc -o '+b+' '+file
    c='gcc '+file
    a=str(a)
    c=str(c)
    print(file,'をコンパイルしました。\n')
    os.system(a)
    os.system(c)
    print("出力結果")
    os.system('./a.out')
    