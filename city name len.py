city_a = input()
city_b = input()
city_c = input()

# the shortest city name
if min(len(city_a), len(city_b), len(city_c)) == len(city_a):
    print(city_a)
elif min(len(city_a), len(city_b), len(city_c)) == len(city_b):
    print(city_b)
elif min(len(city_a), len(city_b), len(city_c)) == len(city_c):
    print(city_c)

# the lengthest city name
if max(len(city_a), len(city_b), len(city_c)) == len(city_a):
    print(city_a)
elif max(len(city_a), len(city_b), len(city_c)) == len(city_b):
    print(city_b)
elif max(len(city_a), len(city_b), len(city_c)) == len(city_c):
    print(city_c)

