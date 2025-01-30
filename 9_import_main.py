# import my_mod as m
# from my_mod import find_index
from my_mod import *
import sys

list_str = ['abcd','dacb','bcad','cbda']

for str in list_str:
	print(find_index(str,'a'))

print(sys.path)	