def sum (x,y):
    result={}
    result['r']=x['r']+y['r']
    result['i']=x['i']+y['i']
    return result
def mul(x,y):
    result={}
    result['r']=x['r']*y['r']-x['i']*y['i']
    result['i']=x['r']*y['i']+x['i']*y['r']
    return result
def sub(x,y):
    result={}
    result['r']=x['r']-y['r']
    result['i']=x['i']-y['i']
    return result
def show(x):
    r=str(x['r'])+'+'+str(x['i'])+'i'
    return r
a={'r':5,'i':8}
b={'r':8,'i':14}
c=mul(a,b)
d=sum(a,b)
e=sub(a,b)
print(f"Sum of {show(a)} and {show(b)} is {show(d)}")
print(f"Muliplication of {show(a)} and {show(b)} is {show(c)}")
print(f"Submission of {show(a)} and {show(b)} is {show(e)}")

