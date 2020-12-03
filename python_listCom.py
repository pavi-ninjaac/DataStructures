# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:27:10 2020

@author: ninjaac
"""


print(hash('a'))
print(hash('aa'))
print(hash([1,2])) # there is no hash function for list , dict can be used for string number tuple
#that is immmutable datatypes

#basic list comprihention
n=[1,5,3]
a=[1,3]
b=[5]
c=sum([(i in a) - (i in b) for i in n])


#ordered list and groupby




store_item = dict()
for _ in range(int(input())):
    key,a,value = input().rpartition(" ")
    print(key,a,value)
    store_item[key] = store_item.get(key,0) + int(value)
for k,v in store_item.items():
    print(k,v)
    

#collections namedtuple
    
from collections import namedtuple
n = int(input('enter the number'))
mark = 0
for i in range(n+1):
    print(i)
    if i==0: Stu = namedtuple('Stu',input().split())
    else:
        f1,f2,f3,f4 = input().split()
        s=Stu(f1,f2,f3,f4)
        mark += int(s.MARKS)
print('{:.2f}'.format(mark/n))
   

#Exception handling

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error code:",e)
    except ValueError as e:
        print("Error code:",e)
    finally:
        print("Finished")
    
#combinations and permutations
from itertools import combinations,permutations
a=[1,2,3]
print(list(combinations(a,2)))
print(list(permutations(a,2)))

#find the combinationn of words
s,r=input().split()
for i in range(1,int(r)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))

