import random
import time

class Env:
    def __init__(self, num_of_cases, num_of_rocks_1, num_of_rocks_2, troll_pos):
        self.troll= Troll(troll_pos)
        self.castle_1= Castle(1, num_of_rocks_1)
        self.castle_2= Castle(2, num_of_rocks_2)
        self.current= 1
        self.num_of_cases= num_of_cases
        self.core_list= [0]* self.num_of_cases
        self.core_list[self.troll.position]= 'T'
        self.play_ground= [-1]+ self.core_list+ [1]
        self.null_pos= self.num_of_cases// 2

    def isFinished(self):
        return self.play_ground[0]== 'T' or self.play_ground[-1]== 'T' or self.castle_1.num_of_rocks== 0 or self.castle_2.num_of_rocks== 0
    
    def gameWinner(self):
        if self.isFinished():
            if self.play_ground[0]== 'T':
                return 1
            elif self.play_ground[-1]== 'T':
                return -1
            elif self.castle_1.num_of_rocks== 0 :
                for i in range(self.castle_2.num_of_rocks):
                    self.troll.moveLeft()
                    self.moveTroll()
                if self.troll.position== self.null_pos:
                    return 0
                return -1 if self.troll.position> self.null_pos else 1
            elif self.castle_2.num_of_rocks== 0 :
                for i in range(self.castle_1.num_of_rocks):
                    self.troll.moveRight()
                    self.moveTroll()
                if self.troll.position== self.null_pos:
                    return 0
                return -1 if self.troll.position> self.null_pos else 1
        else:
            return -1
    
    def roundWinner(self, s1, s2):
        if s1== s2:
            return 0
        return -1 if s1> s2 else 1

    def repositionTroll(self, w):
        if w== 0:
            return
        self.troll.moveRight() if w== -1 else self.troll.moveLeft()
        self.core_list= [0]* self.num_of_cases
        self.core_list[self.troll.position]= 'T'
        self.play_ground= [-1]+ self.core_list+ [1]
        
    def moveTroll(self):
        self.core_list= [0]* self.num_of_cases
        try:
            self.core_list[self.troll.position]= 'T'
        except:
            self.play_ground= [-1]+ self.core_list+ [1]
            if self.troll.position> self.null_pos:
                self.play_ground[-1]= 'T'  
            elif self.troll.position< self.null_pos:
                self.play_ground[0]= 'T'
            else:
                pass
            return
        self.play_ground= [-1]+ self.core_list+ [1]


    def simulateGame(self, s1, s2):
        r= 0
        print(f"-------------------------------------------- ROUND {r} ----------------------------------------------------")
        print((f"CASTLE_1 move: N/A, remaining rocks= {self.castle_1.num_of_rocks} || {self.play_ground} || CASTLE_2 move: N/A, remaining rocks= {self.castle_2.num_of_rocks}"))
        print()
        while not self.isFinished():
            r+= 1
            s1= self.castle_1.executeStrategy(s1)
            s2= self.castle_2.executeStrategy(s2)
            w= self.roundWinner(s1, s2)
            self.repositionTroll(w)
            print(f"-------------------------------------------- ROUND {r} ----------------------------------------------------")
            print(f"CASTLE_1 move: {s1}, remaining rocks= {self.castle_1.num_of_rocks} || {self.play_ground} || CASTLE_2 move: {s2}, remaining rocks= {self.castle_2.num_of_rocks}, ROUND WINNER: {w}")
            print()
        print("-------------------------------------------- GAME FINISHED ----------------------------------------------")
        w= self.gameWinner()
        print(f"FINAL GAME STATE: {self.play_ground}")
        print(f"WINNER: {w}")            

    def analyzeStrat(self, num_of_games, s1, s2):
        pass


class Troll:
    def __init__(self, position) -> None:
        self.position= position

    def moveRight(self):
        self.position+= 1

    def moveLeft(self):
        self.position-= 1

class Castle:
    def __init__(self, id, num_of_rocks) -> None:
        self.num_of_rocks= num_of_rocks
        self.id= id
    def throw(self, n):
        self.num_of_rocks-= n if n<= self.num_of_rocks else self.num_of_rocks

    def executeStrategy(self, s):
        if s== 'random100':
            num_of_rocks= random.randint(1, self.num_of_rocks)
            self.throw(num_of_rocks)
        elif s== 'random50':
            num_of_rocks= random.randint(1, self.num_of_rocks//2)
        return num_of_rocks




def trollOutcome(n, m, p, c):
    if isFinished(n, m, p, c):
        return None
    else:
        w= maxTroll(n, m, p, c)
    return w
    
def maxTroll(n, m, p, c, last_move= None):
    G= -9999999

    if isFinished(n, m, p, c):
        return gameWinner(m, n, p, c)

    
    for move in range(1, n+1):
        #display(n-move, m, p, c, move, last_move)
        g= minTroll(n-move, m, p, c, move) 
        if g> G:
            G= g
    return G


def minTroll(n, m, p, c, last_move= None):
    G= 9999999

    for move in range(1, m+1):
        if last_move != None:
            if last_move== move:
                g= maxTroll(n, m-move, p, c, move)
            elif last_move> move:
                g= maxTroll(n, m-move, p+1, c, move)
            else:
                g= maxTroll(n, m-move, p-1, c, move)

        #display(n, m-move, p, c, move, last_move)
        if g< G:
            G= g
        
    return G

def isFinished(n, m, p, c):
    return n==0 or m==0 or p==c-1 or p==-1*(c-1)
        

def gameWinner(n, m, p, c):
    if isFinished(n, m, p, c):
        if p == -1*(c-1):
            return -1
        elif p == c-1:
            return 1
        elif n== 0 :
            for i in range(m):
                p-= 1
            if p== 0:
                return 0
            return 1 if p> 0 else -1
        elif m== 0 :
            for i in range(n):
                p+= 1
            if p== 0:
                return 0
            return 1 if p> 0 else -1
    else:
        return -99
    
def display(n, m, p, c, m1, m2):
    l= [1] + [0 for x in range(c)] + [2]
    l[p+(c+2)//2]= 'T' 
    print(f"N: {n}, move: {m1}", l, f"M:{m}, move: {m2}")
    print(isFinished(n, m, p, c))
    print(gameWinner(n, m, p, c))


def generateSimplex(n, m, p, c):
    s = [[0]* n for _ in range(m)]
    for x in range(n):
        for y in range(m):
            s[y][x]= trollOutcome(x+1, y+1, p, c)

    return s
s= generateSimplex(5, 4, -1, 5)
print(s)

    