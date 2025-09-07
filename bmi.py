w = float(input('Insert your weight: '))
h = float(input('Insert your height: '))

bmi = w / (h*h)

print('Your BMI score is: ', bmi)

if bmi < 18.5:
    print('According to your BMI score, you are thin.')
elif 18.6<bmi<24.9:
    print('According to your BMI score, you are normal.')
else:
    print('According to your BMI score, you are overweight.')

    
