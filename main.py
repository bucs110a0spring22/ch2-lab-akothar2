import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
print("Weeks", type(weeks))
print("Classes", type(classes))
print("Tuition", type(tuition))
print("Cost per week", type(cost_per_week))
print("Classes per week", type(classes_per_week))
print("Cost per class", type(cost_per_class))

#Part B
print(random.randrange(1,10))


















