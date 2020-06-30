#####   异常  
异常是指在程序运行过程中出现的意外的情况，若未在程序中对其进行处理，该异常就会抛出，程序的运行也随之终止。    
```python
# 异常常分为两种：一种是语法错误SyntaxError，这种错误应该在程序运行前就修改正确。  
#              另一种是逻辑错误，常见的逻辑错误如：
#                                             TypeError：数字类型无法与字符串类型相加                                              
#                                             ValueError：当字符串包含有非数字的值时，无法转成int类型                                              
#                                             NameError：引用了一个不存在的名字x
#                                             KeyError：引用了一个不存在的key
#                                             IndexError：索引超出列表的限制
#                                             AttributeError：引用的属性不存在
#                                             ZeroDivisionError：除数不能为0

```
#####   异常处理  
为了保证程序的容错性与可靠性，即在遇到错误时有相应的处理机制不会任由程序崩溃掉，我们需要对异常进行处理，处理的基本形式为：  
```python
try:  
    被检测的代码块 
except 异常类型：
    检测到异常，就执行这个位置的逻辑
```
举例：  
```python
try:
    print('start...')
    print(x) # 引用了一个不存在的名字，触发异常NameError
    print('end...')
except NameError as e: # as语法将异常类型的值赋值给变量e，这样我们通过打印e便可以知道错误的原因
    print('异常值为：%s' %e)
print('run other code...')

#执行结果为
start...
异常值为：name 'x' is not defined
run other code...
```
如果我们想分别用不同的逻辑处理，需要用到多分支的except（类似于多分支的elif，从上到下依次匹配，匹配成功一次便不再匹配其他）  
```python
try:
    被检测的代码块
except NameError:
    触发NameError时对应的处理逻辑
except IndexError:
    触发IndexError时对应的处理逻辑
except KeyError:
    触发KeyError时对应的处理逻辑
```
举例  
```
def convert_int(obj):
    try:
        res=int(obj)
    except ValueError as e:
        print('ValueError: %s' %e)
        res=None
    except TypeError as e:
        print('TypeError: %s' %e)
        res=None
    return res

convert_int('Tom') # ValueError: invalid literal for int() with base 10: 'Tom'
convert_int({'n':1}) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
```
如果我们想多种类型的异常统一用一种逻辑处理，可以将多个异常放到一个元组内，用一个except匹配  
```
try:
    被检测的代码块
except (NameError,IndexError,TypeError):
    触发NameError或IndexError或TypeError时对应的处理逻辑
```
 如果我们想捕获所有异常并用一种逻辑处理，Python提供了一个万能异常类型Exception  
```
try:
    被检测的代码块
except NameError:
    触发NameError时对应的处理逻辑
except IndexError:
    触发IndexError时对应的处理逻辑
except Exception:
    其他类型的异常统一用此处的逻辑处理
```
在多分支except之后还可以跟一个else（else必须跟在except之后，不能单独存在），只有在被检测的代码块没有触发任何异常的情况下才会执行else的子代码块。  
```
try:
    被检测的代码块
except 异常类型1:
    pass
except 异常类型2:
    pass
......
else:
    没有异常发生时执行的代码块
```
 此外try还可以与finally连用，从语法上讲finally必须放到else之后，但可以使用try-except-finally的形式，也可以直接使用try-finally的形式。无论被检测的代码块是否触发异常，都会执行finally的子代码块，因此通常在finally的子代码块做一些回收资源的操作，比如关闭打开的文件、关闭数据库连接等  
 
```python
try: 
    被检测的代码块 
except 异常类型1: 
    pass 
except 异常类型2: 
    pass 
...... 
else: 
    没有异常发生时执行的代码块 
finally: 
    无论有无异常发生都会执行的代码块
```
举例  
```
f=None
try:
    f=open(‘db.txt’,'r',encoding='utf-8')
    s=f.read().strip()
    int(s)  # 若字符串s中包含非数字时则会触发异常ValueError
    # f.close() # 若上面的代码触发异常，则根本不可能执行到此处的代码，应该将关闭文件的操作放到finally中
finally:
    if f: # 文件存在则f的值不为None
        f.close()
```

另外，对于违反程序员自定制的各类规则，则需要由程序员自己来明确地触发异常，这就用到了raise语句，raise后必须是一个异常的类或者是异常的实例。  
```
class Student:
    def __init__(self,name,age):
        if not isinstance(name,str):
            raise TypeError('name must be str')
        if not isinstance(age,int):
            raise TypeError('age must be int')

        self.name=name
        self.age=age

stu1=Student(4573,18)    # TypeError: name must be str
stu2=Student('Tom','18') # TypeError: age must be int
```
 最后，Python还提供了一个断言语句assert expression，断定表达式expression成立，否则触发异常AssertionError，与raise-if-not的语义相同，如下  
 ```
age='18'

# 若表达式isinstance(age,int)返回值为False则触发异常AssertionError
assert isinstance(age,int)

# 等同于
if not isinstance(age,int):
    raise AssertionError
```
异常处理一般使用在错误发生的条件是“不可预知”的情况下。  

