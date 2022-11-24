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
friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]

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
