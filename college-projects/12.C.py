from collections import Counter
my_dict = {'A': 80, 'B': 23, 'C': 45, 'D': 48, 'E': 12, 'F': 99}
k = Counter(my_dict)
high = k.most_common(3)
print("Initial Dictionary:")
print(my_dict, "\n")
print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
   print(i[0]," :",i[1]," ")
