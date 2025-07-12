import matplotlib.pyplot as plt

categories = ["Apple", "Banana","orange"]
values = [10,30,16]

plt.figure(figsize=(8,9))

plt.bar(categories,values,color="skyblue")

plt.title("Bar Chart")

plt.xlabel("fruit")
plt.ylabel("values")
plt.grid(axis="y",linestyle="--",alpha = 0.7)
plt.show()