# Smarter solutions require acute observation of the specific problem
# I lingered around the given of "battleships must be one vert and horizontal space apart"
# but did not come up with an idea

# Turns out, we can write the following simple logic with this fact:
# If we come across X, check if there is a X above and if there is a X to the left
# If not, we count this X

# The core of this logic avoids battleship double counting: Every battleship
# has either a highest cell or a leftmost cell. The check in the previous paragraph
# ensures that we only count the highest cell or leftmost cell as battleship
# Additionally, this check is never not going to miss count. If battleships can be
# adjacent, we run into the case where, when we in fact on a top/left corner of a battleship,
# we detect the cell one higher or the cell one to the left to have a battelship
from functools import reduce
from itertools import product
import operator


a = product(range(3), range(4))
# print(next(a))


def unpack(run):
    def runner(packed):
        return run(*packed)
    return runner


a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
c = [3, 4, 5, 6]

# d = list(map(unpack(lambda x, y, z: x + y + z),
#          product(a, b, c)))
# print(d)


# # result should same row len
# print(reduce(operator.add, *zip(*product(a, b, c)) , 0))

# zip([1, 2, 3], [3, 4, 5]) => (1, 3) => (2, 4) => (3, 5)
# in other words, list(zip([1, 2, 3], [3, 4, 5])) = [(1, 3), (2, 4), (3, 5)]
# So, the first element passed into map's func is (1, 3)

print(list(map(lambda x, y: x + y, *zip([1, 2, 3], [3, 4, 5]))))
# print(list(product(a, b, c)))  # 64 arguments

zp = zip(*product(a, b, c))
# print([*next(zp)], next(zp), next(zp))

# for a in zip(*product(a, b, c)):
    # print(a)
def largestLocal 