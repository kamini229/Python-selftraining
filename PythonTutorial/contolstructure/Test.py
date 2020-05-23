def calculate_area_of_circle(radius):
	PI = 3.14
	area = PI * radius * radius
	print(area)
	x = area % 4 == True
	if x == True:
		print("The radius :" + str(radius) + " is divisible_area")

calculate_area_of_circle(23.45)
calculate_area_of_circle(56.78)
calculate_area_of_circle(45.67)
calculate_area_of_circle(78.9)



