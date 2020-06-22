```python
#判断给定的书是否为水仙花数

s = int(input('输入正整数：'))  #input()返回对象为字符串，转为int
sum = 0 #

if(s.isdigit()):               #s.isdigit(),判断字符串是否为全数字
    num = len(s)               #对象长度或整数位数
s=int(s)                       #str强转为int
while s:
    sum+=(s%10)**num           #
    s//=10

if sum==s:
    print(s,"是水仙花数")
else:
    print(s,"不是水仙花数")
```