
import random
import copy
import matplotlib.pyplot as plt

random.seed(1000)

class Diffuser:
    def __init__(self, n, dots, dotstrength=0):
        self.n = n

        # Create a 2d list of lists, with zeros
        self.field = [[0]*n for _ in range(n)]

        for _ in range(dots):
            y = random.randint(0, n-1)
            x = random.randint(0, n-1)
            amt = random.random() * dotstrength

            self.field[y][x] += amt

    def add_dot(self, x, y, amt):
        self.field[y][x] += amt
    
    def rotate(self):
        old_field = copy.deepcopy(self.field)

        for j in range(self.n):
            for i in range(self.n):
                self.field[j][i] = old_field[i][j]

    def smooth_horizontally(self):
        old_field = copy.deepcopy(self.field)

        for j in range(0, self.n):
            slc = old_field[j][0:2]
            self.field[j][0] = sum(slc)/len(slc)

            for i in range(1, self.n):
                slc = old_field[j][i-1:i+2]
                self.field[j][i] = sum(slc)/len(slc)

    def smooth(self):
        self.smooth_horizontally()
        self.rotate()
        self.smooth_horizontally()
        self.rotate()

    
    def local_maxima(self):
        dres = Diffuser(self.n, 0)

        for i in range(1, self.n-1):
            for j in range(1, self.n-1):
                slc1 = self.field[i-1][j-1:j+2]
                slc2 = self.field[i][j-1:j+2]
                slc3 = self.field[i+1][j-1:j+2]

                nhood = slc1 + slc2 + slc3
                is_maxima = True
                for k in range(len(nhood)):
                    if nhood[k] > nhood[4]:
                        is_maxima = False
                
                if is_maxima:
                    dres.field[i][j] = 1.0

        return dres
                
    def copy(self):
        dres = Diffuser(self.n, 0)

        for i in range(0, self.n):
            for j in range(0, self.n):
                dres.field[i][j] = self.field[i][j]

        return dres

    def show(self, do_show=False, normalized=True):
        if normalized:
            plt.imshow(self.field)
        else:
            plt.imshow(self.field, vmin=0, vmax=1.0)
        if do_show:
            plt.show()

    def show_comparison(self, other):
        fig, (ax1, ax2) = plt.subplots(1, 2)

        ax1.imshow(self.field)
        ax2.imshow(other.field)
        plt.show()

    def __str__(self):
        s = ''
        
        for i in range(0, self.n):
            for j in range(0, self.n):
                s += f'{self.field[i][j]:0.3f} '
            s += '\n'
        
        return s

d1 = Diffuser(100, 70, 14)
d1_copy = d1.copy()

d1.show(normalized=True)
for it in range(25):
    d1.smooth()
    d1.add_dot(random.randint(0, 99), random.randint(0, 99), random.random() * 6)
    plt.gcf()
    d1.show(normalized=False)
    plt.title(f'{it+1}')
    plt.pause(0.1)
plt.show()    

d1_copy1 = d1.copy()

for it in range(75):
    d1.smooth()
    for _ in range(20):
        d1.add_dot(random.randint(0, 99), random.randint(0, 99), random.random()*6)
    plt.gcf()
    d1.show(normalized=False)
    plt.title(f'{it+1}')
    plt.pause(0.1)
plt.show()
d1_copy1.show_comparison(d1)

dmax = d1.local_maxima()
d1_copy.show_comparison(dmax)

small_d = Diffuser(10, 15, 7)
for _ in range(10):
    small_d.smooth()
s = str(small_d)
print(s)
#dmax.show()
#d1_copy.show()