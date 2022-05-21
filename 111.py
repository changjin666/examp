import chardet
import gzip

#file = gzip.open('E:\pythonProject\代码实用片段/icc2_chipfinish.log.gz','rb')
file = open('E:\pythonProject\代码实用片段/lvyou.txt','r',encoding='utf-8')
for line in file:
    if "376" in line:
        print(line.strip())