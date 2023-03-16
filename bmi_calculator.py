
height = input("enter your height in meters: \n")
weight = input("enter your weight in kilograms: \n")
number_height = float(height)
number_weight = float(weight)
bmi = number_weight / number_height ** 2
bmi_result = int(bmi)
print(bmi_result)