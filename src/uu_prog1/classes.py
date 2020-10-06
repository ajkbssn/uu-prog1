
import random
import math
import matplotlib.pyplot as plt

class Ball:
    def __init__(self, win_sz, pos = None):
        self.win_sz = win_sz

        # Generate a random position, or store the argument-provided position
        if pos is None:
            self.pos = (random.randint(win_sz[0]), random.randint(win_sz[1]))
        else:
            self.pos = pos

        # Generate a random direction
        dir_radians = random.random() * 2 * math.pi

        self.dir = (math.sin(dir_radians), math.cos(dir_radians))


    def move(self, step):
        self.pos = (self.pos[0] + self.dir[0] * step, self.pos[1] + self.dir[1] * step)

        col = False
        if self.pos[0] < 0 and self.dir[0]<0:
            self.pos = (-self.pos[0], self.pos[1])
            self.dir = (-self.dir[0], self.dir[1])
            col = True
        if self.pos[1] < 0 and self.dir[1]<0:
            self.pos = (self.pos[0], -self.pos[1])
            self.dir = (self.dir[0], -self.dir[1])
            col = True
        if self.pos[0] > self.win_sz[0]-1 and self.dir[0]>0:
            self.pos = (2*(self.win_sz[0]-1)-self.pos[0], self.pos[1])
            self.dir = (-self.dir[0], self.dir[1])
            col = True
        if self.pos[1] > self.win_sz[1]-1 and self.dir[1]>0:
            self.pos = (self.pos[0], 2*(self.win_sz[1]-1)-self.pos[1])
            self.dir = (self.dir[0], -self.dir[1])
            col = True
        
        return col

    def __str__(self):
        return f'Ball(pos: {self.pos}, dir: {self.dir})'

    def show(self):
        plt.cla()
        plt.scatter(self.pos[1], self.pos[0])
        plt.xlim([0, self.win_sz[1]])
        plt.ylim([0, self.win_sz[0]])
        #plt.show()

a = Ball((100, 100), (20, 30))
sp = 15

for i in range(200):
    print(a)
    if a.move(sp):
        sp = sp * 0.9
    a.show()
    plt.pause(0.01)
plt.show()
