def light_time(distance):
    time = distance / 299792458
    print("It will take " + str(time) + " To go " + str(distance) + "in space")
    return time

light_time(376291900)
light_time(299792458)