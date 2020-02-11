from display import *

#d0 is pixel to the up-right
#d1 if pixel to the right

# octants 1 and 5 : 0 < m < 1
# octants 2 and 6 : 1 < m < undefined
# octants 3 and 7 : undefined < m < -1
# octants 4 and 8 : -1 < m < 0

def draw_line( x0, y0, x1, y1, screen, color ):
    currentx = x0
    currenty = y0
    slope = (y1-y0) / (x1-x0)

    #Ax + By + C = 0
    a = y1 - y0
    b = -1 * (x1 - x0)
    c = b * ((a / b) * (0 - x0) + y0)

    #OCTANT 1 AND 5
    if (0 <= slope and slope <= 1):
        #midpoint times 2
        d2 = 2 * a + b
        #loop to make line
        while currentx <= x1:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
            if abs(d0) < abs(d2):
                currenty += 1
                d2 += (2*b)
            currentx += 1
            d2 += (2*a)

    #OCTANT 2 AND 6
    if (1 < slope):
        #midpoint times 2
        d2 = 2 * b + a
        #loop to make line
        while currenty <= y1:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
            if abs(d0) < abs(d2):
                currentx += 1
                d2 += (2*a)
            currenty += 1
            d2 += (2*b)
