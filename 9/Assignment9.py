class Kasr:
    def __init__(self,s=1,m=1):
        self.sorat=s
        self.makhraj=m

    def sum(self,b):
        result=Kasr()
        result.sorat=self.sorat * b.makhraj + self.makhraj * b.sorat
        result.makhraj=self.makhraj * b.makhraj
        return result

    def mul(self,b):
        result=Kasr()
        result.sorat=self.sorat * b.sorat
        result.makhraj=self.makhraj * b.makhraj
        return result

    def sub(self,b):
        result=Kasr()
        result.sorat=self.sorat * b.makhraj - self.makhraj * b.sorat
        result.makhraj=self.makhraj * b.makhraj
        return result

    def div(self,b):
        result=Kasr()
        result.sorat=self.sorat * b.makhraj
        result.makhraj=self.makhraj * b.sorat
        return result

    def show(self):
        print(self.sorat,'/',self.makhraj)

a=Kasr(5,8)
b=Kasr(8,14)
c=a.mul(b).show()
d=a.sum(b).show()
e=a.div(b).show()
f=a.sub(b).show()

class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def sum(self,b):
        result=Time()
        result.hour=self.hour + b.hour
        result.minute=self.minute + b.minute
        result.second=self.second + b.second

        if result.second > 60:
            result.second -= 60
            result.minute +=1
        if result.minute > 60:
            result.minute -= 60
            result.hour += 1
        return result

    def sub(self,b):
        result=Time()
        result.hour=self.hour - b.hour
        result.minute=self.minute - b.minute
        result.second=self.second - b.second

        if result.hour < 0:
            result.second *= -1
            result.hour *= -1
            result.minute *= -1
        if result.minute < 0:
            result.minute += 60
            result.hour -= 1
        if result.second <0:
            result.second +=60
            result.minute -=1
        return result

    def time2second(self):
        result=self.hour*3600+self.minute*60+self.second
        return result

    def second2time(self,s):
        result=Time()
        result.hour=s//3600
        result.minute=(s-result.hour*3600)//60
        result.second=s-result.hour*3600-result.minute*60
        return result

    def show(self):
        print(self.hour,':',self.minute,':',self.second)

a=Time(2,30,45)
b=Time(3,17,40)
c=a.sum(b).show()
d=a.sub(b).show()
e=a.time2second()
f=a.second2time(e).show()
print(e)