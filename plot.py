import matplotlib.pyplot as plt

time_cluster = [1.84, 2.43, 1.84, 2.16, 2.24, 2.81, 5.29, 7.12, 11.03, 18.56]
city_cluster = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

time_seq = [3.04, 4.02, 6.84, 14.66, 29.5]
city_seq = [50, 100, 200, 400, 800]

plt.title("Cluster 7 workers: 100 iterations and 60 particles")
plt.plot(city_cluster, time_cluster, '--bo')

#plt.title("Sequential: 100 iterations and 60 particles")
#plt.plot(city_seq, time_seq, '--bo')

plt.xlabel('Number of cities')
plt.ylabel('Time (s)')

plt.show()