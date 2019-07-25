def far2cel(tempFar):
    tempCel = (5/9) * (tempFar - 32)
    print("Temperature is " + str(tempCel) + " Celcius")

far2cel(77.9)
far2cel(32)



def light_time(distance):
    time = distance / 299792458
    print("It will take " + str(time) + " To go " + str(distance) + "in space")

light_time(376291900)
light_time(299792458)