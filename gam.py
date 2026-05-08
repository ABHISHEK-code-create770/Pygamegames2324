import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
font = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

def welcome():
    bgi=pygame.image.load("home.png")
    bgi=pygame.transform.scale(bgi,(800,600))
    waitin =True
    font1 = pygame.font.Font(None, 36)
    font = pygame.font.Font(None, 50)
    sound=pygame.mixer.Sound("home.mp3")
    sound.play()

    while waitin:
      
        # screen.fill((255,255,255))
        screen.blit(bgi,(0,0))
        text=font.render("WELCOME TO THE GAME",True,(170,170,170))
        start=font1.render("PRESS SPACE TO START",True,(170,170,170))
        credit=font1.render("BUILT BY ABHISHEK",True,(170,170,170))
        credit2=font1.render("NIT DURGAPUR CSE",True,(170,170,170))

        screen.blit(text,(200,250))
        screen.blit(start,(180,300))
        screen.blit(credit,(500,500))
        screen.blit(credit2,(500,550)) 
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_SPACE:
                     waitin=False
                     sound.stop()
                    
def end(mess="GAME OVER"):
    bgi=pygame.image.load("home.png")
    bgi=pygame.transform.scale(bgi,(800,600))
    waitin =True
    font1 = pygame.font.Font(None, 36)
    font = pygame.font.Font(None, 50)
    sound=pygame.mixer.Sound("home.mp3")

    while waitin:
      
        # screen.fill((255,255,255))
        screen.blit(bgi,(0,0))
        text=font.render(f"{mess}",True,(170,170,170))
       
        credit=font1.render("BUILT BY ABHISHEK",True,(170,170,170))
        credit2=font1.render("NIT DURGAPUR CSE",True,(170,170,170))

        screen.blit(text,(200,250))

        screen.blit(credit,(500,500))
        screen.blit(credit2,(500,550)) 
        sound.play()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_SPACE:
                     waitin=False
                     sound.fadeout(2000)
 


bgi=pygame.image.load("home.png")
bgi=pygame.transform.scale(bgi,(800,600))

clock = pygame.time.Clock()
BLACK = (50, 50, 50)
GRAY=(255,0,0)
WHITE = (255,255,255)
COL1=(255,100,250)
COL2=(101,67,33)

# Paddle
paddle_x = WIDTH // 2 - 60
paddle_y = HEIGHT - 40
paddle_width, paddle_height = 120, 20
paddle_speed = 15

# Ball
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 3, -3
ball_radius = 10
popsound=pygame.mixer.Sound("soundreality-pop-423717.mp3")

#BOULDERS

class Boulder:
    def __init__(self,x,y):
        self.image=pygame.image.load("image2.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(35,35))
        self.rect=self.image.get_rect(topleft=(x,y))

    def draw(self,screen):
        # pygame.draw.circle(screen,GRAY,self.rect.center,self.rect.width//2)
        screen.blit(self.image,self.rect)




score=0
boulders=[]

for j in range(40):
    x=random.randint(50,WIDTH-50)
    y=random.randint(50,300)
    boulders.append(Boulder(x,y))


welcome()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    if(score==40):
        end("CONGRATULATIONS:YOU WON")

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy
    ball_rect=pygame.Rect(ball_x-10,ball_y-10,20,20)

    # Wall bounces
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= ball_radius:
        ball_dy = -ball_dy
    if ball_y >= HEIGHT - ball_radius:
        # Reset ball if misses paddle
        running=False

    # Paddle collision (simple)
    if (paddle_y < ball_y + ball_radius < paddle_y + paddle_height and
        paddle_x - ball_radius < ball_x < paddle_x + paddle_width + ball_radius):
        popsound.play()
        ball_dy = -ball_dy

    #BOULDER COLLISION
    for boulder in boulders[:]:
        if ball_rect.colliderect(boulder.rect):
            score=score+1
            ball_dy=-ball_dy
            popsound.play() 
            boulders.remove(boulder)
            

    
    screen.blit(bgi,(0,0))
   
    pygame.draw.rect(screen,COL2, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, GRAY, (int(ball_x), int(ball_y)), ball_radius)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    for boulder in boulders:
        boulder.draw(screen)

    pygame.display.update()
    clock.tick(70)

end()


pygame.quit()
sys.exit()