def sum (x,y):
    result={}
    result['s']=x['s']*y['m']+x['m']*y['s']
    result['m']=x['m']*y['m']
    return result
def mul(x,y):
    result={}
    result['s']=x['s']*y['s']
    result['m']=x['m']*y['m']
    return result
def sub(x,y):
    result={}
    result['s']=x['s']*y['m']-x['m']*y['s']
    result['m']=x['m']*y['m']
    return result
def dev(x,y):
    result={}
    result['s']=x['s']*y['m']
    result['m']=x['m']*y['s']
    return result
def show(x):
    r=str(x['s'])+'/'+str(x['m'])
    return r
a={'s':5,'m':8}
b={'s':8,'m':14}
c=mul(a,b)
d=sum(a,b)
e=sub(a,b)
f=dev(a,b)
print(f"Sum of {show(a)} and {show(b)} is {show(d)}")
print(f"Muliplication of {show(a)} and {show(b)} is {show(c)}")
print(f"Submission of {show(a)} and {show(b)} is {show(e)}")
print(f"Division of {show(a)} and {show(b)} is {show(f)}")

