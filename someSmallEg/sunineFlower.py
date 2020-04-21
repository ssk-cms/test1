from turtle import *

color('black','yellow')
begin_fill()

while True:

    forward(250)
    left(130)
    if abs(pos()) <1:
        break

end_fill()

done()