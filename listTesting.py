## Lists in Python

list1 = ["Robert", 2, "Robot", 3]
list2 = ["Maggie", 5, "Doha", 7]
list3 = ["Ken", "George", "Alpha", "Ken"]
list4 = [5, 6, 9, 9, 7]

## MUST convert lists to strings using str() function when printing OUTPUT WITH OTHER STRINGS
print("List 1: " + str(list1))
print("List 2: " + str(list2))
print("List 3: " + str(list3))
print("List 4: " + str(list4))
print("")

## Slice operator: Takes the first element in the operation in the operation -
## till the last element but does not include the last element
print("List 1: Sliced elements from index 0 to index 2: " + str(list1[0:3]))
print("List 2: Sliced index from 1 to 2: " + str(list2[1:3]))
print("")

list1.extend(list2) ## Extends list2 onto list1
print("List 1 with extension of List 2: " + str(list1))
list1.append("Tony") ## Adds the element onto the end of the list
print("List 1 with the element \"Tony\" appended on the end of it: " + str(list1))
list2.insert(2, 88) ## Inserts an element into the list with 2 params: index-position, element
print("List 2 insertion of \"88\" in the 2nd index of the list: " + str(list2))
print("List 1 has not added in the insertion of \"88\" into its list after extending List 2 onto it: " + str(list1))
list2.remove(88) ## Remove the element from the list
print("List 2 removal of \"88\" in the list: " + str(list2))
list1.pop() ## Removal of last element in the list
print("List 1 last element \"Tony\" removed: " + str(list1))

## Prints the index of element in the list
print("List 2 element \"Maggie\" retrieved based on index: " + str(list2.index("Maggie")))
print("List 1 extended element \"Maggie\" retrieved based on index: " + str(list1.index("Maggie")))
list1.clear() ## Clears List 1
print("List 1 cleared with clear() function: " + str(list1))
print("")

print(list3)
print("Counting \"Ken\" in List 3: " + str(list3.count("Ken")))

print(list4)
list4.sort() ## List 4 is now sorted into ascending order
print("Sorting list 4 in ascending order: " + str(list4))
list4.reverse()
print("List 4 output in reversed order after being sorted: " + str(list4))

list33 = list3.copy() ## copies attributes of 'list3' to the variable 'list33'
print("Copy of List 3: " + str(list33))

exit()