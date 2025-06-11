
def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 16.0:
        return " Severe Thinness"
    elif 16.0 <= bmi < 17.0:
        return "Moderate  Thinness"
    elif 17 <= bmi < 18.5:
        return " Mild Thinness "
    elif 18.5 <= bmi < 25:
        return "Normal  Thinness"
    elif 25 <= bmi < 30:
        return "Overweight "
    elif 30 <= bmi < 35:
        return " Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

def bmi_result():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight,height)
    category= bmi_category(bmi)
    print(f" BMI: {bmi:.1f}")
    print(f"Category: {category}")

bmi_result()










