import matplotlib.pyplot as plt 

labels = 'Logs', 'Frog', 'Dogs', 'Hogs'
sizes = [15, 30, 50, 5]
explode = (0, 0.1, 0, 0.03)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle = 90)
plt.show()
