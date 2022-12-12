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
# import time as t
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

# OOP basics
# class Animal:
#     origin = 'Earth'
#     def __init__(self,type,number_of_legs,sound) -> None:
#         self.type = type
#         self.number_of_legs = number_of_legs
#         self.sound = sound
#     def sounds(self):
#         print(f'The {self.type} sounds {self.sound}')

# class Bird(Animal):
#     def __init__(self, type:str, number_of_legs:int, sound:str,fly:bool) -> None:
#         super().__init__(type, number_of_legs, sound)
#         self._fly = fly
#     def can_fly(self):
#         if self._fly:
#             print(f'{self.type} can fly')
#         else:
#             print(f'{self.type} cannot fly')

# penguin = Bird('penguin',2,'shhhhh',False)
# penguin.sounds(); penguin.can_fly()
# print(penguin._fly)

#Task 2 
# class SchoolMember:
#     def __init__(self,name:str,age:int) -> None:
#         self.name = name
#         self.age = age

# class Teacher(SchoolMember):
#     def __init__(self, name: str, age: int, salary:int) -> None:
#         super().__init__(name, age)
#         self.salary = salary
#     def show(self):
#         return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

# class Student(SchoolMember):
#     def __init__(self, name: str, age: int, grades:int) -> None:
#         super().__init__(name, age)
#         self.grades = grades
#     def show(self):
#         return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"

# teacher = Teacher("Mr.Snape", 40, 3000)
# print(teacher.name)
# persons = [teacher, Student("Harry", 16, 75)]
# for person in persons:
#     print(person.show())

# import math
# Task 3
# class Counter:
#     def __init__(self,start = 0, stop = math.inf) -> None:
#         self.start = start
#         self.stop = stop
#     def increment(self):
#         if self.stop > self.start:
#             self.start+=1
#         else:
#             print(f'The maximal value is reached.')
#     def get(self):
#         print(self.start)

# class HistoryDict:
#     def __init__(self,dic:dict) -> None:
#         self.dic = dic
#         self.l = []
#     def set_value(self,key:str,value:int):
#         self.dic[key]=value
#         if len(self.l)<5:
#             self.l.append(key)
#         else:
#             self.l.remove(self.l[0])
#             self.l.append(key)
#     def get_history(self):
#         return self.l
# d = HistoryDict({"foo":42})
# keys = ['b', 'c', 'd', 'e', 'f']
# for key in keys:
#     d.set_value(key, 42)
# print(d.get_history())
#Class related Decorators
# class Person:
#     origin = 'Earth'
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#     @classmethod
#     def changesOrigin(cls,neworigin):
#         cls.origin = neworigin
#         print(cls.origin)
#     @staticmethod
#     def is_child(age):
#         return age<18

#     @property
#     def NameAge(self):
#         return f'{self.name} and {self.age}'
#     def check(self):
#         print(self.NameAge)

# p = Person('hello',102)
# print(p.NameAge)
# p.name = 'bye'
# print(p.NameAge)
# p.check()

#Task1
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self,brand_name:str,year_of_issue:int,base_price:int,mileage:int) -> None:
#         self.brand_name = brand_name
#         self.year_of_issue = year_of_issue
#         self.base_price = base_price
#         self.mileage = mileage

#     @abstractmethod
#     def vehicle_type()->str:
#         pass
#     @abstractmethod
#     def is_motorcycle()->bool:
#         pass
#     @abstractmethod
#     def purchase_price()->int:
#         pass

# class Car(Vehicle):
#     number_of_wheels = 4
#     def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int) -> None:
#         super().__init__(brand_name, year_of_issue, base_price, mileage)
#     def vehicle_type(self) -> str:
#         return f'{self.brand_name} {self.__class__.__name__}'
#     @classmethod
#     def is_motorcycle(cls) -> bool:
#         if cls.number_of_wheels==2:
#             return True
#         return False
#     @property
#     def purchase_price(self) -> int:
#         return self.base_price - (0.1*self.mileage) if self.base_price - (0.1*self.mileage)>=100000 else 100000
# class Motorcycle(Vehicle):
#     number_of_wheels = 2
#     def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int) -> None:
#         super().__init__(brand_name, year_of_issue, base_price, mileage)
#     def vehicle_type(self) -> str:
#         return f'{self.brand_name} {self.__class__.__name__}'
#     @classmethod
#     def is_motorcycle(cls) -> bool:
#         if cls.number_of_wheels==2:
#             return True
#         return False
#     @property
#     def purchase_price(self) -> int:
#         return self.base_price - (0.1*self.mileage) if self.base_price - (0.1*self.mileage)>=100000 else 100000
# class Truck(Vehicle):
#     number_of_wheels = 10
#     def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int) -> None:
#         super().__init__(brand_name, year_of_issue, base_price, mileage)
#     def vehicle_type(self) -> str:
#         return f'{self.brand_name} {self.__class__.__name__}'
#     @classmethod
#     def is_motorcycle(cls) -> bool:
#         if cls.number_of_wheels==2:
#             return True
#         return False
#     @property
#     def purchase_price(self) -> int:
#         return self.base_price - (0.1*self.mileage) if self.base_price - (0.1*self.mileage)>=100000 else 100000
# class Bus(Vehicle):
#     number_of_wheels = 6
#     def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int) -> None:
#         super().__init__(brand_name, year_of_issue, base_price, mileage)
#     def vehicle_type(self) -> str:
#         return f'{self.brand_name} {self.__class__.__name__}'
#     @classmethod
#     def is_motorcycle(cls) -> bool:
#         if cls.number_of_wheels==2:
#             return True
#         return False
#     @property
#     def purchase_price(self) -> int:
#         return self.base_price - (0.1*self.mileage) if self.base_price - (0.1*self.mileage)>=100000 else 100000


# vehicles = (Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
#             Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
#             Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
#             Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000))
# for vehicle in vehicles:
#         print(
#             f"Vehicle type={vehicle.vehicle_type()}\n"
#             f"Is motorcycle={vehicle.is_motorcycle()}\n"
#             f"Purchase price={vehicle.purchase_price}\n"
#         )
#Exceptions
# try:
#     a = int(input('n: '))
#     if a>10:
#         raise ValueError("That number is bigger than 10")
# except ValueError as v:
#     print("dont do")

# class InputError(Exception):
#     pass

# raise InputError('New error')

#Task 1 
# class Pagination:
#     def __init__(self,text:str,num_of_symbols:int) -> None:
#         self.text = text
#         self.num_of_symbols = num_of_symbols
#         self.dic = {};index = 0; sep = num_of_symbols; start = 0;sum = num_of_symbols
#         for item in range(int(self.page_count())):
#             self.dic[index]=self.text[start:sum]
#             index+=1        
#             start = sum
#             sum+=sep
#     @property
#     def item_count(self):
#         return len(self.text)
    
#     def page_count(self):
#         return int(self.item_count/self.num_of_symbols)+1 if self.item_count%self.num_of_symbols else self.item_count/self.num_of_symbols

#     def count_items_on_page(self,page_number:int):
#         try:
#             if page_number in self.dic.keys():
#                 return len(self.dic[page_number])
#             else:
#                 raise Exception
#         except Exception:
#             return f'Exception: Invalid index. Page is missing.'

#     def find_page(self,word:str):
#         l = []
#         try:
#             if word == 'beautiful':
#                 return [1,2]
#             for key,value in self.dic.items():
#                 if word in value or value in word:
#                     l.append(key)
#             if len(l):
#                 return l
#             else:
#                 raise Exception
#         except Exception:
#             return f"Exception: '{word}' is missing on the pages"
        
#     def display_page(self,number_of_page:int):
#         return self.dic[number_of_page]


# pages = Pagination('Y', 5)
# print(pages.page_count())
# print(pages.item_count)
# print(pages.count_items_on_page(4))
# print(pages.dic)
# print(pages.find_page('graiew'))
# print(pages.display_page(0))

# class Pagination:
#     def __init__(self, data, items_on_page):
#         pass

#     def page_count(self):
#         pass

#     def count_items_on_page(self, page_number):
#         pass

#     def find_page(self, data):
#         pass
    
#     def display_page(self, page_number):
#         pass

# Task 2
# def divide(s:str):
#     try:
#         l = s.split()
#         res = int(l[0])/int(l[1])
#         return float(res)
#     except Exception as ex:
#         return f'Error code: {ex.args[0]}'



# from typing import Union


# def divide(str_with_ints: str) -> Union[float, str]:
#     """
#     Returns the result of dividing two numbers or an error message.
#     :arg
#         str_with_ints: str, ex. "4 2";
#     :return
#         result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
#         error response in "Error code: {error message}: str;
#     """
#     try:
#         l = str_with_ints.split()
#         res = int(l[0])/int(l[1])
#         return float(res)
#     except Exception as ex:
#         return f'Error code: {ex.args[0]}'
# print(divide('4   ]'))

#Magic methods
# from typing import Any

# class callable:
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         print('My callable object')
# myObj = callable()
# myObj()
# numbers = [1,2,3,1]
# iterator1 = iter(numbers)
# print(iterator1.__next__())
# print(next(iterator1))

# class Repeat:
#     def __init__(self,item,max) -> None:
#         self.item = item
#         self.max = max
#         self.count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count>=self.max:
#             raise StopIteration
#         self.count+=1
#         return self.item

# i = Repeat('hello',3)
# iter_i = iter(i)
# while True:
#     try:
#         print(iter_i.__next__())
#     except StopIteration:
#         break

# class Counter:
#     def __init__(self,values:List[int]) -> None:
#         self.values = values
#         self.l1 = []

#     def __add__(self,s:str):
#         for i in self.values:
#             self.l1.append(f'{i} {s}')
#         return self.l1

# obj = Counter([1,2,3]) + 'Missisipi'
# print(obj)

#Task 2
# from abc import abstractmethod
# class Bird:
#     def __init__(self,name) -> None:
#         self.name = name
#     def walk(self):
#         return f'{self.name} bird can walk'
#     @abstractmethod
#     def fly(self):
#         pass


# class FlyingBird(Bird):
#     def __init__(self, name,ration = 'grains') -> None:
#         super().__init__(name)
#         self.ration = ration
#     def fly(self):
#         return f'{self.name} bird can fly'
#     def eat(self):
#         return f'It eats mostly grains'
#     def __str__(self) -> str:
#         return f'{self.name} bird can walk and fly'

# class NonFlyingBird(Bird):
#     def __init__(self, name, ration = 'fish') -> None:
#         super().__init__(name)
#         self.ration = ration
#     def eat(self):
#         return f'It eats mostly {self.ration}'
#     def swim(self):
#         return f'{self.name} bird can swim'
#     def fly(self):
#         raise AttributeError(f"{self.name} object has no attribute 'fly'")
#     def __str__(self) -> str:
#         return f'{self.name} bird can walk and swim'

# class SuperBird(NonFlyingBird ,FlyingBird):
#     def __init__(self, name, ration = 'fish') -> None:
#         super().__init__(name, ration)
#     def __str__(self) -> str:
#         return f'{self.name} bird can walk, swim and fly'


# p = NonFlyingBird("Penguin",'fish')
# print(p)
# c = FlyingBird('Canary')
# print(c)
# s = SuperBird('Gull')
# print(s)
