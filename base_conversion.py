import logging
logging.basicConfig(level=logging.INFO)

class Number():
    def __init__(self, num):
        self.num=num
        if self.num>2**16:
            logging.error("The number you assigned is out of range! Sorry!")
        self.digitslist=[]
        for b in range(2,17):
            digits=self.check_num(self.num, b)
            self.digitslist.append(digits)

    def check_num(self, num, b):
        for i in range(1,17):
            if num<b**i:
                return i
                break

    def get_new_number(self, b):
        num=self.num
        digits=self.digitslist[b-2]
        digitslist=list(reversed(list(range(digits))))
        extra=["A","B","C","D","E","F"]
        r=""
        for k in digitslist:
            i, num=divmod(num,b**k)
            if i>=10:
                i=extra[i-10]
            r=r+str(i)
        return r
            

if __name__=="__main__":
    orig=31
    base=16
    num=Number(orig)
    print(num.get_new_number(base))
