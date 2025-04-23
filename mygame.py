import pygame
import os
from pygame.locals import *

# Setup display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Capstone 2")

# Initialize mixer for sound
pygame.mixer.init()

# Load sound effects (adjust file paths/names as needed)
try:
    sound_path = "C:/Users/brown/webContents/yes.wav/"
    yes_sound = pygame.mixer.Sound(os.path.join(sound_path, "yes.wav"))
    yes_sound = pygame.mixer.Sound("C:/Users/brown/webContents/yes.wav")  # Sound for 'Y' press
    no_sound = pygame.mixer.Sound("no.wav")    # Sound for 'N' press
    end_sound = pygame.mixer.Sound("end.wav")  # Sound for game end
except FileNotFoundError:
    print("Sound files not found. Place 'yes.wav', 'no.wav', and 'end.wav' in the same directory.")
    yes_sound = no_sound = end_sound = None  # Fallback if files are missing

# Choose a font to use in the game
myFont = pygame.font.SysFont('cambria', 12)

# Directions displayed throughout the game
directions = "Please press the 'Y' key for yes and the 'N' key for no."
restart_prompt = "Press 'R' to restart the game."

# Counts how many questions have been asked
currentQuestion = 0

# Determines which question to ask based on the player's answer and the current question number
def story(answer, count):
    screen.fill("white")
    if count == 0:
        question1(answer)
    elif count == 1:
        question2(answer)
    elif count == 2:
        question3(answer)
    elif count == 3:
        end(answer)

# Displays the introduction to the story and the first question
def intro():
    intro1 = "Once upon a time lived a brave hero named Anya."
    intro2 = "She lived a simple life in a small village, making biscuits for the village people."
    intro3 = "One day, late at night, she hears a loud noise outside the village."
    q1 = "Should she go outside to investigate? Yes or no?"
    screen.fill("white")
    textSurface = myFont.render(intro1, True, "black")
    screen.blit(textSurface, (10, 10))
    textSurface = myFont.render(intro2, True, "black")
    screen.blit(textSurface, (10, 50))
    textSurface = myFont.render(intro3, True, "black")
    screen.blit(textSurface, (10, 90))
    textSurface = myFont.render(q1, True, "black")
    screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 170))

# Checks the answer provided to the first question and displays the second question
def question1(answer):
    screen.fill("white")
    if answer == K_y:
        yes1 = "She ventures into the dark, prepared for danger."
        yes2 = "Eventually, she sees an army of ogres coming toward her village!"
        q2 = "Should she fight the ogres? Yes or no?"
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 90))
    elif answer == K_n:
        no1 = "She chooses the safety of her home and stays inside."
        no2 = "However, the sounds do not go away."
        no3 = "She can tell something is very wrong..."
        no4 = "Eventually, she sees an army of ogres coming toward her village!"
        q2 = "Should she fight the ogres? Yes or no?"
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 90))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 170))

# Checks the answer provided to the second question and displays the third question
def question2(answer):
    screen.fill("white")
    if answer == K_y:
        yes1 = "She bravely confronts the ogres, hoping to protect her village from harm."
        q3 = "Should Anya risk her life to retrieve the sword from the Ancient Forest? Yes or no?"
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
    elif answer == K_n:
        no1 = "The ogres raid the village but Anya manages to escape with her life."
        story2 = "The ogres decide to leave but she knows they will be back."
        story3 = "Anya decides to talk with a village elder about what she should do."
        story4 = "The elder says there is a powerful sword hidden in the Ancient Forest."
        q3 = "Should Anya risk her life to retrieve it? Yes or no?"
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(story2, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(story3, True, "black")
        screen.blit(textSurface, (10, 90))
        textSurface = myFont.render(story4, True, "black")
        screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(q3, True, "black")
    screen.blit(textSurface, (10, 170))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 210))

# Checks the answer provided to the third question and displays the fourth question
def question3(answer):
    screen.fill("white")
    if answer == K_y:
        yes1 = "Although Anya almost died in the Ancient Forest, she returns with the Sword of Legends!"
        yes2 = "In the dead of winter, the ogres come back. This time they are led by their evil king."
        q4 = "Should Anya fight the ogre king now that she has the Sword of Legends? Yes or no?"
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 50))
    elif answer == K_n:
        no1 = "Anya decides it's too risky to go into the forest alone."
        no2 = "She hopes for the best with the weapons she has."
        no3 = "In the dead of winter, the ogres come back."
        no4 = "This time they are led by their evil king."
        q4 = "Should Anya fight the king even though she doesn't have the Sword of Legends? Yes or no?"
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 90))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(q4, True, "black")
    screen.blit(textSurface, (10, 170))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 210))

# Displays the ending based on the answer to the fourth question
def end(answer):
    screen.fill("white")
    if answer == K_y:
        yes1 = "Tension fills the air as she prepares to fight the king. The duel commences..."
        end1 = "After an intense battle, Anya strikes the final blow!"
        end2 = "The king surrenders and pleads for mercy."
        end3 = "Anya is a true hero, who shows mercy to the king."
        end4 = "This act of kindness warms the evil king's heart,"
        end5 = "who promises to leave the village alone for eternity."
        end6 = "The end!"
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 90))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 170))
        textSurface = myFont.render(end5, True, "black")
        screen.blit(textSurface, (10, 210))
        textSurface = myFont.render(end6, True, "black")
        screen.blit(textSurface, (10, 250))
    elif answer == K_n:
        no1 = "Anya refuses to duel the king, who laughs at her cowardice."
        end1 = "This buys some time for the villagers to escape."
        end2 = "Sadly, the ogre king takes over Anya's village."
        end3 = "She is just thankful that the villagers were able to get to safety."
        end4 = "The end!"
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 50))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 90))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 170))
    # Add restart prompt
    textSurface = myFont.render(restart_prompt, True, "black")
    screen.blit(textSurface, (10, 290))
    if end_sound:
        end_sound.play()

# Game loop
running = True
while running:
    # Check for events
    for currentEvent in pygame.event.get():
        if currentEvent.type == QUIT:
            running = False
        elif currentEvent.type == KEYDOWN:
            if currentQuestion == 0:
                if currentEvent.key == K_y and yes_sound:
                    yes_sound.play()
                elif currentEvent.key == K_n and no_sound:
                    no_sound.play()
                story(currentEvent.key, currentQuestion)
                currentQuestion += 1
            elif currentQuestion < 4:
                if currentEvent.key == K_y and yes_sound:
                    yes_sound.play()
                elif currentEvent.key == K_n and no_sound:
                    no_sound.play()
                story(currentEvent.key, currentQuestion)
                currentQuestion += 1
            elif currentQuestion == 4 and currentEvent.key == K_r:
                # Restart the game
                currentQuestion = 0
                intro()

    # Show intro screen at the start
    if currentQuestion == 0:
        intro()

    # Update the display every frame
    pygame.display.update()

pygame.quit()