# in the below code i used only one if condition and one loop
a={1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
d,e,c,b=0,'',int(input('give your no. here  ')),[1,4,5,9,10,40,50,90,100,400,500,900,1000]
while c!=0:
    if b[d]>c:
        e+=a[b[d-1]]
        c%=b[d-1]
        d=0
    d+=1
print(e)
# in the below code i used a single loop and nothing else
a,b,c={1000:'m',900:'cm',500:'d',400:'xd',100:'c',90:'xc',50:'l',40:'xl',10:'x',9:'ix',5:'v',4:'iv',1:'i'},'',int(input())
for i in a.keys():
    d=c // i
    c%=i
    b+=a[i]*d
print(b)