import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

turtle.register_shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\loot-1.gif")
turtle.register_shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wall-1.gif")
turtle.register_shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wizzl-1.gif")
turtle.register_shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wizzr-1.gif")
turtle.register_shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\enemy.gif")
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wall-1.gif")
        # self.shape("square")
        # self.color("white")
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wizzr-1.gif")
        # self.shape("circle")
        # self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() -24
        move_to_y = self.ycor()
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wizzl-1.gif")
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\wizzr-1.gif")
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance <5:
            return True
        else:
            return False
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\loot-1.gif")
        # self.shape("turtle")
        # self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("E:\My Faculty\Computer Graphics Systems\Sections\Maze game\img\enemy.gif")
        # self.shape("triangle")
        # self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"   
            if player.xcor() > self.xcor():
                self.direction = "right"
            if player.ycor() < self.ycor():
                self.direction = "down"
            if player.ycor() > self.ycor():
                self.direction = "up"       
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        

        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])
        
        turtle.ontimer(self.move, t = random.randint(100,300))

    def is_close(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        if distance<75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

enemies = []
treasures = []
levels = [""]
level_1 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"O     OOOOO   OOOOOOOOOOO",
"OOOOO    OOOOO   OOOOOOOO",
"OOOOO    OOOOO   OOOOOOOO",
"OO                     EO",
"OO    P     OOOOO T OOOOO",
"OO          OOOOO  OO EOO",
"OOT            EO  OO  OO",
"OO          OOOOO  OO  OO",
"OO     OO   OOOOO  OO  OO",
"OO O   OO              OO",
"OO     OO     OOOOOOO  OO",
"OO O   OO    TOOOOOOO  OO",
"OOOOOOOOO   OOOOOOO O  OO",
"OOOOOOOOO        OOOOOOOO",
"O                     EOO",
"O  OO     OOOOOOOOO    OO",
"O  OO     OOO O  OO    OO",
"OO OO    TOOO    OO    OO",
"OOOOO   OOOOO          OO",
"OOOOO   OOOOO    OO   EOO",
"OOOOO              OOOOOO",
"OO      OOOOOO     OOOOOO",
"OOOO    OOOOOO   T  O OOO",
"OOOOOOOOOOOOOOOOOOOOOOOOO"
]

walls = []

levels.append(level_1)

pen = Pen()
player = Player()
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + ( x * 24)
            screen_y = 288 - ( y * 24)

            if character == "O":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character == "P":
                player.goto(screen_x,screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))
            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))
setup_maze(levels[1])
turtle.listen()
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")
turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")

wn.tracer(0)
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            turtle.penup()
            turtle.hideturtle()
            turtle.color("orange")
            turtle.goto(-80,300)
            turtle.clear()
            turtle.write("Gold({})".format(player.gold), True, "left",["arial", 30, "italic",])
            treasure.destroy()
            treasures.remove(treasure)
            if treasures == []:
                turtle.goto(0,0)
                turtle.write("You win", True, "center",["arial", 60, "italic","bold"])
                for enemy in enemies:
                    enemy.destroy()
                    enemies.remove(enemy)

    for enemy in enemies:
        if player.is_collision(enemy):
            turtle.penup()
            turtle.hideturtle()
            turtle.color("red")
            turtle.goto(0,0)
            turtle.write("Game over", True, "center",["arial", 60, "italic","bold"])
            player.destroy()

    wn.update()