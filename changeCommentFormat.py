#!/usr/bin/python
# coding = utf-8

import os,sys,re
path = sys.path[0]

def replaceComment(originalComment:str,targetComment):
    result = re.sub(r"# (获取.*)",targetComment,originalComment)
    return result

fileDict = {}
fileList = ["wsd.py","wsee.py","wses.py","wsi.py","wsq.py","wss.py","wst.py"]
replaceFunction = [
    lambda x:'''"""\n\t'''+x.group(1)+'''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\tstartDate : str\n\t\tThe start date of time series.\n\tendDate : str\n\t\tThe end date of timeseries.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""''',
    lambda x: '''"""\n\t''' + x.group(1) + '''\n\n\tParameters\n\t----------\n\tsecurity : list\n\t\tThe list whose elements are security code.\n\n\tReturns\n\t-------\n\tpd.DataFrame\n\t"""'''
]
for fileName,targetComment in zip(fileList,replaceFunction):
    with open(path+os.sep+"windget"+os.sep+fileName,"r",encoding="utf-8") as f:
        content = f.read()
        afterReplaced = replaceComment(content,targetComment)
        fileDict[fileName] = afterReplaced
for fileName in fileDict:
    with open(path+os.sep+"windget"+os.sep+fileName,"w",encoding="utf-8") as f:
        f.write(fileDict[fileName])
print("注释替换完成")











