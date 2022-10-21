from ctypes import sizeof
from tkinter.messagebox import YES
from turtle import right
import numpy as np
import matplotlib.pyplot as plt
import os

print("Insert output file path.") #put output directory
path=input()
with open(str(path)) as f: 
    lines = f.readlines()
righe = []
for i in range(1,len(lines)):
    righe.append(lines[i])

class parameter():
    def create(self, name, unit):
        self.name = str(name)
        self.unit = str(unit)
        self.values = list()


Time=parameter()
Time.create('Time', '[h]')
Temperature=parameter()
Temperature.create('Temperature', '[K]')
Fission_Rate=parameter()
Fission_Rate.create('Fissio rate', '[fiss/(m^3 s)]')
Hydrostatic_Stress=parameter()
Hydrostatic_Stress.create('Hydrostatic stress', '[MPa]')
Grain_Radius=parameter()
Grain_Radius.create('Grain radius', '[m]')
Xe_Produced=parameter()
Xe_Produced.create('Xe produced', '[at/m^3]')
Xe_Grain=parameter()
Xe_Grain.create('Xe in grain', '[at/m^3]')
Xe_Intragranular_solution=parameter()
Xe_Intragranular_solution.create('Xe in intragranular solution', '[at/m^3]')
Xe_Intragranular_bubbles=parameter()
Xe_Intragranular_bubbles.create('Xe in intragranular bubbles', '[at/m^3]')
Xe_Grain_boundary=parameter()
Xe_Grain_boundary.create('Xe at grain buondary','[at/m^3]')
Xe_Released=parameter()
Xe_Released.create('Xe released', '[at/m^3]')
Kr_Produced=parameter()
Kr_Produced.create('Kr produced', '[at/m^3]')
Kr_Grain=parameter()
Kr_Grain.create('Kr in grain', '[at/m^3]')
Kr_Intragranular_solution=parameter()
Kr_Intragranular_solution.create('Kr in intragranular solution', '[at/m^3]')
Kr_Intragranular_bubbles=parameter()
Kr_Intragranular_bubbles.create('Kr in intragranular bubbles', '[at/m^3]')
Kr_Grain_boundary=parameter()
Kr_Grain_boundary.create('Kr at grain buondary','[at/m^3]')
Kr_Released=parameter()
Kr_Released.create('Kr released', '[at/m^3]')
Fission_gas_release=parameter()
Fission_gas_release.create('Fission gas release', '') #vedi unità
Intragranular_bubble_Concentration=parameter()
Intragranular_bubble_Concentration.create('Intragranular bubble concentration', '[bub/m^3]')
Intragranular_bubble_Radius=parameter()
Intragranular_bubble_Radius.create('Intragranular bubble radius', 'm')
Intragranular_gas_Swelling=parameter()
Intragranular_gas_Swelling.create('Intragranular gas Swelling', '') #vedi unità
Intergranular_bubble_Concentration=parameter()
Intergranular_bubble_Concentration.create('Intergranular bubble concentration', '[bub/m^2]')
Intergranular_atoms_per_bubble=parameter()
Intergranular_atoms_per_bubble.create('Intergranular atoms per bubble', 'at/bub')
Intergranular_vacancies_per_bubble=parameter()
Intergranular_vacancies_per_bubble.create('Intergranular vacancies per bubble', '[vac/bub]')
Intergranular_bubble_Radius=parameter()
Intergranular_bubble_Radius.create('Intergranular bubble radius', '[m]')
Intergranular_bubble_Area=parameter()
Intergranular_bubble_Area.create('Intergranular bubble area', '[m^2]')
Intergranular_bubble_Volume=parameter()
Intergranular_bubble_Volume.create('Intergranular bubble volume', '[m^3]')
Intergranular_fractional_coverage=parameter()
Intergranular_fractional_coverage.create('Intergranular fractional coverage', '')
Intergranular_saturation_fractional_coverage=parameter()
Intergranular_saturation_fractional_coverage.create('Intergranular saturation fractional coverage', '')
Intergranular_gas_Swelling=parameter()
Intergranular_gas_Swelling.create('Intergranular gas Swelling', '')
Intergranular_fractional_intactness=parameter()
Intergranular_fractional_intactness.create('Intergranular fractional intactness', '')
Burnup=parameter()
Burnup.create('Burnup', '[MWd/kgUO2]')
U235_density=parameter()
U235_density.create('U235 density', '[kg/m^3]')
U238_density=parameter()
U238_density.create('U238 density', '[kg/m^3]')
Intergranular_vented_fraction=parameter()
Intergranular_vented_fraction.create('Intergranular vented fraction', '')
Intergranular_venting_probability=parameter()
Intergranular_venting_probability.create('Intergranular venting probability','')
for riga in righe:
    riga = riga.split("\t")
    Time.values.append(float(riga[0]))
    Temperature.values.append(float(riga[1]))
    Fission_Rate.values.append(float(riga[2]))
    Hydrostatic_Stress.values.append(float(riga[3]))
    Grain_Radius.values.append(float(riga[4]))
    Xe_Produced.values.append(float(riga[5]))
    Xe_Grain.values.append(float(riga[6]))
    Xe_Intragranular_solution.values.append(float(riga[7]))
    Xe_Intragranular_bubbles.values.append(float(riga[8]))
    Xe_Grain_boundary.values.append(float(riga[9]))
    Xe_Released.values.append(float(riga[10]))
    Kr_Produced.values.append(float(riga[11]))
    Kr_Grain.values.append(float(riga[12]))
    Kr_Intragranular_solution.values.append(float(riga[13]))
    Kr_Intragranular_bubbles.values.append(float(riga[14]))
    Kr_Grain_boundary.values.append(float(riga[15]))
    Kr_Released.values.append(float(riga[16]))
    Fission_gas_release.values.append(float(riga[17]))
    Intragranular_bubble_Concentration.values.append(float(riga[18]))
    Intragranular_bubble_Radius.values.append(float(riga[19]))
    Intragranular_gas_Swelling.values.append(float(riga[20]))
    Intergranular_bubble_Concentration.values.append(float(riga[21]))
    Intergranular_atoms_per_bubble.values.append(float(riga[22]))
    Intergranular_vacancies_per_bubble.values.append(float(riga[23]))
    Intergranular_bubble_Radius.values.append(float(riga[24]))
    Intergranular_bubble_Area.values.append(float(riga[25]))
    Intergranular_bubble_Volume.values.append(float(riga[26]))
    Intergranular_fractional_coverage.values.append(float(riga[27]))
    Intergranular_saturation_fractional_coverage.values.append(float(riga[28]))
    Intergranular_gas_Swelling.values.append(float(riga[29]))
    Intergranular_fractional_intactness.values.append(float(riga[30]))
    Burnup.values.append(float(riga[31]))
    U235_density.values.append(float(riga[32]))
    U238_density.values.append(float(riga[33]))
    Intergranular_vented_fraction.values.append(float(riga[34]))
    Intergranular_venting_probability.values.append(float(riga[35]))



print("List of output parameters:")
print("Time, Temperature, Fission_Rate, Hydrostatic_Stress, Grain_Radius, Fission_gas_release")
print("Xe_Produced, Xe_Grain, Xe_Intragranular_solution, Xe_Intragranular_bubbles, Xe_Grain_boundary, Xe_Released")
print("Kr_Produced, Kr_Grain, Kr_Intragranular_solution, Kr_Intragranular_bubbles, Kr_Grain_boundary, Kr_Released")
print("Intragranular_bubble_Concentration, Intragranular_bubble_Radius, Intragranular_gas_Swelling, ")
print("Intergranular_bubble_Concentration, Intergranular_atoms_per_bubble, Intergranular_vacancies_per_bubble, Intergranular_bubble_Radius") 
print("Intergranular_bubble_Area, Intergranular_bubble_Volume, Intergranular_fractional_coverage")
print("Intergranular_saturation_fractional_coverage, Intergranular_gas_Swelling, Intergranular_fractional_intactness")
print("Burnup, U235_density, U238_density")
print("Intergranular_vented_fraction, Intergranular_venting_probability.")

print("Plot variables? yes/no")
cond=input("Ans: ")
while cond == "yes":
    print("How many parameters do you want to plot in the same graph? (2 or 3)")
    cond2 = int(input("Ans: "))  
    if cond2 == 2:
          print("Choose parameter for plot:")
          xInput = globals().get(input("X axis = "))
          yInput = globals().get(input("Y axis = "))
          plt.plot(xInput.values,yInput.values)
          plt.xlabel(str(xInput.name) +" " +str(xInput.unit))
          plt.ylabel(str(yInput.name) +" " +str(yInput.unit))
          plt.grid()
          plt.show()
    else:
          print("Choose parameter for plot:")
          xInput = globals().get(input("X axis = "))
          y1Input = globals().get(input("Y1 axis = "))
          y2Input = globals().get(input("Y2 axis = "))
          fig, ax1=plt.subplots()
          ax1.plot(xInput.values,y1Input.values)
          ax1.plot(xInput.values,y2Input.values)
          ax1.set_xlabel(str(xInput.name) +" " +str(xInput.unit))
          ax1.set_ylabel(str(y1Input.name) +" " +str(y1Input.unit))
          ax2=ax1.twinx()
          ax2.set_ylabel(str(y2Input.name) +" " +str(y2Input.unit))
          ax1.legend([str(y1Input.name) , str(y2Input.name)])
          ax1.grid()
          plt.show()
    print("Plot variables? yes/no")
    cond3=input("Ans: ")
    if cond3 == 'no':
         break

  
