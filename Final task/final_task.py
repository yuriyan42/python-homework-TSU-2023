import matplotlib.pyplot as plt
import random
import math
import numpy as np
import lhapdf

class MC:
    def __init__(self, pdf, flavor, dglap_kernel, Q2, number_of_iterations=100, number_of_points=10000):
        self.x_list = []
        self.integral_values = []
        self.absolute_errors = []
        self.relative_errors = []
        
        if Q2 < pdf.q2Min:
            print("Your Q2 value falls below the lower limit of the valid range!")
            print("The Q2 value set to the minimum available value!")
            Q2 = pdf.q2Min
        elif Q2 > pdf.q2Max:
            print("Your Q2 value exceeds the upper limit of the valid range!")
            print("The Q2 value set to the maximum available value!")
            Q2 = pdf.q2Max
        
        print('Evaluation started. Please wait...')
        for x_i in np.arange(pdf.xMin, pdf.xMax, 0.02):
            integrals = []
            for _ in range(number_of_iterations):
                integral = 0.0
                for _ in range(number_of_points):
                    u = random.uniform(x_i, 1)
                    integral += dglap_kernel(u) * (pdf.xfxQ2(flavor, x_i / u, Q2) / x_i)
                integrals.append(integral * (1 - x_i) / number_of_points)
            self.x_list.append(x_i)
            mean = np.mean(integrals)
            self.integral_values.append(mean)
            std_error = np.std(integrals) / math.sqrt(len(integrals))
            self.absolute_errors.append(std_error)
            self.relative_errors.append(abs(std_error / mean))

    def get_x_list(self):
        return self.x_list

    def get_values(self):
        return self.integral_values

    def get_abs_error(self):
        return self.absolute_errors

    def get_rel_error(self):
        return self.relative_errors
    
def SetInit(name: str, info: bool = True):
    
    set = lhapdf.getPDFSet(name)
    
    if info:
        print('#######################')
        print(set.description)
        print('#######################')
    
    return(set)

def PdfInit(set, pdfID: int, info: bool = True):
    
    pdf = set.mkPDF(pdfID)
    
    if info:
        print('#######################')
        print(f'Aviable flavors: {pdf.flavors()}')
        print(f'with masses: {[pdf.quarkMass(id) for id in pdf.flavors()]}')
        print(f'Minimum valid x value: {pdf.xMin}. Maximum valid x value: {pdf.xMax}')
        print(f'Minimum valid Q^2 value: {pdf.q2Min}. Maximum valid Q^2     value: {pdf.q2Max}')
        print('#######################')
        
    return(pdf)

#################################################
def Pqg(x):
    return 0.5 * (x ** 2 + (1 - x) ** 2)

# Dataset initialization
pdfset = SetInit("CT10nlo")
pdf = PdfInit(pdfset, 0)

# Convolution
test1 = MC(pdf, 21, Pqg, 10 ** 8)

# Get values
x_list = test1.get_x_list()
integral_values = test1.get_values()
absolute_errors = test1.get_abs_error()
relative_errors = test1.get_rel_error()

# Print values
for i in range(len(x_list)):
    print(f"x_{i} = {x_list[i]}, Conv = {integral_values[i]}, AbsErr = {absolute_errors[i]}, RelErr = {relative_errors[i]}")

# Plot Convolution(x)
fig, ax = plt.subplots()
ax.plot(x_list, integral_values, "-o", linewidth = 2.0)
plt.title("Pqg plot")
plt.xlabel("x")
plt.ylabel("convolution")
ax.set(xlim=(0.01, 1), ylim=(0, 40))
plt.show()


