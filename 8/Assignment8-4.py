def sum(x,y):
    result={}
    result['s']=x['s']+y['s']
    result['h']=x['h']+y['h']
    result['m']=x['m']+y['m']
    if result['s']> 60:
        result['s']-=60
        result['m']+=1
    if result['m']> 60:
        result['m']-=60
        result['h']+=1 
    return result

def div(x,y):
    result={}
    result['s']=x['s']-y['s']
    result['h']=x['h']-y['h']
    result['m']=x['m']-y['m']
    if result['h']<0:
        result['s']*=-1
        result['h']*=-1
        result['m']*=-1
    if result['m']<0:
        result['m']+=60
        result['h']-=1
    if result['s']<0:
        result['s']+=60
        result['m']-=1
    return result
def time2second(x):
    s=x['h']*3600+x['m']*60+x['s']
    return s
def second2time(x):
    result={}
    result['h']=x//3600
    result['m']=(x-result['h']*3600)//60
    result['s']=x-result['h']*3600-result['m']*60
    return result
def show(x):
    print(x['h'],':',x['m'],':',x['s'])
a={'h':2,'m':30,'s':45}
b={'h':3,'m':17,'s':40}

show(sum(a,b))
show(div(a,b))
c=time2second(a)
print(c)
show(second2time(c))