from pyowm.owm import OWM


owm = OWM('3326a0e7b6c3f19ca40826b5fe3277bf')
T = [] #temperature
manager = owm.weather_manager()
weather = manager.weather_at_place('Moscow,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Москва: ", weather, temp )

weather = manager.weather_at_place('Saint Petersburg,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Санкт-Петербург: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Novosibirsk,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Новосибирск: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Ekaterinburg,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Екатеринбург: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Nizhny Novgorod,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Нижний Новгород: ", weather, weather.temperature('celsius'))

weather = manager.weather_at_place('Kazan,Russia').weather 
temp = weather.temperature('celsius')
T.append(temp["temp"])
print("Казань: ", weather, weather.temperature('celsius'))

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

print("Медиана данного ряда -", T[len(T) // 2 - 1] )
print("Среднее значение температуры в 6-и самых больших городах Росии:", mid)