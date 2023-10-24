car_speed = int(input('Enter current speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min:
    print('Ur goin too slowww')
elif car_speed > speed_limit_max:
    print('Wziuuum ur gettin a fine!')
