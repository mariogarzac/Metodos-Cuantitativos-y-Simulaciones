
from random import seed
from random import randint
import matplotlib.pyplot as plt


dice_face = [i for i in range(6)]
reps = [0 for _ in range(6)]
label = ["One", "Two", "Three", "Four", "Five", "Six"]

seed()
for i in range(1000):
    reps[randint(0,5)] += 1

print("Arreglo con las repeticiones")
print(reps)
max = max(reps)
# plt.ylim(0,max)
# plt.xlim(1,6)
plt.bar(dice_face, reps)

plt.xlabel("Dice Face")
plt.ylabel("Repetitions")
plt.title("Act 1")
plt.show()
