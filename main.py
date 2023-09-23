from turtle import*


pen()
speed(4000)
for i in range(180):
		forward(1)
		right(1)
left(90)
for i in range(180):
		forward(1)
		right(1)
left(90)
for i in range(180):
	forward(1)
	right(1)
left(90)
for i in range(180):
	forward(1)
	right(1)
penup()
for x in range(-5, 15):
	for y in range(-6, 16):
		setpos(x*11.5, y*11.5)
		dot(3)
done()