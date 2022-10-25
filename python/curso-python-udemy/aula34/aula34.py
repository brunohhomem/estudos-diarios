import sys
import time


# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
#
# for v in g:
#     print(v)

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

for v in l2:
    print(v)