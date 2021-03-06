class Point:
    row=0
    col=0
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def copy(self):
        return Point(self.row,self.col)


import pygame
import random   # for random number generation
pygame.init()
W=800
H=600
ROW=30
COL=40
size=(W,H)

bg_color=(255,255,255)
window=pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇")
head=Point(row=ROW//2,col=COL//2)
head_color=(0,128,128)
food_color=(255,255,0)
body_color=(200,200,200)
snakes=[Point(row=head.row,col=head.col+1),Point(row=head.row,col=head.col+2),Point(row=head.row,col=head.col+3)]
def generate_food():
    food=Point(random.randint(0,ROW-1),random.randint(0,COL-1))

    while food in snakes or food==head:
        food=Point(random.randint(0,ROW-1),random.randint(0,COL-1))
    return food
food=generate_food()

def rect(point,color):
    left=point.col*W//COL
    top=point.row*H//ROW
    pygame.draw.rect(window,color,(left,top,W//COL,H//ROW))
quit=False
clock=pygame.time.Clock()
direction="right"
while not quit:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key==pygame.K_a and direction!="right" :
                direction="left"
            elif event.key==pygame.K_RIGHT or event.key==pygame.K_d and direction!="left":
                direction="right"
            elif event.key==pygame.K_UP or event.key==pygame.K_w    and direction!="down":
                direction="up"
            elif event.key==pygame.K_DOWN or event.key==pygame.K_s   and direction!="up":
                direction="down"
    eat=(head.row==food.row and head.col==food.col)
    if eat:
        food=Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
    snakes.insert(0,head.copy())
    if not eat:
        snakes.pop()
    if direction=="right":
        head.col+=1
    elif direction=="left":
        head.col-=1
    elif direction=="up":
        head.row-=1
    elif direction=="down":
        head.row+=1
    if head.row<0 or head.row>=ROW or head.col<0 or head.col>=COL:
        quit=True
    if head in snakes:
        quit=True
    if quit==True:
        print("Game Over")
    ### 绘制图像
    pygame.draw.rect(window,bg_color,(0,0,W,H))
    for snake in snakes:
        rect(snake,body_color)
    rect(head,head_color)
    rect(food,food_color)
    pygame.display.flip()

    clock.tick(20)