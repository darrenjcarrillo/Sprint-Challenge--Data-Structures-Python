import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# BST Data Structure
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert
    def insert(self, value):
        # Case 1 - Value is less than root
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        # Case 2 - Value is greater than root
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Contains
    def contains(self, target):
        # Case 1 - if self.value is target. return True
        if self.value == target:
            return True
        # Case 2 - if self.value is greater than target
        if self.value > target:
            # if self.left is None - its not in the tree
            if self.left is None:
                return False
            # else self.left contains target
            else:
                return self.left.contains(target)
        # Case 3 - Otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode(names_1[0])
for names_in_file_1 in names_1:
    bst.insert(names_in_file_1)
for names_in_file_2 in names_2:
    if bst.contains(names_in_file_2):
        duplicates.append(names_in_file_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
