import numpy as np

all_data_chars = open('input_8.txt').read().strip()
all_data = np.array(list(all_data_chars), dtype=int).reshape(-1, 25*6)
min_layer = np.argmin(np.sum(all_data==0, axis=1))
print(sum(all_data[min_layer]==1) * sum(all_data[min_layer]==2))

# my_image = np.array(list((layer[layer!=2][0] for layer in all_data.transpose()))).reshape(25,6).transpose()


# print(all_data.shape)
# ans =[all_data[:,x][all_data[:,x]!=2][0] for x in range(0,150)]

# twos_removed = [l[l!=2][0] for l in all_data.transpose()]
# print(''.join(str(x) for x in twos_removed))



# print(''.join([str(c) for c in my_image.flatten()]))

# import matplotlib.pyplot as plt

# plt.imshow(np.array(twos_removed).reshape(25,6))
# plt.show()
