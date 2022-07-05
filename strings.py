#In python a string, is shortened to str and refers to anything inside quotes. 
#The quotes can be double or single. The examples below are identical to python.

"A hunter should hunt beasts. Leave the hunting of hunters to me"
'A hunter should hunt beasts. Leave the hunting of hunters to me'

#If you want to include a direct quote in your sentence, 
#then use single quotes for the string and double quotes for the direct quote. 

'The error message was "Incorrect DataType"'

#This allows you the flexibility to use single quotes to wrap the string and double quotes inside the string for a direct quote, without python getting confused.
#Strings, like all data types, can be assigned to a variable.

first_name = "Dan"
last_name = "Santarossa"

#You can add strings together using variables. This concatenates them.

print(first_name+last_name)
print(first_name + " " + last_name)

#Using Variables in Strings
#Imagine we want to use the value of a variable in the middle of a string. This can be done a few ways in python.

#.format()
#In this method you can use the {} in your string to indicate where the variable should go. 
#Then use .format(variable_name) after the quotation marks. 
#If you have multiple variables, for each variable you use a {}. 
#In the .format() separate each variable with a comma. For example .format(variable_1, variable_2).
#Try this in the interactive python. Type or paste each line after the

print("My first name is {}. My last name is {}".format(first_name, last_name))

#New Lines and indentation
#If you want your text to go over several lines you can use \n and \t. The \ character is called an escape character.

#The n tells python to put the text on the next line.
#The t tells python to add a tab spacing.

str = "Acts of goodness are not always wise\nand acts of evil are not always foolish\n\tbut regardless, we shall always strive to be good."
print(str)