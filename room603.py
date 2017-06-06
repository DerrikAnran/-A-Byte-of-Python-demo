#!/usr/bin/python
#Filename:room603.py
import cPickle as p
class person:
    '''define class person'''
    def getname(self):
        return self.name
    def setname(self,name):
        self.name = name
    def getad(self):
        return self.address
    def setad(self,address):
        self.address = address
dic = {}
def addp(cname,name,address):
    cname = person()
    cname.setname(name)
    cname.setad(address)
    dic[name] = cname
def delp(name):
    del dic[name]
def write():
    f = file("dic.data",'w')
    p.dump(dic,f)
    f.close()
def read():
    f = file("dic.data")
    dic = p.load(f)
def search(name):
    '''search person'''
    read()
    p = person()
    if name in dic:
        p = dic[name]
        print "%s's address is %s"%(name,p.getad())
    else:
        print "%s cannot find"%name
def view():
    '''view all person information'''
    f = file("dic.data")
    dic = p.load(f)
    for name,cname in dic.items():
        print '%s at %s'%(name,dic[name].getad())
while True:
    s = raw_input('enter cmd-->')
    if s == 'quit':
        break
    else:
        exec s
