
import pgzrun
import random

HEIGHT = 600
WIDTH = 1200

WHITE = (255,255,255)
BLUE = (0,0,100)

bulletsL = []
enemiesL = []
isGameover = False
direction = 1
score = 0
speed = 5
player = Actor("player2")
player.pos = (WIDTH//2, HEIGHT - 55)

for x in range(8):
    for y in range(4):
        enemiesL.append(Actor("enemy2"))
        enemiesL[-1].x = 100 + 80 * x
        enemiesL[-1].y = 50 + 80 * y

def draw():
    screen.clear()
    screen.fill(BLUE)
    player.draw()
    for bullet in bulletsL:
        bullet.draw()
    for enemy in enemiesL:
        enemy.draw()
    if len(enemiesL) == 0:
        gameover()


def on_key_down(key):
    if key == keys.SPACE:
        #bullet = Actor("bullet")
        bulletsL.append(Actor("bullet"))
        bulletsL[-1].x = player.x
        bulletsL[-1].y = player.y - 50

def displayScore():
    screen.draw.text(f"Score = {score}", fontsize = 20, color = "white", pos = (50,550))

def gameover():
    global isGameover
    screen.draw.text("Game Over!", fontsize = 40, color = "white", pos = (WIDTH//2 - 50, HEIGHT//2))
    isGameover = True

def update():
    global direction, score
    if not isGameover:
        moveDown = False
        if keyboard.left:
            player.x -= speed
            if player.x <= 25:
                player.x = 25
        if keyboard.right:
            player.x += speed
            if player.x > WIDTH - 25:
                player.x = WIDTH - 25
        for bullet in bulletsL:
            if bullet.y <= 0:
                bulletsL.remove(bullet)
            else:
                bullet.y -= 10
        if len(enemiesL) == 0:
            gameover()
        if len(enemiesL) > 0 and (enemiesL[-1].x > WIDTH - 50 or enemiesL[0].x < 50):
            moveDown = True
            direction = direction * -1
        for enemy in enemiesL:
            enemy.x += 5 * direction
            if moveDown == True:
                enemy.y += 50
            if enemy.y > HEIGHT:
                enemiesL.remove(enemy)
            for bullet in bulletsL:
                if bullet.colliderect(enemy):
                    score += 10
                    bulletsL.remove(bullet)
                    enemiesL.remove(enemy)
                    if len(enemiesL) == 0:
                        gameover()
            if enemy.colliderect(player):
                gameover()

pgzrun.go()