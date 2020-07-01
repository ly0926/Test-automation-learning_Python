#####  面向过程和面向对象  
面向过程的程序设计的核心是过程，过程即解决问题的步骤，面向过程的设计就是分析出解决问题所需要的步骤，然后用函数把这些步骤一步一步实现，使用的时候一个一个依次调用就可以了。  

特性：模块化；流程化。  

优点：1. 极大的降低了写程序的复杂度，只需要顺着要执行的步骤，堆叠代码即可。  
&emsp;&emsp;&emsp;2. 性能比面向对象高，因为类调用时需要实例化，开销比较大，比较消耗资源。    

缺点：一套流水线或者流程就是用来解决一个问题，没有面向对象易维护、易复用、易扩展。

应用场景：一旦完成基本很少改变的场景，比如Linux內核，git，以及嵌入式开发等重视性能。  

  
    
面向对象的程序设计的核心是对象，它是对现实世界理解和抽象的方法，把构成问题事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而是为了描叙某个事物在整个解决问题的步骤中的行为。  

特性：封装；继承；多态。

优点：易维护、易复用、易扩展。

缺点：性能比面向过程低。

应用场景：需求经常变化的软件，一般需求的变化都集中在用户层，互联网应用，企业内部软件，游戏等。

看到一个比较好的文章，引用一下：
    
    用面向过程的方法写出来的程序是一份蛋炒饭，而用面向对象写出来的程序是一份盖浇饭。所谓盖浇饭，北京叫盖饭，东北叫烩饭，广东叫碟头饭，就是在一碗白米饭上面浇上一份盖菜，你喜欢什么菜，你就浇上什么菜。我觉得这个比喻还是比较贴切的。
    蛋炒饭制作的细节，我不太清楚，因为我没当过厨师，也不会做饭，但最后的一道工序肯定是把米饭和鸡蛋混在一起炒匀。盖浇饭呢，则是把米饭和盖菜分别做好，你如果要一份红烧肉盖饭呢，就给你浇一份红烧肉；如果要一份青椒土豆盖浇饭，就给浇一份青椒土豆丝。
    蛋炒饭的好处就是入味均匀，吃起来香。如果恰巧你不爱吃鸡蛋，只爱吃青菜的话，那么唯一的办法就是全部倒掉，重新做一份青菜炒饭了。盖浇饭就没这么多麻烦，你只需要把上面的盖菜拨掉，更换一份盖菜就可以了。盖浇饭的缺点是入味不均，可能没有蛋炒饭那么香。
    到底是蛋炒饭好还是盖浇饭好呢？其实这类问题都很难回答，非要比个上下高低的话，就必须设定一个场景，否则只能说是各有所长。如果大家都不是美食家，没那么多讲究，那么从饭馆角度来讲的话，做盖浇饭显然比蛋炒饭更有优势，他可以组合出来任意多的组合，而且不会浪费。
    盖浇饭的好处就是”菜”“饭”分离，从而提高了制作盖浇饭的灵活性。饭不满意就换饭，菜不满意换菜。用软件工程的专业术语就是”可维护性“比较好，”饭” 和”菜”的耦合度比较低。蛋炒饭将”蛋”“饭”搅和在一起，想换”蛋”“饭”中任何一种都很困难，耦合度很高，以至于”可维护性”比较差。软件工程追求的目标之一就是可维护性，可维护性主要表现在3个方面：可理解性、可测试性和可修改性。面向对象的好处之一就是显著的改善了软件系统的可维护性。  

#####  几组概念  
    1、封装（encapsulation）：把需要重用的函数或者功能封装，方便其他程序直接调用。
    2、继承（inheritance）：子项继承父项的某些功能，在程序中表现某种联系(Python不支持多态)。
    3、多态（polymorphism）：一个函数有多种表现形式，调用一个方法有多种形式，但是表现出的方法是不一样的。
    4、类：对具有相同数据或者方法的一类对象的集合。
    5、对象：对象是一个类的具体实例。
    6、实例化：从类->对象的过程。
    7、类属性：属于一个类中所有对象的属性。
    8、类方法：那些无须特定的对性实例就能够工作的从属于类的函数。

##### 类的定义与实例化
```python
# 类定义的语法
#class 类名：   # 关键字：class；类的命名应该使用“驼峰体”（首字母大写）
  # 属性：变量
  # 行为：函数

class SeniorTestingEngineer:  # 高级测试工程师类
     # 属性
     work_year = 3
     salary = 20000

     # 行为
     def coding(self):  # self 对象本身--》有self标记为对象函数，只能对象来调用。self是变量，也可以用其他a，b等
         print('self:{}'.format(self))
         print('会写代码')

     def do_sql(self):
         print('会操作数据库')

     def do_linux(self):
         print('会使用linux系统')

     def do_funtion_testing(self):
         print('会功能测试')

     def do_api_test(self):
         print('会接口测试')

# 1. 创建对象：类名（）
# 2. 对象拥有类里面的所有属性和函数的使用权
# 3. 类里面的函数只能有对象来调用
# 4. 类里面的属性可以对象或类名调用

p_1 = SeniorTestingEngineer()  # 创建对象
# 属性和行为的调用
print(p_1.work_year)
print(p_1.salary)
p_1.coding()
p_1.do_funtion_testing()
```

#####  面向对象的各种方法（绑定方法与非绑定方法）  
```python
class SeniorTestingEngineer:  # 高级测试工程师类
     # 属性
     work_year = 3
     salary = 20000

     # 行为
     def coding(self):  # 对象方法
         print('self:{}'.format(self))
         print('会写代码')
         print(self.work_year)

     @staticmethod
     def do_sql():  # 静态方法,没有self参数，可以非对象调用，类名.方法 进行调用，不需要特地创建对象调用
         print('会操作数据库')
         # print(self.work_year)  # 不支持属性调用，不使用类属性的方法可以写成静态方法

     @classmethod  # 类方法，由cls参数标记
     def do_linux(cls):  # 类方法
         print('cls为：{}'.format(cls))
         print('会使用linux系统')
         print(cls.work_year)  # 类属性调用 ，不支持self.属性调用


'''区别'''

# 1.对象方法：有self参数，只能由对象调用
#            对象方法中可直接通过self.属性 调用类的属性
# 2.静态方法：由@staticmethod装饰器，无self参数，可以对象或类名调用
#            静态方法中不可直接通过self.属性 调用类的属性
# 3.类方法：由@classmethod装饰器，且有cls参数标记，可以对象或类名调用
#           类方法中可直接通过cls.属性 调用类的属性
# 4. 三种方法中都可以有：位置参数、默认参数、动态参数、关键字参数

p_1 = SeniorTestingEngineer()  # 创建对象
print(p_1.work_year)
print(p_1.salary)
p_1.coding()
p_1.do_sql()
p_1.do_linux()

P_2 = SeniorTestingEngineer  # 类名
print(P_2.work_year)  # 类名调用属性
print(P_2.salary)  # 类名调用属性
P_2.do_sql()    # 静态方法支持类名调用
P_2.do_linux()  # 类方法支持类名调用
# P_2.coding()  # 对象方法不支持类名调用


'''类中的方法相互调用'''

class SeniorTestingEngineer:  # 高级测试工程师类
    # 属性
    work_year = 3
    salary = 20000

    # 行为
    def coding(self):  # 对象方法
        print('会写代码')

        # self.do_linux()  # 类方法调用
        # self.do_sql()  # 静态方法调用

    @staticmethod
    def do_sql():
        print('会操作数据库')
        # SeniorTestingEngineer().coding()  # 对象方法调用
        # SeniorTestingEngineer().do_linux()  # 类方法调用


    @classmethod  # 类方法，由cls参数标记
    def do_linux(cls):  # 类方法
        print('会使用linux系统')

        cls().coding()  # 对象方法调用
        cls.do_sql()  # 静态方法调用


p = SeniorTestingEngineer()  # 创建实例

# p.coding()  # 测试 类方法和静态方法 调用

# p.do_sql()  # 测试 对象方法和类方法 调用

p.do_linux()  # 测试 对象方法和静态方法 调用
```

#####  类的初始化  

```python
'''初始化函数'''
# 1. 作用：在创建对象的时候，设置初始值(属性参数化)
# 2.用法：def __init__(self,参数1，参数2...)
# 3. 有初始化函数的类，创建对象时需传参

class SeniorTestingEngineer:  # 高级测试工程师类
    # 属性
    work_year = 3
    salary = 20000

    # 初始化函数

    # def __init__(self):  # 无参数
    #     self.name = 'Tom'
    #     self.age= 18
    #     self.sex = 'male'

    def __init__(self, name, age, sex):  # 有传参
        self.name = name  # 将属性赋值给对象
        self.age = age
        self.sex = sex

    # 行为
    def coding(self, language):  # 对象方法
        print('{}同学，年龄{}，性别{}，会写{}代码'.format(self.name, self.age, self.sex, language))

    @staticmethod
    def do_sql():
        print('会操作数据库')

    @classmethod  # 类方法，由cls参数标记
    def do_linux(cls):  # 类方法
        print('会使用linux系统')


# 初始化函数无参数 创建对象
# p1 = SeniorTestingEngineer()  # 创建对象跟无初始化函数一样 不需要传参
# p1.coding('python')

# p2 = SeniorTestingEngineer()  # 无法对name，work_year,salary 进行参数化
# p2.coding('java')


# 初始化函数有参数 创建对象
p3 = SeniorTestingEngineer('Lisa', 20, 'famale',)  # 创建对象需要传参
p3.coding('python')

p4 = SeniorTestingEngineer('Annie', 19, 'famale',)  # 可以对name，age,sex 进行参数化
p4.coding('java')


''' _call_ 方法'''

# 1.作用：能够让类的实例对象，像函数一样被调用
# 2._call__()方法还可以带参数

class Info(object):

    def __init__(self):
        print('此处_init_方法')

    def __call__(self, name, sex):
        print("此处_call_方法")
        print("姓名：{}".format(name))
        print("性别：{}".format(sex))


f = Info()
print("f为：{}".format(f))

# 有_call_方法
f('Tom', 'male')

# 无_call_方法
# f('Tom', 'male')  # 不支持直接调用，故会报错：TypeError: 'Info' object is not callable


#  _init_方法 和_call_方法参数使用
# 1. init中的参数需创建对象时传入
# 2. call中的参数，在调用时传入

class Info(object):

    def __init__(self, name, sex):
        print('此处_init_方法')
        self.name = name
        self.sex = sex
        print("self.name:{}".format(self.name))
        print("self.sex:{}".format(self.sex))

    def __call__(self, name, sex):
        self.name = name
        self.sex = sex
        print("此处_call_方法")
        print("self.name:{}".format(self.name))
        print("self.sex:{}".format(self.sex))


f = Info('李梅', '女')  # 创建对象
f('李雷', '男')  # 类直接调用
```



















