import tkinter
#position = index(substr,begin=0,end=len(string))
#position = find(substr,begin=0,end=len(string))
#描述：index和find函数的作用相同，都是查找子字符串，可以指定开始和结束索引，在一个范围内查找。
#返回值：子字符串的其实索引值。index和find的区别是，当没有找到子字符串时，index报错，find返回-1.
s = 'abcdefdef'
s1 = s.find('de')
s2 = s.index('de',5)
print(s1,s2)
#replace
#str_new = replace(substr_old,substr_new,[max])
#描述：替换函数，如其名，查找子字符串subst，替换成substr_new.第三个参数可选，指定替换的最大次数，默认是全部替换
#返回值：返回替换后的新字符串
s = 'abcdefdef'
s1 = s.replace('de','gh')
s2 = s.replace('de','gh',1)
print(s1,s2)
#split
#list = split(str='',num)
#描述：split函数用分隔字符str把字符串拆分成若干个子字符串。number指定拆分多少次，若没有指定次数，则为全部拆分，
#返回值：拆分后的子字符串列表
s = 'I am learning python'
list1 = s.split(' ')
list2 = s.split(' ',2)
print(list1,list2)
#upper lower
#str_new = upper()
#str_new = lower()
#描述：把字符串转换成大写或小写
#返回值：大小写转换后的新字符串
s = 'abc'
s1 = s.upper()
s2 = s.lower()
print(s1,s2)
#strip lstrip rstrip
#str_new = strip(char='')
#str_new = rstrip(char='')
#str_new = lstrip(char='')
#描述：strip函数是用来去除头或尾的指定字符，默认是去掉空格
#返回值：返回处理后的新字符串
s = ' abc\n'
s1 = s.lstrip()
s2 = s.rstrip('\n')
print(s1,s2)
#statwith endswith
#boolean = startswith(str,begin=0,end=len(string))
#boolean = endswith(str,begin=0,end=len(string))
#描述：检查字符串是否易str开头或结尾，可以在指定范围内检查
#返回值：如果检查到，返回True，否则返回False
s = 'clk_a'
b1 = s.startswith('clk')
s = 'rst_m'
b2 = s.endswith('_n')
print(b1,b2)
#format
#str_new = '{}{}...'format(arg1,arg2,...)
#描述：format用来把其它数字、字符串、甚至对象等格式化字符串。大括号{}用来指定名称、位置、数字的格式。
#返回值:格式化后的字符串

s = 'I am learing {lang}'.format(lang='python')
s1 = '{0} {1} {0}'.format('face','to')
s2 = '{} {} {}'.format('I','love','python')
print(s + "\n",s1 + "\n",s2)
#第一种，按名称替换 第二种，按位置替换 第三种，默认按位置替换，也是最常见的替换方式


#1.怎么查看string还内置了什么函数？ s = 'abc' ; print(dir(s)); dir是一个内置函数，能够查看类的属性和方法
#1.怎么查看具体函数的使用方法？ print(help(s.find))
#列表作为一种序列，与字符串一样，支持序列的基本操作，如 + 拼接 *重复 index索引 slice切片
#列表作为对象本身的操作方法有append extend insert remove pop sort reverse count index clear

#元组（Tuple）元组可以理解成只读的列表。不能进行上面的几乎所有操作，除了index和count，只读属性有点像字符串，正因为定义后不能修改，元组是定长的
#元组是用于防止误修改的情况，比如作为函数的输入参数，并不希望被函数内部误修改到

#1.字典最基本的操作就是根据索引取值，如stdcell[buff0] 还有一种根据索引取值的方法就是用get()函数stdcell.get('buff0')
#2.用len()计算字典的元素个数，如len(stecell)
#3.修改元素的值，一种方法是update()函数，这种方法是可以一次更新多个值，甚至增加新的键值对
#4.删除元素用pop()
#5.清空函数clear()
#6分别提取字典的键和值的列表：keys()、values()
#stdcell.keys()
#stdcell.values()
#keys()可以配合for循环对字典有序输出，

for c in "abc":
    print(c + "\n",end='')

#for 循环与range
#range是for循环的最佳拍档，利用range我们可以递增或递减的，指定步长的循环。range(start=0,stop,step=1) start是开始点，默认是0，stop是结束点，
#但不包括结束点，step是步长，默认是1.当开始点是0，步长是1时，可以简写成range(stop)
s = "abc"
for x in range(len(s)):
    print(s[x])

s = "abcdef"
for x in range(len(s)-1,-1,-2):
    print(s[x])

#for 循环与zip
#zip可以把两个列表打包，for可以并行对两个列表遍历。
L1 = ["AND2","NOR2","XOR2"]
L2 = [10,20,30]
for (x,y) in zip(L1,L2):
    print("Cell {} used {}".format(x,y))

#for 循环与enumerate
#enumerate可以同时取出序列的索引和元素，当遍历序列时，如果需要索引值时，这样会比较方便。
L1 = ["AND2","NOR2","XOR2"]
for (i,c) in enumerate(L1):
    print("{}:{}".format(i,c))
#for 循环与map
#map把序列的元素按照指定函数进行转换，并返回新的序列。
s = 'abc'
for x in map(ord,s):
    print(x)
#退出循环，对于循环可以用break和continue来退出循环，区别在于break退出整个while或者for,而continue会立即结束本次循环，进入下一次循环
L1 = ["NAD2","NOR2","NXOR2","AND2","OR2","XOR2","INV2","BUF2"]
L2 = [10,20,30,1,6,3,60,7]
i = 0
for (x,y) in zip(L1,L2):
    if y < 5:
        continue
    print("Cell {} used {}".format(x,y))
    i += 1

D1 = {"NAND2":10,
      "NOR2":20,
      "NXOR2":30,
      "AND2":1,
      "OR2":6,
      "XOR2":3,
      "INV2":60,
      "BUF2":7}
L2 = sorted(D1.items(),key = lambda d:d[1],reverse=True)
D3 = dict(L2)
i = 0
for k in D3.keys():
    if i == 6:
        break
    print("Cell {} used {}".format(k,D3[k]))
    i += 1
#1.函数也是对象
#2.函数定义是动态执行的，没有编译的过程，所以使用之前必须定义
#3.函数定义可以出现在任意地方，甚至在另一个函数内部
#4.函数的参数是对象引用，是指针传递
#5.函数的参数类型由传入的对象决定，利用操作符重载，实现了多态


##三段代码的对比
a = 1
def func_a():
    a = 2
    def func_b():
        a = 3
        print(a)
    func_b()
func_a()

a =  1
def func_a():
    a = 2
    def func_b():
        print(a)
    func_b()
func_a()

a = 1
def func_a():
    def func_b():
        print(a)
    func_b()
func_a()
#从上面的代码来看，python会自动按照由里向外，由近及远的规则查找变量
#示例一，func_b不能修改func_a里面的变量
a = 1
def func_a():
    a = 2
    def func_b():
        a = 3
    func_b()
    print(a)
func_a()
#示例二，func_b修改了func_a里的变量
a = 1
def func_a():
    a = 2
    def func_b():
        nonlocal a
        a = 3
    func_b()
    print(a)
func_a()
#示例三，func_b修改了全局变量，而不影响func_a内部的变量
a = 1
def func_a():
    a = 2
    def func_b():
        global a
        a = 3
    func_b()
    print(a)
func_a()

print(a)
#所以，当需要修改外部变量的值时global和nonlocal是必须的。一般建议是不管是引用还是修改，都使用global和nonlocal

def func(a):
    print("id of a(initially):",id(a))
    a = 88
    print("id if a(assign):",id(a))
    print("value of a:",a)
b = 99
print("id if b:",id(b))
print("value of b (before):",b)

func(b)
print("value if b (after):",b)
#函数的参数传递细节问题非常多，我们写代码时要多用简单，容易理解的编码风格，对于参数我们总结以下几点：
#1.注意可修改型（如数字，字符串）和不可修改类型（如列表，字典）参数的区别，并学会利用拷贝避免风险
#2.按位置和按名称两种调用方式，复杂的情况下多用按名称调用
#3.学会用*和**实现参数个数不确定的函数
#4.注意参数定义和调用时按位置、名称、*、**的顺序
def print_anything(*args):
    args = args[:]
    for arg in args:
        print(arg)

print_anything(1,"abc",[4,5,6],{"name":"dut","area":"40um3"})

def list_sum(l):
    print(l)

    if not l:
        return 0
    else:
        return l[0] + list_sum(l[1:])

sum = list_sum([1,2,3,4,5])
print(sum)

top = tkinter.Tk()

str_e1 = tkinter.StringVar()
e1 = tkinter.Entry(top,textvariable=str_e1)
str_e1.set("hello")
e1.pack()

b1 = tkinter.Button(top,text="press me",command=lambda:print(str_e1.get()))
b1.pack()

top.mainloop()

def sum(a:int,b:int) -> int:
    if not type(a) == sum.__annotations__['a']:
        print("Error:a should be type int")
        return

    return a + b

s = sum(2,5)
print(s)
s = sum('abc',5)
print(s)
#上述例子，使用annotation来限制变量类型，当不符合变量类型时报错。其中：int指定变量类型。函数的返回值的annotati写在最后面-》int


#概要 1.模块是一块积木，是最基本的功能单位
#2.一切都是以模块的形式存在的
#3.再来理解if __name__ == '__main__'
#4.模块的搜索路径sys.path和PYTHONPATH
#5.安装模块
#6.从源码开始安装Tk库

