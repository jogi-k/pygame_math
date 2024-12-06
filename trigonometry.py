import math
WIDTH = 1000
HEIGHT = 1000

mitte_x = WIDTH / 2
mitte_y = HEIGHT / 2

radius = 4 * HEIGHT / 10

winkel = 30


def draw():
    screen.clear()
    screen.draw.circle(( mitte_x , mitte_y ), radius , 'white')
    
    sinus = math.sin( math.radians( winkel ) ) 
    cosinus = math.cos( math.radians( winkel ) )  
    sinu_r = sinus * radius
    cosi_r = cosinus * radius

    screen.draw.line(( mitte_x , mitte_y ),( mitte_x + cosi_r, mitte_y - sinu_r ), 'white')
    screen.draw.line(( mitte_x , mitte_y ),( mitte_x + cosi_r, mitte_y ), 'red')
    screen.draw.line(( mitte_x + cosi_r , mitte_y ),( mitte_x + cosi_r, mitte_y - sinu_r ), 'green')

    mytext = "Winkel = " + str( winkel) + "\nSinus = " + str(sinus) + "\nCosinus = " + str(cosinus)      
    screen.draw.text( mytext, ( 10, 10) )

    if cosinus > 0 :
        screen.draw.text("cos", topright = ( mitte_x + cosi_r - 3 , mitte_y + 3 ))
    else :
        screen.draw.text("cos", topleft = ( mitte_x + cosi_r + 3 , mitte_y + 3 ))

    if sinus > 0 :
        screen.draw.text("sin", topright = ( mitte_x + cosi_r + 3 , mitte_y - sinu_r + 3), angle = 90 )
    else:
        screen.draw.text("sin", topleft = ( mitte_x + cosi_r + 3 , mitte_y - sinu_r - 3), angle = 90 )



def on_key_down( key ):
    global winkel

    if key == key.UP:
        winkel = winkel + 10
    if key == key.DOWN:
        winkel = winkel - 10
    if key == key.LEFT:
        winkel = winkel - 1
    if key == key.RIGHT:
        winkel = winkel + 1
    if key == key.W :
        winkel = 90
    if key == key.A :
        winkel = 180
    if key == key.S :
        winkel = 270
    if key == key.D :
        winkel = 0

    
    if winkel > 360 :
        winkel = winkel - 360
    if winkel < 0 :
        winkel = 360 + winkel   

