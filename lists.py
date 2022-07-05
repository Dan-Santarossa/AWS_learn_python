###Lists
#A list is an ordered sequence of values separated by spaces. For example:
#[0,1,2,3,4] or ["apples","oranges","bananas"]
#A list can contain other objects, for example dictionaries, which we learned about in the last lesson. For example:
#[{"fruit_type":"apples"},{"number":50}]

###Creating, Reading, Updating and Deleting elements in a list
###Create
#Lists can be created by assigning the values you want to store in a list to a variable, for example:

fruit = ["apples","oranges","bananas"]

#or if you are going to be adding the contents of the list later, you can declare an empty list. You can create an empty list in two ways:

#Assigning [] to a variable, for example:

#fruit = []

#or use the list() constructor:

#fruit = list()

###Read
#Objects stored in list are given an index number starting at 0. 
#To read an element from a list you use the index number of the stored value.
#Try the following:

print(fruit[1])

#You can find the length of a list using len(). Try the following:

print(len(fruit))

#You can return the last value in a list or work backwards from the last item using a negative index value. For example to return the last value in the list
#Try the following:

print(fruit[-1])
print(fruit[-2])
print(fruit[-3])

###Update
#Lists are mutable, which means they can be changed after you create them. 
#You can add, update, delete and reorder elements in a list.
#You can use append() to add an element to the end of the list.
#Try the following:

fruit.append("kiwi")
print(fruit)

#If you want add an element at a specific point in the list you can use the index value with the insert() method.
#Try the following:

fruit.insert(2, "pear")
print(fruit)

###Organizing a list
#The elements in a list are not sorted automatically.
#If you want to return information which is sorted, but retain the original order of the list, you can use the sorted() function.
#Try the following:

print(sorted(fruit))

#If you want to permanently sort the list, you should use the sort() method.
#Try the following:

fruit.sort()
print(fruit, "<Permanently sorted with sort() method")

#To reverse the order of a list you can use the reverse() method. This will permanently reverse the order of the list.
#Try the following:

fruit.reverse()
print(fruit, "<Reversed after permanent sort with reverse() method")
#^^^To undo this action. you would just use reverse() again to restore the original order.^^^

#Delete
#You can remove elements from a list using the del statement if you know the index position.

del fruit[1]
print(fruit, "<Removed element 'oranges' from list using del statement")

#If you use del the element is deleted, so you can no longer use it, for example if you had a list of users, you might want to delete a user.
#If you want to use the value after removing it from a list you use the pop() method. 
#To use pop(), you need to store the value you have removed from the list inside another variable.
#Try the following:

fav_fruit = fruit.pop()
print(fav_fruit, "<pop() has returned the last element in the list, which is the default")

#You can return any element with the pop() by using the index value.
#Try the following:

fresh_fruit = fruit.pop(2)
print(fresh_fruit, "<pop() with value added")

#If you don't know the index position, or you don't want to remove the last item in the list, 
#you can use the remove() method to specify the value of the element you want to remove.
#Try the following:

fruit.remove('kiwi')
print(fruit)

#Remember that when you use del, pop() or remove(), the element is permanently deleted from the original list. 
#If the list is printed out, you will see that those elements are no longer stored in the list.

#Summary
#As you will see in later labs, learning to use dictionaries and lists will significantly enhance your knowledge of how to use some features in AWS.