import functools
import operator
# define the binary trans
# def int2(x, base = 2):
#     return int(x, base)
int2 = functools.partial(int, base = 2)
sorted_ignore_case = functools.partial(sorted, cmp = lambda s1, s2: cmp(s1.upper(), s2.upper()))
print(int2('101010'))     
print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))