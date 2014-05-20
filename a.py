#Google нашел что число скобочных выражений является числом Каталана. Подставим формулу - получим ответ
from math import factorial
n = int(raw_input())
if n==0 or n%2==1:
	print 0
else:
	print factorial(n) // factorial(n/2 + 1) // factorial(n/2)