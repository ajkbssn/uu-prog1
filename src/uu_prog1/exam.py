# src/uu_prog1/20201023_exam_CS_0035_XXU.py
# CS-0035-XXU
# Computer Programming I
# October 23, 2020
# A1 -------------------------------------------
"""
The code rolls a six side dice and prints the fibonacci number for the result.
I put the given script in a new function main_a1()
Modules:
random
Function definitions:
def fib(n):
Method definitions:
def roll(self):
(def __init__(self, nsides): constructors are methods of a special kind)
Function calls:
fib(d.value) is the only call of a function defined in the code, but there are also
other calls of functions
print(fib(d.value)) print is a function in python3 with special behaviour
range() in function fib() is a function returning a range object
random.randint(1, self.nsides) is a call of the function randint() in the module 
random
Method calls: 
d.roll()
Classes:
Dice
Variables:
f0, f1, fi in function fib()
Attributes:
nsides, value in objects of class Dice
Constructors:
__init__() in class Dice
Parameters:
n in def fib(n):
"""
import random
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for _ in range(2, n):
        fi = f0 + f1
        f0 = f1
        f1 = fi
    return f1
class Dice:
    def __init__(self, nsides):
        self.nsides = nsides
        self.value = 0
    def roll(self):
        self.value = random.randint(1, self.nsides)
def main_a():
    d = Dice(6)
    d.roll()
    print(fib(d.value))
# A2 -------------------------------------------
def alternating(s):
    """
    takes a string s and returns it with every other
    character uppercase and lowercase respectivly
    """
    new_s = ""
    for i, c in enumerate(s):
        new_s += c.lower() if i % 2 else c.upper()
    return new_s
# A3 -------------------------------------------
def predecessors(s):
    """
    takes a string s, splits the string into a list of words
    (splits where there is a whitespace) and returns a dict with 
    all the words in the string as lower case keys and 
    the list of predecessing words in lowercase as values
    """
    lst = s.split()
    dct = dict()
    for i, w in enumerate(lst):
        wl = w.lower()
        if wl in dct.keys():
            dct[wl].append(lst[i - 1].lower())
        elif i == 0:
            dct[wl] = [""]
        else:
            dct[wl] = [lst[i - 1].lower()]
    return dct
# A4 -------------------------------------------
def central_difference(lst):
    """
    takes a list of numbers lst (no type checking)
    and returns a new list of numbers with 
    computed central difference approximation
    """
    diff_lst = []
    for x in range(1, len(lst) - 1):
        diff_lst.append((lst[x + 1] - lst[x - 1]) / 2)
    return diff_lst
# A5 -------------------------------------------
def random_shuffle(lst):
    """
    takes a list of elements and returns a new list as output
    which contains all the elements in the original list but
    reordered at random
    """
    from numpy.random import permutation
    return [lst[i] for i in permutation(len(lst))]
# A6 -------------------------------------------
def test_random_shuffle(lst):
    """
    takes a list of elements as a parameter and aims to test the
    correctness of the function random_shuffle()
    """
    def orig_unchanged(lst, orig_lst):
        if len(lst) != len(orig_lst):
            return False
        else:
            for i in range(len(lst)):
                if lst[i] != orig_lst[i]:
                    return False
        return True
    def elems_preserved(lst, orig_lst):
        if len(lst) != len(orig_lst):
            return False
        # Test that elements in original list is in shuffled list
        for orig_elem in orig_lst:
            if orig_elem not in lst:
                return False
        # Test that elements in shuffled list is in original list
        for lst_elem in lst:
            if lst_elem not in orig_lst:
                return False
        return True
    orig_lst = lst.copy()
    shuf_lst = random_shuffle(lst)
    if len(lst) != len(shuf_lst):
        return False
    if not orig_unchanged(lst, orig_lst):
        return False
    if not elems_preserved(shuf_lst, lst):
        return False
    return True
# A7 -------------------------------------------
def draw_text_circle(r, n):
    from math import sqrt
    for y in range(-n, n + 1):
        for x in range(-n, n + 1):
            if round(sqrt(x ** 2 + y ** 2), 0) != r:
                print(".", end="")
            else:
                print("X", end="")
        print()
# A8 -------------------------------------------
class Clock:
    # no checking if created with invalid time or other than integers
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"
    # A9 -------------------------------------------
    def tick(self, n=1):
        self._addsec(n % 60)
        self._addmin(n // 60)
    def _addsec(self, n):
        self.s += n
        self._addmin(self.s // 60)
        self.s = self.s % 60
    def _addmin(self, n):
        self.m += n
        self._addhour(self.m // 60)
        self.m = self.m % 60
    def _addhour(self, n):
        self.h += n
        self.h = self.h % 24
# PART B -------------------------------------
class Maze:
    def __init__(self, n):
        self.a = [["X" for _ in range(n)] for _ in range(n)]
    def create_path_between(self, x1, y1, x2, y2):
        xc = x1
        yc = y1
        self.a[yc][xc] = " "
        while xc != x2 or yc != y2:
            if x2 > xc:
                xc += 1
            elif x2 < xc:
                xc -= 1
            if y2 > yc:
                yc += 1
            elif y2 < yc:
                yc -= 1
            self.a[yc][xc] = " "
    def create_exit(self, x, y):
        self.a[y][x] = "E"
    def get_neighbour(self, x, y):
        if x < 0 or y < 0 or x >= len(self.a) or y >= len(self.a):
            return (x, y, "X")
        else:
            return (x, y, self.a[y][x])
    # B1 -----------------------
    def get_neighbours(self, x, y):  # *** B1: get_neighbours
        nbor_lst = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i or j:  # pointing at own cell?
                    nbor_lst.append(self.get_neighbour(x + i, y + j))
        return nbor_lst
    def __str__(self):
        s = ""
        s += "X" * (len(self.a) + 2)
        s += "\n"
        for y in range(len(self.a)):
            s += "X"
            for x in range(len(self.a)):
                s += self.a[y][x]
            s += "X\n"
        s += "X" * (len(self.a) + 2)
        return s
# B2 -----------------------
class RandomMazeSolver:
    def __init__(self, x, y, mz):
        self.x = x
        self.y = y
        self.mz = mz
        self.path = [(x, y)]
    # B3 -----------------------
    def step(self):
        nbors = self.mz.get_neighbours(self.x, self.y)
        nbors = random_shuffle(nbors)
        n = 0
        while nbors[n][2] == "X":
            n += 1
        self.x = nbors[n][0]
        self.y = nbors[n][1]
        self.path.append((self.x, self.y))
        return nbors[n][2] == "E"
# B4 -----------------------------
# RecursionError: maximum recursion depth exceeded in comparison
def shorten_path_too_deep(pth):
    before_exit = pth[len(pth) - 2]
    for i, step in enumerate(pth):
        if i == len(pth) - 2:
            return pth
        if step == before_exit:
            return shorten_path(pth)
def shorten_path(pth):
    i = len(pth) - 1
    rev_pth = list(pth[i])
    while i > 0:
        j = 0
        while j < i:
            if pth[i] == pth[j]:
                rev_pth.append(pth[i])
                j = i - 1  # exit while j loop
            j += 1
        i = j - 1
    return rev_pth[::-1]
def main_b():
    mz = Maze(10)
    mz.create_path_between(0, 0, 9, 9)
    mz.create_path_between(1, 1, 7, 3)
    mz.create_path_between(7, 3, 5, 0)
    mz.create_path_between(7, 3, 8, 5)
    mz.create_path_between(8, 5, 7, 6)
    mz.create_path_between(0, 0, 0, 4)
    mz.create_path_between(0, 4, 4, 7)
    mz.create_path_between(4, 7, 0, 9)
    mz.create_path_between(0, 9, 0, 5)
    mz.create_exit(9, 9)
    print(mz)
    mz_solver = RandomMazeSolver(0, 0, mz)  # *** B2: RandomMazeSolver
    while mz_solver.step() == False:  # *** B3: step
        pass
    pth = mz_solver.path
    shrt_pth = shorten_path(pth)  # *** B4: shorten path
    print("Long path: ", pth, sep="")
    print("Short path: ", shrt_pth, sep="")
    print(f"Length of long path: {len(pth)}.")
    print(f"Length of short path: {len(shrt_pth)}.")
