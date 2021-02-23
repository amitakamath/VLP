import matplotlib.pyplot as plt

bleu1 = [0.622, 0.677, 0.707, 0.712, 0.712, 0.720, 0.731, 0.736, 0.740, 0.741, 0.744, 0.745, 0.744, 0.743, 0.748]
bleu4 = [0.188, 0.230, 0.263, 0.277, 0.283, 0.291, 0.294, 0.301, 0.306, 0.302, 0.311, 0.312, 0.311, 0.313, 0.314]
cider = [0.555, 0.731, 0.828, 0.879, 0.880, 0.921, 0.940, 0.939, 0.965, 0.973, 0.983, 0.997, 0.989, 1.006, 0.998]

bleu1_2 = [0.742, 0.752, 0.749, 0.744, 0.751, 0.749, 0.751, 0.754, 0.752, 0.753, 0.754, 0.752, 0.752, 0.751, 0.752]
bleu4_2 = [0.315, 0.316, 0.321, 0.317, 0.319, 0.322, 0.317, 0.321, 0.319, 0.327, 0.326, 0.323, 0.323, 0.326, 0.326]
cider_2 = [1.003, 1.010, 1.025, 1.016, 1.022, 1.028, 1.023, 1.027, 1.030, 1.044, 1.045, 1.036, 1.039, 1.042, 1.042]

bleu1.extend(bleu1_2)
bleu4.extend(bleu4_2)
cider.extend(cider_2)
epochs = list(range(1, 31))

plt.plot(epochs, bleu1, label='BLEU-1')
plt.xlabel('Epochs')
plt.ylabel('Val BLEU-1')
plt.title('Val BLEU-1 of bare-bones VLP')
plt.grid()
plt.savefig('bleu1.png', dpi=400)
plt.clf()

plt.plot(epochs, bleu4, label='BLEU-4')
plt.xlabel('Epochs')
plt.ylabel('Val BLEU-4')
plt.title('Val BLEU-4 of bare-bones VLP')
plt.grid()
plt.savefig('bleu4.png', dpi=400)
plt.clf() 

plt.plot(epochs, cider, label='CIDEr')
plt.xlabel('Epochs')
plt.ylabel('Val CIDEr')
plt.title('Val CIDEr of bare-bones VLP')
plt.grid()
plt.savefig('cider.png', dpi=400)

