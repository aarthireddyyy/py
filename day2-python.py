long_wided_computation = (1+2+3+4+5+6+7+8+9+10+11+12+13)
print(long_wided_computation)

listoflists= [[1,2,3],[2,3,4],[3,4,5]]
print(listoflists)
listoflists= [[1,2,3],
              [2,3,4],
              [3,4,5]]
print(listoflists)
for i in [1,2,3,4,5]:

    print(i) 
#STRINGS
single_q='hey'
double_q= "heyy"
print(single_q, double_q)

tab_string = "\t"
print(len(tab_string))

tab_string = r"\t"
print(len(tab_string))

multi = """Thiis a dlsfjn
dlafj
sdfjnc"""
print(multi)

#LISTS
integer_list = [1,2,3,4,5]
hetero_list = ["string", 0.34, 234]
lol=[integer_list, [], []]
list_length = len(integer_list)
list_sum = sum(integer_list)
print(integer_list)
print(lol)
print(list_length)
print(list_sum)

x = [0,1,2,3,4,5,6,7,8,9]
zero = x[0]
one = x[1]
print(x)
print(x[:3])
print(x[3:])
print(x[1:5])
print(x[:])

print(1 in [1,2,3])
print(0 in range(1,7))

x = [1,2,3]
x.extend([2,3,4])
print(x)
x.append(8)
print(x)

#TUPLE
my_list = [1,2,3]
my_tuple = (1,2)
tup = 3,4
try:
    my_list[1] = 3
except TypeError:
    print("cannot modify a tuple")
print(my_list)

#DICT
document = "hello greet meet hello".split()
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

#COUNTER
document = "ge ge ge heh heh hi nj ko lo".split
from collections import Counter
c  = Counter([34,23,32,44])
word_counts = Counter(document)
for word, count in word_counts.most_common(10):
    print(word, count)

#SETS 
s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)
print(len(s))

#CONTROL FLOW 
if 1 > 2:
    print("fasle")
else:
    print("true")

x = 20
parity = "even" if x % 2 == 0 else "odd"
print(parity)

x = 20 
while x > 0:
    print(x)
    x += 1

# SORTING
x = [-4,23,34,22,-67,34,-9]
y = sorted(x)
print(y)
x.sort()
print(x)

#LIST COMPREHENSIONS

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_square = [x * x for x in even_numbers]
print(even_numbers, squares, even_square)

squared={ x : x *  x for x in range(10)}
squareds={ x * x for x in [1, -1]}
print(squared, squareds)

pairs = [(x,y) 
        for x in range(1)
        for y in range(10)]
print(pairs)

#GENERATORS , ITERATORS
def lazy_range(n):
    """a lazy version of range"""
    i = 0 
    while i < n:
        yield i 
        i += 1
for num in lazy_range(6):
    print(num)


