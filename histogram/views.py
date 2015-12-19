
from django.shortcuts import HttpResponse
from cs361_as1.settings import *



def myHistogram(request, filename):
    file = open("%s/static/templates/%s"%(BASE_DIR,filename),"r+")
    myDic={}
    s =""
    for word in file:
        word = word.strip()
        if word not in myDic:
            myDic[word]=1
        else:
            myDic[word]+=1
    for key in myDic:
        s = s+str(key)+" "+str(myDic[key])+" "
    return HttpResponse(s)

