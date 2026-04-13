from gpiozero import LED,Button
from time import sleep , time
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

left_point=0
right_point=0

def pressed(button):
	global left_point,right_point,start_time
	pressed_time = time()
	reaction_time = round((pressed_time - start_time) * 1000 , 2)
	if button.pin.number ==14:
		print(left_name + ' won the game')
		left_point+=1
	else:
		print(right_name + ' won the game')      
		right_point+=1
	print('left_point ' + str(left_point) + ' right_point ' + str(right_point))
	print('reaction time: '+str(reaction_time))
	led.on()
	sleep(uniform(5,10))
	led.off()
	start_time = time()
  
right_button.when_pressed = pressed
left_button.when_pressed = pressed
print('left_point ' + str(left_point) + ' right_point ' + str(right_point))
led.on()
sleep(uniform(5,10))
led.off()
start_time = time()

while(left_point<=5 and right_point<=5):
	sleep(0.01)


