#!/usr/bin/python
# coding = utf-8

import os,sys,re
path = sys.path[0]

def findFunction(sourceFile:str):
    result = re.findall(r'''def ([a-zA-Z]+)\(security.*\n    """\n\t(.+)''',sourceFile)
    return result

fileDict = {}
fileList = ["wsd.py","wsee.py","wses.py","wsi.py","wsq.py","wss.py","wst.py"]
meaningList = ["时间序列","板块多维","板块序列","分钟序列","实时行情","截面字段","日内跳价"]
for fileName in fileList:
    with open(path+os.sep+"Windget"+os.sep+fileName,"r",encoding="utf-8") as f:
        content = f.read()
        functionInfo = findFunction(content)
        fileDict[fileName] = functionInfo

rstPrefix = '''函数索引\n=======================\n\n.. toctree::\n\t:maxdepth: 4\nwindget提供如下的函数，为了方便，在这里我们按照不同的函数尾缀做呈现：\n\n'''
rstDict = {}
for fileName,mean in zip(fileDict.keys(),meaningList):
    content = fileDict[fileName]
    maxLength = max([len(i[1]) for i in content])*2
    dash = "".join(['-' for i in range(maxLength)])
    equal = "".join(['=' for i in range(maxLength)])
    if fileName!='wss.py':
        rstDict[fileName] = fileName.split('.py')[0].capitalize()+mean+rstPrefix+'''以下是尾缀为'''+fileName.split('.py')[0].capitalize()+'''的函数：\n\n'''
    else:
        rstDict[fileName] = fileName.split('.py')[0].capitalize()+mean+rstPrefix+'''以下是不包含尾缀的函数：\n\n'''
    rstDict[fileName] = rstDict[fileName] + '''+'''+dash+'''+'''+dash+'''+\n'''
    rstDict[fileName] = rstDict[fileName] + '''|'''+"函数名称".ljust(maxLength-4," ")+'''|'''+"字段名称".ljust(maxLength-4," ")+'''|\n'''
    rstDict[fileName] = rstDict[fileName] + '''+'''+equal+'''+'''+equal+'''+\n'''
    for item in content:
        chineseString = re.sub(r"[a-zA-Z0-9\(\)\._/,:\-% ]","",item[1])
        chineseLength = len(chineseString)
        rstDict[fileName] = rstDict[fileName] + '''|'''+item[0].ljust(maxLength," ")+'''|'''+item[1].ljust(maxLength-chineseLength," ")+'''|\n'''
        rstDict[fileName] = rstDict[fileName] + '''+'''+dash+'''+'''+dash+'''+\n'''
    rstDict[fileName] = rstDict[fileName]+'''\n'''

for fileName in fileList:
    targetFileName = fileName.split('.py')[0]+'.rst'
    with open(path+os.sep+"source"+os.sep+targetFileName,"w",encoding="utf-8") as f:
        f.write(rstDict[fileName])

print("函数索引生成完成")











