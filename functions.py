#Temperature conversions with functions
#CS175
#Ziv Cohen

def main():
    controlLoop()

def convertToKelvin():
    Kelvin = (((temp - 32) * 5) / 9)+273.15
    return Kelvin
    

def convertToCentigrade():
    Centigrade = ((temp - 32)*5/9)
    return Centigrade
    

def doConversion():
    temp = getFahrenheit()
    Kelvin = convertToKelvin()
    Centigrade = convertToCentigrade()
    print(f'Fahrenheit: {temp:.2f}', f'Kelvin: {Kelvin:.2f}', f'Centigrade: {Centigrade:.2f}')
    
    
    

def repeat():
    how_many = int(input('How many conversions would you like to do this time?: '))

    for x in range (how_many):
        doConversion()
    

def controlLoop():
    conversions = input('Do you want to do some conversions(Yes or No)?: ')
    if conversions == 'yes':
        repeat()
    

def getFahrenheit():
    global temp
    while True:
        temp = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
    
        if temp > 130 or temp < -50:
            print('Invalid value, please re-enter')
        else:
            return temp


if __name__ == '__main__':
    main()
