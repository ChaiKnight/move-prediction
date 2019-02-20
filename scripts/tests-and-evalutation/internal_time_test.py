import matplotlib.pyplot as plt

# x = [11.84,9.30,5.37,7.59,11.64,8.58,7.14,4.72,5.77,9.1,6.23,4.91,4.19,6.10,10.46,7.62,6.24,4.85,5.25,8.37]
# x = [6.03,6.26,4.48,1.64,11.38,1.32,13.28,12.66,5.59,9.22,2.27,2.01,14.13,13.51,3.46,2.82,3.25,7.25,2.51,6.89,3.35,1.18,5.32,13.43,1.25,4.14,6.38,13.88,11.82,1.20]
x = [3.97,8.56,2.98,3.49,9.36,4.25,10.92,5.86,2.37,2.76,6.77,3.32,4.47,17.21,13.75,3.15,6.08,7.23,7.20,7.10,4.02,5.50,2.14,9.27,2.25,4.49,13.55,2.75,2.13,9.20,8.59,3.79,1.82,12.59,3.93,2.99,3.42,17.32,12.92]

fig1, ax1 = plt.subplots()
ax1.set_title('Time(s) to reach bottle')
dic = ax1.boxplot(x)

for line in dic['boxes']:
    print(line.get_ydata())
    
for line in dic['medians']:
    print(line.get_ydata())
    
for line in dic['whiskers']:
    print(line.get_ydata())
    
# results: 4.19, 5.34, 6.69, 8.71, 11.84
# results round 2: 1.18, 2.59, 5.46, 10.84, 14.13
# results round 3 (single direction): 1.82, 3.24, 4.49, 8.9, 17.32