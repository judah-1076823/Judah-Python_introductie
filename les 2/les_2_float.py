#Float

#ethernet capacity berekenen
ethernet_speed_mbs = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbs * efficiency
print(maximum_capacity)

#print capacity used on the ethernet
ethernet_speed_mbs = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbs /  download_speed_average
print(usage)


#speed of light in m/s
speed_of_light = 299_792_458

#afstand Rotterdam / New York
distance_Rotterdam_NewYork = 5_862.03
#afstand Rotterdam naar New York in meters delen door the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC *1000.0} milliseconds.')

#wat is het data type?
print(type(time_to_reach_NYC))
