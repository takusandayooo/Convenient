import os
import glob
c=__file__
c=c.replace('/konpairu.py','')
files = glob.glob(c+"/*.c")
name=os.path.splitext(c+"/*.c")
for file in files:
    b=file.replace('.c','')
    a='gcc -o '+b+' '+file
    a=str(a)
    os.system(a)
    print(file,'をコンパイルしました。\n')
