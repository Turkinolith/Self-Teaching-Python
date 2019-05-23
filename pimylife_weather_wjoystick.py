from sense_hat import SenseHat
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640,480))

sense = SenseHat()
sense.clear()

scroll = scroll_speed=(0.08)
backcolor = back_colour=[0,0,0]
tcolor = text_colour=[200,0,200]

temp = round(sense.get_temperature())
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())

def handle_event(event):
    if event.key == pygame.K_DOWN:
        sense.show_message("Temp:" + str(temp) + "C", scroll, tcolor, backcolor)
    elif event.key == pygame.K_UP:
        sense.show_message("Humidity:" + str(humidity) + "%", scroll, tcolor, backcolor)
    elif event.key == pygame.K_RIGHT:
        sense.show_message("Pressure:" + str(pressure) + "mb", scroll, tcolor, backcolor)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            handle_event(event)
        if event.type == KEYUP:
            temp = round(sense.get_temperature())
            humidity = round(sense.get_humidity())
            pressure = round(sense.get_pressure())
            sense.clear()

sense.clear()
