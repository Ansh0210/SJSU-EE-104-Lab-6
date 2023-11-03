# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:07:12 2023

@author: EK
"""

# Import libraries
import pgzrun
from pygame.locals import Rect

# Screen size in pixels
WIDTH = 1280
HEIGHT = 720

# Create box for interface
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

# Move the boxes
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

# Create a list of answer boxes
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

# Set the score
score = 0

# Set the timer
time_left = 15

# Questions
q1 = ["1. What is the unit of electrical resistance?", 
      "Ampere (A)", "Ohm (Ω)", "Volt (V)", "Watt (W)", 2]

q2 = ["2. What does AC stand for in the context of electrical circuits?", 
      "Alternating Current", "Active Circuit", "Analog Circuit", "Amplitude Control", 1]

q3 = ["3. Which component is used to store electrical energy in a circuit?", 
      "Resistor", "Diode", "Inductor", "Capacitor", 4]

q4 = ["4. What is the SI unit of electric charge?", 
      "Volt (V)", "Ampere (A)", "Coulomb (C)", "Ohm (Ω)", 3]

q5 = ["5. Which semiconductor device allows current to flow in one direction only?", 
      "Transistor", "Diode", "Capacitor", "Inductor", 2]

q6 = ["6. Which law states that the total current entering a junction is equal to the total current leaving the junction in a closed loop circuit?", 
      "Ohm's Law", "Faraday's Law", "Kirchhoff's Voltage Law", "Kirchhoff's Current Law", 4]

q7 = ["7. What is the function of a rectifier in a power supply circuit?", 
      "To convert AC to DC", "To regulate voltage", "To amplify signals", "To store electrical energy", 1]

q8 = ["8. What is the primary function of a relay in an electrical circuit?", 
      "To amplify signals", "To store electrical energy", "To switch high-voltage circuits", "To measure current", 3]

# List for questions
questions = [q1, q2, q3, q4, q5, q6, q7, q8]
question = questions.pop(0)

# Draw the boxes
def draw():
    screen.fill("slate blue")
    screen.draw.filled_rect(main_box, "black")
    screen.draw.filled_rect(timer_box, "black")
    
    for box in answer_boxes:
        screen.draw.filled_rect(box, "black")
        
    screen.draw.textbox(str(time_left), timer_box, color=("red"))
    screen.draw.textbox(question[0], main_box, color=("white"))
    
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("orange"))
        index = index + 1

# Set up final screen
def game_over():
    global question, time_left
    message = "Game over! Your score is %s/8." % str(score)
    question = [message, "~", "~", "~", "~", 5]
    time_left = "Time's Up"

# Correct answers
def correct_answer():
    global question, score, time_left
    
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 15
    else:
        print("End of questions")
        game_over()
        
#Answering questions
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1

# Update the timer
def update_time_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

# Take the hint
def on_key_up(key):
    global score
    if key == keys.H:
        print("Hint: correct answer is box #%s " % question[5])

clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()


