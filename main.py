import random

#Part A
weeks = 16
print("Weeks:", weeks, type(weeks))

classes = 5
print("Classes:", classes, type(classes))

tuition = 6000
print("Tuition:", tuition, type(tuition))

cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)

classes_per_week = 3
print("Classes per week:", classes_per_week, type(classes_per_week))

cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))
print("Cost per class is", cost_per_class)

#Part B
print(random.randrange(1,10))
avg_height_cm = [160, 170, 180, 190, 200]
print(avg_height_cm)
random_height = print(random.choice(avg_height_cm))

















