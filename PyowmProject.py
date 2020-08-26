from pyowm.owm import OWM


owm = OWM('3326a0e7b6c3f19ca40826b5fe3277bf')
T = [] #temperature
manager = owm.weather_manager()
weather = manager.weather_at_place('Moscow,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Moscow: ", weather, temp )

weather = manager.weather_at_place('Saint Petersburg,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Saint Petersburg: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Novosibirsk,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Novosibirsk: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Ekaterinburg,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Ekaterinburg: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Nizhny Novgorod,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Nizhny Novgorod: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Kazan,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Kazan: ", weather, weather.temperature('celsius'))

print(*T)

for i in range(len(T) - 1):
	for j in range(i + 1, len(T)):
		if T[j] < T[i]:
			T[i], T[j] = T[j], T[i]

sum = 0
for elem in T:
	sum += elem
mid = sum / len(T)
print(*T)

print("Медиана значений температуры в 6 самых больших городов России -", T[len(T) // 2 - 1] )
print("И среднее значение температурыв 6 самых больших городов России:", mid)