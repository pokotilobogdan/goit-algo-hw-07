import AVL_Tree
from colorama import Fore

root = None
keys = [10, 20, 50, 30, -4, 25, 40, 28, 27, -1]
# keys = [1, 2, 3, 4]

for key in keys:
    root = AVL_Tree.insert(root, key)
    # print("Вставлено:", key)
    # print("AVL-Дерево:")
print(root)

# Завдання 1

print(Fore.RED + "Завдання 1:" + Fore.RESET)

def max_node(root):
    while root.right:
        root = root.right
    return root.key

print("Max node is ", max_node(root))


# Завдання 2

print()
print(Fore.RED + "Завдання 2:" + Fore.RESET)

def min_node(root):         # Або просто скористатись AVL_Tree.min_value_node(root), що, виявляється, навіть є в реалізації з конспекту
    while root.left:
        root = root.left
    return root.key

print("Min node is ", min_node(root))


# Завдання 3

print()
print(Fore.RED + "Завдання 3:" + Fore.RESET)

def sum_of_nodes(root):
    
    if root is not None and root.left is None and root.right is None:
        return root.key
    else:
        s = root.key
        s += (sum_of_nodes(root.left) if root.left is not None else 0) + (sum_of_nodes(root.right) if root.right is not None else 0)
        return s
    
print("Сума значень всіх вузлів: ", sum_of_nodes(root))
print()