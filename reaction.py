from gpiozero import LED,Button
from time import sleep , time
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

led.on()
sleep(uniform(5,10))
led.off()
start_time = time()

def pressed(button):
	pressed_time = time()
	reaction_time = round((pressed_time - start_time) * 1000 , 2)
	if button.pin.number ==14:
		print(left_name + 'won the game')
	else:
		print(right_name + 'won the game')
	exit()
right_button.when_pressed = pressed
left_button.when_pressed = pressed
