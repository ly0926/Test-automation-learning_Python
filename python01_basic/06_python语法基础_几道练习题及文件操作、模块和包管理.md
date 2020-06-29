```python
#判断给定的书是否为水仙花数

s = input('输入正整数：')  #input()返回对象为字符串，转为int
sum = 0 #

if(s.isdigit()):               #s.isdigit(),判断字符串是否为全数字
    num = len(s)               #对象长度或整数位数
s = int(s)                       #str强转为int
temp = s
while temp:
    sum+=(temp%10)**num           #
    temp//=10
if sum==s:
    print(s,"是水仙花数")
else:
    print(s,"不是水仙花数")



#回文数
num = 1234321
temp = num

x = 0
while (temp):
     x = x * 10 + temp % 10
     temp //= 10

if(x == num):
    print('是回文数')
else:
    print('不是')

#斐波那契数列  兔子数列   跳台阶问题  抛硬币问题

num = 100       #100以内的斐波那契数

a = 0
b = 1           #d第0项和第1项

while a <= num:
    print(a,end = ' ')
    a,b=b,a+b


#求阶乘
num = int(input('请输入一个正整数：'))
result = 1

for i in range(1, num + 1):
        result *= i
print(result)




#打印1~100之间的素数

from math import sqrt           #引入sqrt()求平方根

def isprime(x):                 #判断x是否为素数   返回bool
    t = True                 
    if x ==1:
        t = False
    k=int(sqrt(x))              #终止条件可以是x,x/2,x**0.5   素数求解的n种境界
    for j in range(2,k+1):
        if x%j==0:
            t = False
            break 
    return t

for i in range(2,101):
    if isprime(i):
        print (i,end = ' ')




#CRAPS赌博游戏

from random import randint

money = 1000

while money > 0:
    go = False
    wager = int(input('请下注：'))
    while wager > money:
        print('你的钱不够,请重新下注')
        wager = int(input('请输入你的赌注：'))
    print('开始摇骰子')
    first_01 = randint(1, 6)
    first_02 = randint(1, 6)
    first = first_01 + first_02
    print('你摇出了%d点和%d点' % (first_01, first_02))
    if first == 7 or first == 11:
        print('你赢了 %d 元' % wager)
        money += wager
    elif first == 2 or first == 3 or first == 12:
        print('你输了 %d 元' % wager)
        money -= wager
    else:
        go = True
        while go:
            second = randint(1, 6) + randint(1, 6)
            if second == 7:
                print('你输了')
                money -= wager
                go = False
            elif second == first:
                print('你赢了')
                money += wager
                go = False
            else:
                go = True
print('你破产了，游戏结束！')
```

#### 模块和包管理

##### 模块和包的定义
模块（Moudle）：模块就是一个py文件，包含了Python对象定义和Python语句。  
模块其实分为四个通用类别，分别是：  
1、使用纯Python代码编写的py文件  
2、包含一系列模块的包  
3、使用C编写并链接到Python解释器中的内置模块  
4、使用C或C++编译的扩展模块  

##### 模块的作用
使用模块既保证了代码的重用性，又增强了程序的结构性和可维护性。另外除了自定义模块，我们还可以导入使用内置或第三方模块提供的现成功能，这种“拿来主义”极大地提高了程序员的开发效率。  
##### 模块的使用
想要使用模块，必须先要将模块加载进来，可以通过关键字 import  或 from进行加载；需要注意的是模块和当前文件在不同的命名空间中。  

1. import导入模块
```python
import module1
import module2
    ...
import moduleN

#还可以在一行导入，用逗号分隔开不同的模块    但分开导入更为规范，可读性强
import module1,module2,...,moduleN
```

2. from-import 
```python
from module1 import fun1
from module2 import fun2
    ...
from module3 import fun3

from module import * #把module模块中所有的方法都导入到当前执行文件的名称空间中，在当前位置直接可以使用这些对对象
```

3. as起别名
```python
import module1 as m1
#通常在被导入的名字过长时采用起别名的方式来精简代码，另外为被导入的名字起别名可以很好地避免与当前名字发生冲突
from module1 import fun1 as fun1_m1
```

4. 循环导入  
循环导入问题指的是在一个模块加载/导入的过程中导入另外一个模块，而在另外一个模块中又返回来导入第一个模块中的名字，由于第一个模块尚未加载完毕，所以引用失败、抛出异常，究其根源就是在python中，同一个模块只会在第一次导入时执行其内部代码，再次导入该模块时，即便是该模块尚未完全加载完毕也不会去重复执行内部代码。

5.搜索模块的路径与优先级  
在导入一个模块时，如果该模块已加载到内存中，则直接引用，否则会优先查找内置模块，然后按照从左到右的顺序依次检索sys.path中定义的路径，直到找模块对应的文件为止，否则抛出异常。  
sys.path也被称为模块的搜索路径，它是一个列表类型,列表中的每个元素都可以当作是一个目录。
```python
import sys

for i in sys.path:
    print(i)
```
6. 区分py文件的两种用途  
一个Python文件有两种用途，一种被当主程序/脚本执行，另一种被当模块导入，为了区别同一个文件的不同用途，每个py文件都内置了__name__变量，该变量在py文件被当做脚本执行时赋值为“__main__”,在py文件被当做模块导入时赋值为模块名。


####  文件处理  
应用程序运行过程中产生的数据最先都是存放于内存中的，若想永久保存下来，必须要保存于硬盘中。应用程序若想操作硬件必须通过操作系统，而文件就是操作系统提供给应用程序来操作硬盘的虚拟概念，用户或应用程序对文件的操作，就是向操作系统发起调用，然后由操作系统完成对硬盘的具体操作。

##### 文件操作的基本流程  
```python
# 1. 打开文件，由应用程序向操作系统发起系统调用open()，操作系统打开该文件，对应一块硬盘空间，并返回一个文件对象赋值给一个变量f
#编码方式很重要   乱码问题
f=open('a.txt',mode='r',encoding='utf-8') #默认打开模式就为r 只读， 在文件不存在时则报错,文件存在则文件内指针直接跳到文件开头
                                     # w(只写)，  文件不存在时会创建空文档,文件存在会清空文件,文件指针指向文件开头
                                     # a(追加)    文件不存在时会创建空文档,文件存在会将文件指针指向到文件末尾
                                    
                                     # 控制文件读写内容的模式: t 文本模式（默认）
                                     #                      b 二进制模式
# 2. 调用文件对象下的读/写方法，会被操作系统转换为读/写硬盘的操作
data=f.read()

# 3. 向操作系统发起关闭文件的请求，回收系统资源
f.close()
```
   
```python
# 资源回收:在操作完毕一个文件时，必须回收操作系统打开的文件资源,即f.close()
#为了防止我们忘记f.close()，python提供了with关键字来帮我们管理上下文

# 1、在执行完子代码块后，with 会自动执行f.close()
with open('a.txt','w') as f:
    pass 

# 2、可用用with同时打开多个文件，用逗号分隔开即可
with open('a.txt','r') as read_f,open('b.txt','w') as write_f:  
    data = read_f.read()
    write_f.write(data)
```
##### 文件操作     
```python
# 读操作
f.read()  # 读取所有内容,执行完该操作后，文件指针会移动到文件末尾
f.readline()  # 读取一行内容,光标移动到第二行首部
f.readlines()  # 读取每一行内容,存放于列表中

# 写操作
f.write()
f.writelines() 

# 控制文件内的指针
# 文件内指针的移动都是Bytes为单位的,唯一例外的是t模式下的read(n),n以字符为单位
# 之前文件内指针的移动都是由读/写操作而被动触发的，若想读取文件某一特定位置的数据，则则需要用f.seek方法主动控制文件内指针的移动，详细用法如下：
# f.seek(指针移动的字节数,模式控制): 
# 模式控制:
# 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
# 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
# 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
# 强调:其中0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用
```