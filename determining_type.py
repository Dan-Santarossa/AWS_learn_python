###Determining Type
#Sometimes your code will raise a TypeError. These can be frustrating to fix. 
#The first step is often to find out what type of data python thinks the object is.
#The way to find out what type of data python has stored in a variable is to use the type() method.
#In the python IDE try the following:

my_variable = "A string"
print(type(my_variable)) #This should return: 1 <class 'str'>

#Once you know the type data, you can fix the issue by being explicit about how you want python to treat the data.
#Here is an example of a TypeError below.

my_number = 50
some_string = "The number is "
#print(some_string + my_number)
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#TypeError: can only concatenate str (not "int") to str

#Here is how we can fix the TypeError by telling python to convert my_number to a string.
print(some_string + str(my_number))