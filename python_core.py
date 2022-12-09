# ---------Tuple-----------
# def add(a,b,c):
#     return a+b+c

# print(add(*t))

# t = 1,2,4,4,
# print(type(t))

# l,t,s,i = [1,2,3,],(1,2,4,),"hellow",12
# print(s)

# a,b = 1,2
# a,b = b,a
# print(a)

# x,y = (1,2,3),(1,2,3)
# print(x is y, id(x),id(y))

#task 1
# Implement a function get_tuple(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.
# Example:
# >>> get_tuple(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# def get_tuple(num: int) -> tuple[int]:
#     # TODO: Add your code here
#     num = str(num); t = ()
#     for ch in num:
#         temp = (int(ch),)
#         t += temp
#     return t

#task 2
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements. The pairs should be formed as in the example. If there is only one element in the list, return [] instead.

# Example:

# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
# >>> get_pairs([1])
# []
# def get_pairs(lst: list[any]) -> list[tuple[any, any]]:
#     # TODO: Add your code here
#     t = (); l = []
#     for ch in range(len(lst)):
#         if ch+1<len(lst):
#             t = lst[ch],lst[ch+1]
#             l.append(t)
#     return l


#-------------------Set-------------
# se = {1,2,3,2,1,2,}
# print(se)
# se = {}
# print(type(se))
# se = set()
# print(type(se))
# A set is a useful type when dealing with collections without duplicates—especially if you need to compare them, find differences, or check if there is something in common. For these purposes, the set provides useful and fast methods.


#------------Dictionary---------
# d = {
#     'name':'Izzatullo',
#     'age':18,
#     'university':'INHA',
#     'has_job':False,
#     'skills':['python','django','oop']
# }
# for key, value in d.items():
#     print(key)

#Task 1

# s = ' Oh, it is python'; d = {}
# s = s.lower()
# for ch in s:
#     frequency = s.count(ch)
#     d[ch] = frequency

# print(d)

# result = 20 / 2 + 12 * 2 - 9
# print(result)

#(Data types) Final practical test
#Task 1
# l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# S = set();
# for o in l:
#     for obj in o.values():
#         S.add(obj)
# print(S)
#Task 2
# def check(row_start:int, row_end:int, column_start:int, column_end:int) -> list[list[int]]:
#     """
#     Add your code here or call it from here   
#     """
#     l,l1 = [],[]
#     for r in range(row_start,row_end+1):
#         for c in range(column_start,column_end+1):
#             mult = r*c
#             l.append(mult)
#     start = 0; end = (column_end+1)-column_start
#     for i in range(row_end-row_start+1):
#         l1.append(l[start:end])
#         start+=(column_end+1)-column_start
#         end+=(column_end+1)-column_start
#     return l1

# print(check(2,4,3,7))


#-----------------Functions-------------
# def sum_of_2numbers(a,b):
#     return a+b
# def square(n):
#     return n*n
# two_number_adder = sum_of_2numbers
# def adder(func, *args):
#     result = 0
#     for n in args:
#         result+=func(n)
#     return result
# print(square(two_number_adder(1,2)))
# print(adder(square,2,3))
# l = []; l.append(sum_of_2numbers(1,2));l.append(square);print(l)

#Function arguments
# def subtractor(first,second=9):
#     return first-second


# print(subtractor(second=1))

# def printer(*args,**kwargs):
#     for i in args:
#         print('Args:',i)
#     for k in kwargs.values():
#         print('Kwargs:',k)

# printer(1,2,3,name='Izzatullo',h = 123)
#Task0
# def generate_squares(num: int)-> dict[int, int]:
#     d = {}
#     for i in range(1,num+1):
#         d[i] = i*i
#     return d
# print(generate_squares(5))

#Task 2
# friends = [
#     {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
#     {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
# ]

# def foo(*args,**kwargs):
#     print('args: ',args,'kwargs: ',kwargs)

# foo()
#Task 2
# def union(*args):
#     s = set()
#     for arg in args:
#         if type(arg)!=set:
#             for ch in range(len(arg)):
#                 s.add(arg[ch])
#         else:
#             s.update(arg)
# union(('S', 'A', 'M'),{'S','j','N',2} ,['S', 'P', 'A', 'C'],)

# def intersect(*args):
#     s = set();l = [];count = 0
#     for arg in args:
#         if type(arg)!=set:
#             for ch in range(len(arg)):
#                 l.append(arg[ch])
#             count+=1
#         else:
#             for ch in arg:
#                 l.append(ch)
#             count+=1
#     for i in l:
#         if l.count(i) == count:
#             s.add(i)
#     print(l,count,s)
# intersect(('S', 'A',0, 'C'), [0,'P', 'C', 'S'], {'G',0, 'H', 'S', 'C'})

#Task 3
# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# def combine_dicts(*args)->dict:
#     dic = {} ; tuple_list = [];unique_key_list = [];
#     for arg in args: 
#         for i in arg.items():
#             tuple_list.append(i)
    
#     for arg in args:
#         dic.update(arg)
#     for key in dic.keys():
#         unique_key_list.append(key)
#     print(unique_key_list)
#     for uniqueKey in unique_key_list:
#         result = 0
#         for tuple in tuple_list:
#             if uniqueKey == tuple[0]:
#                 result+=tuple[1]
#         dic[uniqueKey] = result  
#     return dic
# print(combine_dicts(dict_1,dict_2,dict_3))




#Recursion
#Task 2

# def linear_seq(sequence):
#     l = []
#     for item in sequence:
#         if type(item) != int:
#            l.extend(linear_seq(item))
#         else:
#             l.append(item)
#     return l
# print(linear_seq([1,2,3,[4,5, (6,7)]]))

#Namespaces

# def explicit(s:str):
#     name  = s
#     def implicit(s):
#         s = name
#         print(s)
#     implicit(name)
# explicit('Izzat')

#Decorators



# def myDec(cool):
#     def wrapper():
#         print('It\'s hot')
#         cool()
#         print('It is cold now')
#     return wrapper
# @myDec
# def my_func():
#     print('Im cool')

# my_func()
# def one_adder(func):
#     def wrapper(x,y):
#        print(func(x,y)+1)
#     return wrapper

# @one_adder
# def adder(n1,n2):
#     return n1+n2

# adder(1,2)

# def square(func):
#     def wrapper(*numbers):
#         print(func(*numbers)**2)
#     return wrapper

# @square
# def sum(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# sum(1,2,1,4)
import time as t
# now = t.time()

# print(f'Answer:{add(2,3)}\nExecution time:{t.time()-now}')
# print(t.time())
# print(t.localtime(1669810533.278775))
# from typing import Dict

# execution_time: dict[str, float] = {}
# def time_decorator(fn):
#     """
#     Create a decorator function `time_decorator`
#     which has to calculate decorated function execution time
#     and put this time value to `execution_time` dictionary where `key` is
#     decorated function name and `value` is this function execution time.
#     """
#     def wrapper(x,y):
#         start = t.time()
#         fn(x,y)
#         ex_time = t.time() - start
#         execution_time[f'{fn}'] = ex_time
#     return wrapper
# @time_decorator
# def add(n,m):
#     return n+m
# add(1,2)
# print(execution_time)
# from typing import Dict
# execution_time: Dict[str, float] = {}


# def time_decorator(fn):
#     """
#     Create a decorator function `time_decorator`
#     which has to calculate decorated function execution time
#     and put this time value to `execution_time` dictionary where `key` is
#     decorated function name and `value` is this function execution time.
#     """
#     def wrapper(x,y):
#         start = t.time()
#         fn(x,y)
#         ex_time = t.time() - start
#         execution_time[f'{fn}'] = ex_time
#         print(execution_time)
#     return wrapper

# @time_decorator
# def add(n,m):
#     t.sleep(0.2)
#     return n+m
# add(10,20)
# print(add.__name__)

# def input_taker(func):
#     def wrapper():
#         l = []
#         a = int(input("Number: "))
#         while a != 0:
#             l.append(a)
#             a = int(input("Number: "))
#         print(func(l))
#     return wrapper

# @input_taker
# def square(args):
#     return list(map(lambda a: a**2,args))
# square()

# @input_taker
# def mult_by_2(args):

#     return list(map(lambda b: 2*b,args))

# mult_by_2()

# def perfomance(func):
#     def wrapper(*args, **kwargs):
#         start  = t.time()
#         func(*args,**kwargs)
#         stop = t.time()
#         print(f'Time taken: {stop - start} seconds')
#     return wrapper

# @perfomance
# def some():
#     for i in range(1000000000):
#         i*5
# some()
#Task 2 
# def log(fn):
#     def wrapper(*args,**kwargs):
#         start = t.time()
#         fn(*args,**kwargs)
#         stop = t.time()
#         l = ['a','b','c','d']; argstring = ''; kwargstring = ''
#         for i in range(len(args)):
#             argstring = argstring + f'{l[i]}={args[i]}, '
#         for i in kwargs.items():
#             kwargstring = kwargstring + f'{i[0]}={i[1]}, '
#         if len(kwargs)== 0:
#             log_text = f'{fn.__name__}; args: {argstring[:len(argstring)-2]}; execution time: {round(stop-start,2)} sec.'
#         else:
#             log_text = f'{fn.__name__}; args: {argstring[:len(argstring)-2]}; kwargs: {kwargstring[:len(kwargstring)-2]}; execution time: {round(stop-start,2)} sec.' 
#         out = open('log.txt','a')
#         out.write(f'{log_text}\n')
#         out.close()
#     return wrapper
 
# @log
# def foo(*args,**kwargs):
#     pass
# foo(1,2,c=3,d=4)


# def validate(fn):
#     '''
#     Add corresponded arguments and implementation here. 
#     '''
#     def wrapper(a,b,c):
#         t = a,b,c; flag = True
#         for i in t:
#             if i<0 or i>256:
#                 flag = False
#         if flag == True:
#             return fn(a,b,c)
#         else:
#             return "Function call is not valid!"
#     return wrapper
        

# @validate
# def set_pixel(x: int, y: int, z: int) -> str:
#     return "Pixel created!"


# print(set_pixel(256,256,257))

#Task 4

# def decorator_apply(lambda_func):
#     def overwrapper(fn):
#         def wrapper(n):
#             return lambda_func(n)
#         return wrapper
#     return overwrapper
   

# @decorator_apply(lambda user_id:user_id+1)
# def add(num):
#     return num

# print(add(42))

# x = 1 
# def foo(): 
#     x = 2 
#     def bar(): 
#         global x 
#         print(x) 
#     bar() 
# x = 3 
# foo() 

# def split(data: str, sep=None, maxsplit=-1)->list:
#     """
#     Add your code here or call it from here   
#     """
#     temps = ''; templ = []
#     data = data.replace(sep,' ')
#     for d in data:
#         if d.isspace():
#             continue
#         templ.append(d)
#     return templ
# print(split('aqbobal','b'))
s = 'adf<>adf<>adf<>adf'
print(s.split('<>'))
sep = '<>'
sl = []
i = None  # start of 'word'

for j, c in enumerate(s + ' '):
    if c == sep:
        if i is not None:
            sl.append(s[i:j])
            i = None
    else:
        if i is None:
            i = j
print(sl)

