def celsius_to_fahrenheit():
    
    print("Enter a temperature in celsius:")
    celsius = float(input())
    
    return celsius*9/5 + 32

print("Your Fahrenheit temperature: ",celsius_to_fahrenheit())