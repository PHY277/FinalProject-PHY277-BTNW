import numpy as np 
import matplotlib.pyplot as plt 
from scipy import optimize 
#Vin is A-k Voltage
#Vout is Y-Out Voltage
#Preliminary Data to observe trends
Vin = np.array([-0.001, 0.343, 4.165, 5.883, 6.69, 7.90, 10.01, 12.06, 14.50, 16.57, 17.40, 18.56, 19.96, 21.52, 23.48, 26.30, 28.30, 30.52, 32.30, 34.42, 36.41, 38.12, 39.85, 41.55, 43.92, 43.90])
Vout = np.array([-0.084, -0.080, -0.082, -0.066, -0.062, -0.068, 0.045, 0.105, 0.274, 0.842, 0.202, 0.110, 0.500, 0.545, 0.260, 0.830, 0.190, 1.023, 0.760, 0.930, 1.178, 1.440, 1.823, 2.45, 2.84, 5.40])

#Data Set 1
Vin1 = np.array([-0.001, 0.009, 0.247, 0.279, 0.308, 0.323, 0.353, 0.495, 0.553, 3.005, 3.437, 4.512, 5.860, 6.260, 6.88, 6.92, 7.82, 8.83, 9.37, 10.27, 11.59, 11.76, 13.27, 13.70, 14.76, 15.53, 16.83, 18.32, 18.95, 19.25, 20.45, 21.84, 23.14, 24.21, 25.35, 25.13, 26.57, 27.03, 27.08, 29.62, 30.33, 31.60, 32.06, 32.60, 32.94, 34.06, 34.74, 35.46])
Vout1 = np.array([-0.067, -0.070, -0.074, -0.070, -0.081, -0.081, -0.080, -0.081, -0.081, -0.080, -0.080, -0.080, -0.078, -0.071, -0.071, -0.069, -0.075, -0.069, -0.051, 0.024, 0.093, 0.084, -0.004, 0.041, 0.292, 0.602, 0.361, 0.109, 0.296, 0.443, 1.457, 1.258, 0.573, 1.450, 2.68, 1.45, 1.57, 1.78, 2.09, 2.64, 3.08, 3.32, 3.46, 3.35, 3.08, 3.19, 3.48, 4.05])

Vin2 = np.array([-0.001, 0.026, 0.270, 0.271, 0.412, 0.870, 2.527, 3.280, 4.110, 4.625, 4.913, 5.84, 7.20, 7.90, 8.55, 9.65, 10.40, 11.09, 11.65, 11.96, 12.25, 12.72, 13.04, 13.77, 14.88, 15.02, 15.39, 15.84, 16.18, 16.67, 17.17, 17.60, 18.18, 18.82, 19.07, 19.55, 19.98, 20.49, 20.94, 21.47, 21.88, 22.48, 22.90, 23.47, 24.08, 24.48, 25.02, 25.52, 26.09, 26.46, 27.10, 27.56, 27.99, 28.49, 29.17, 29.46, 29.89, 30.50, 31, 31.53, 32.30, 32.91, 33.20, 34.00, 34.46, 34.94, 35.39, 35.99, 36.67, 37.18, 37.49, 38.01, 38.48])
Vout2_orig = np.array([-.297, -.294, -.302, -.312, -.312, -.316, -.316, -.310, -.317, -.312, -.318, -.318, -.302, -.305, -.298, -.270, -.215, -.152, -.152, -.172, -.193, -.232, -.253, -.237, -.062, -.002, .219, .370, .203, .005, -.142, -.190, -0.189 ,-.072, .025, .184, .230, .403, 0.628, .570, .468, .060, -.078, -.069, 0.066, .190, .450, 1.080, 1.364, 0.933, 0.239, 0.000, -0.023, 0.183, .513, .678, .662, 1.218, 1.590, 1.452, 0.720, .140, .147, .740, 1.005, 1.262, 2.261, 1.381, 1.094, 0.848, 0.775, 0.853, 1.083])
Vout2 = Vout2_orig + 0.3
print(len(Vin2))
print(len(Vout2))

#plt.scatter(Vin2, Vout2, color="r")
plt.plot(Vin2, Vout2, color='r', linewidth=2)
#plt.plot(Vin2, Vout2, 'sr-', linewidth=1)

plt.title("Vout vs. Vin (2)")
plt.xlabel("Vin (Volts)")
plt.ylabel("Vout (Volts)")
#plt.show()

#Gaussian Fit Functions

def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-0.5*((x - mean) / stddev)**2)

bins= np.arange(0,41,1)
bin_x = Vin2
bin_counts = Vout2
#Fit 1
x_min = 8.5
x_max = 13

x_fit = bin_x[(bin_x>=x_min) & (bin_x<=x_max)]
y_fit = bin_counts[(bin_x>=x_min) & (bin_x<=x_max)]
x_fit_ave = np.average(x_fit, weights= y_fit)
#print(x_fit_ave)
print("Peak 1")
print("Amplitude, Mean, Standard Deviation")
initial_par_1= [2.5,x_fit_ave, 1]
popt1, covmat1 = optimize.curve_fit(gaussian, x_fit, y_fit, p0= initial_par_1)
print(popt1)
print("------------------------------------------")

x_plot = np.linspace(x_min, x_max, 100)
#plt.hist(bin_x, bins, weights=bin_counts)
plt.plot(x_plot, gaussian(x_plot, *popt1), 'k--')
#plt.xlim(0,x_max+3)
#plt.show()

#Fit 2
x_min2 = 13
x_max2 = 18

x_fit2 = bin_x[(bin_x>=x_min2) & (bin_x<=x_max2)]
y_fit2 = bin_counts[(bin_x>=x_min2) & (bin_x<=x_max2)]
x_fit_ave2 = np.average(x_fit2, weights= y_fit2)

print("Peak 2")
print("Amplitude, Mean, Standard Deviation")
initial_par_2= [2.5,x_fit_ave2, 1]
popt2, covmat2 = optimize.curve_fit(gaussian, x_fit2, y_fit2, p0= initial_par_2)
print(popt2)
print("------------------------------------------")

x_plot2 = np.linspace(x_min2, x_max2, 100)
plt.plot(x_plot2, gaussian(x_plot2, *popt2), 'k--')

#Fit 3
x_min3 = 18
x_max3 = 24

x_fit3 = bin_x[(bin_x>=x_min3) & (bin_x<=x_max3)]
y_fit3 = bin_counts[(bin_x>=x_min3) & (bin_x<=x_max3)]
x_fit_ave3 = np.average(x_fit3, weights= y_fit3)

print("Peak 3")
print("Amplitude, Mean, Standard Deviation")
initial_par_3= [2.5,x_fit_ave3, 1]
popt3, covmat3 = optimize.curve_fit(gaussian, x_fit3, y_fit3, p0= initial_par_3)
print(popt3)
print("------------------------------------------")

x_plot3 = np.linspace(x_min3, x_max3, 100)
plt.plot(x_plot3, gaussian(x_plot3, *popt3), 'k--')

#Fit 4
x_min4 = 24
x_max4 = 28

x_fit4 = bin_x[(bin_x>=x_min4) & (bin_x<=x_max4)]
y_fit4 = bin_counts[(bin_x>=x_min4) & (bin_x<=x_max4)]
x_fit_ave4 = np.average(x_fit4, weights= y_fit4)

print("Peak 4")
print("Amplitude, Mean, Standard Deviation")
initial_par_4= [2.5,x_fit_ave4, 1]
popt4, covmat4 = optimize.curve_fit(gaussian, x_fit4, y_fit4, p0= initial_par_4)
print(popt4)
print("------------------------------------------")

x_plot4 = np.linspace(x_min4, x_max4, 100)
plt.plot(x_plot4, gaussian(x_plot4, *popt4), 'k--')

#Fit 5
x_min5 = 28
x_max5 = 33.25

x_fit5 = bin_x[(bin_x>=x_min5) & (bin_x<=x_max5)]
y_fit5 = bin_counts[(bin_x>=x_min5) & (bin_x<=x_max5)]
x_fit_ave5 = np.average(x_fit5, weights= y_fit5)

print("Peak 5")
print("Amplitude, Mean, Standard Deviation")
initial_par_5= [2.5,x_fit_ave5, 1]
popt5, covmat5 = optimize.curve_fit(gaussian, x_fit5, y_fit5, p0= initial_par_5)
print(popt5)
print("------------------------------------------")

x_plot5 = np.linspace(x_min5, x_max5, 100)
plt.plot(x_plot5, gaussian(x_plot5, *popt5), 'k--')

#Fit 6
x_min6 = 33.25
x_max6 = 37.25

x_fit6 = bin_x[(bin_x>=x_min6) & (bin_x<=x_max6)]
y_fit6 = bin_counts[(bin_x>=x_min6) & (bin_x<=x_max6)]
x_fit_ave6 = np.average(x_fit6, weights= y_fit6)

print("Peak 6")
print("Amplitude, Mean, Standard Deviation")
initial_par_6= [2.5,x_fit_ave6, 1]
popt6, covmat6 = optimize.curve_fit(gaussian, x_fit6, y_fit6, p0= initial_par_6)
print(popt6)
print("------------------------------------------")

x_plot6 = np.linspace(x_min6, x_max6, 100)
plt.plot(x_plot6, gaussian(x_plot6, *popt6), 'k--')

netMeans = np.array([popt1[1], popt2[1], popt3[1], popt4[1], popt5[1], popt6[1]])
print("The Mean of Each peak is: ")
print(netMeans)
print("------------------------------------------")

#Calculating the Quantization Part of Franck Hertz
q1 = popt2[1] - popt1[1]
q2 = popt3[1] - popt2[1]
q3 = popt4[1] - popt3[1]
q4 = popt5[1] - popt4[1]
q5 = popt6[1] - popt5[1]
q_mean = (q1 + q2 + q3 + q4 + q5) / 5

print("Differences of means")
print(q1, q2, q3, q4, q5)
print("------------------------------------------")
print("Averge of the Differences")
print(q_mean)
print("------------------------------------------")

#Standard Error in each of the Means calculated
SE1 = popt1[2] / np.sqrt(100)
SE2 = popt2[2] / np.sqrt(100)
SE3 = popt3[2] / np.sqrt(100)
SE4 = popt4[2] / np.sqrt(100)
SE5 = popt5[2] / np.sqrt(100)
SE6 = popt6[2] / np.sqrt(100)

#Error Propagation 
SE = np.array([SE1, SE2, SE3, SE4, SE5, SE6])
diff_var = SE[:-1]**2 + SE[1:]**2
Alpha = np.sqrt(np.sum(diff_var)) / 5 
print("The Standard Error associated with the Average of Differences")
print(Alpha)
print("------------------------------------------")

print("The Final Result is")
print(f'({q_mean:.4f} ± {Alpha:.4f}) Volts')
plt.show()