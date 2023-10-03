
# coding: utf-8

# # Data Types and Functions in Python
# 
# **_Author: Jessica Cervi_**
# 
# **Expected time = 1.5 hrs**
# 
# **Total points = 120 points**

# ## Assignment Overview
# 
# 
# In this assignment, you will work with the Python data types you learned in Module 2, such as integers, floats, booleans, lists, tuples, and dictionaries. You will also practice using comparison and logical operators. In the second half of the assignment, you will apply what you have learned in Module 3 to use built-in and user-defined functions. You will also work with loops and conditional statements. Before you begin the assignment, review the instructions below and complete Question 0 to practice using Vocareum.
# 
# 
# This assignment is designed to build your familiarity and comfort coding in Python while also helping you review key topics from each module. As you progress through the assignment, answers will get increasingly complex. It is important that you adopt a data scientist's mindset when completing this assignment. **Remember to run your code from each cell before submitting your assignment.** Running your code beforehand will notify you of errors and give you a chance to fix them before submitting. You should view your Vocareum submission as if you are delivering a final project to your manager or client. 
# 
# 
# ### Learning Objectives
# 
# - Use Jupyter Notebooks to begin programming in Python.  
# - Identify Python data types, including strings, integers, floats, booleans, lists, and tuples. 
# - Explain the operations that can be performed on a given data type.  
# - Examine the benefits and limitations of using lists, tuples, and dictionaries to store and organize your data. 
# - Explain the benefits of functions in performing specified tasks in Python.  
# - Use built-in functions to perform common tasks in Python.  
# - Use methods to perform analyses on specific data types.  
# - Create custom functions to perform custom analyses relevant to the dataset or research question. 

# 
# 
# ## Index:
# 
# ####  Working with data types and operators in Python
# 
# - [Question 1](#Question-1)
# - [Question 2](#Question-2)
# - [Question 3](#Question-3)
# - [Question 4](#Question-4)
# - [Question 5](#Question-5)
# - [Question 6](#Question-6)
# - [Question 7](#Question-7)
# - [Question 8](#Question-8)
# - [Question 9](#Question-9)
# - [Question 10](#Question-10)
# - [Question 11](#Question-11)
# - [Question 12](#Question-12)
# - [Question 13](#Question-13)
# 
# 
# ####   Writing functions in Python
# - [Question 14](#Question-14)
# - [Question 15](#Question-15)
# - [Question 16](#Question-16)
# - [Question 17](#Question-17)
# - [Question 18](#Question-18)
# - [Question 19](#Question-19)
# - [Question 20](#Question-20)

# ## Instructions:
# 
# All the questions in the assigments will be graded automatically and you will have the chance to fix your solutions many times in order to get the expected output. Make sure to follow the steps carefully (and don't delete or change anything unless you're asked to).
# 
# Question 0 is designed and solved for you to understand how to complete this and the next assignments. You will see this question appear in your grading report. It's worth 0 points so you can just ignore it.
# 
# Below you can see the structure of the questions. In the markdown cell just before the question, you will see the question number and the description of what has been asked. 
# 
# Next, there is a code cell starting with the comment: `### YOUR ANSWER BELOW`. This means that the cell will  be autograded.
# 
# The line `###BEGIN SOLUTION` tells you where to write your solution. You can use as many auxiliary variables and additional codes as you need. Note that we have already initialized the answer variables that you will need for you final answer and assigned them the placeholder value `None`. This is to avoid errors when typing the variable names that contain the results. You can replace the value `None` with the actual answer or redefine it below.
# 
# Finally, you will see a second code cell with the autograded solution. **DO NOT CHANGE ANYTHING IN THAT CELL**
# 
# 
# ### Question 0:
# Assign the String `"hello"` to the variable `var`:
# 

# In[1]:


### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
var = "hello" ## edit code here, i.e., set var = "hello"
print(var)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER CELL - DO NOT REMOVE
###


# 
# ##  Working with data types and operators in Python
# 
# In the first part of this assignment, we will be testing your knowledge of the topics covered in Module 2, such as basic data types (`int`, `floats`, and `str`) as well as lists, tuples, and dictonaries.

# ## Floats
# 
# As you have learned, float are data types designed to store decimal numbers.
# 
# [Back to top](#Index:) 
# 
# ### Question 1
# 
# *5 points* 
# 
# 
# Assign the value of 175 multiplied by 16.28 to the variable `ans1` and make sure it's stored as a float.

# In[2]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans1 = 175*16.28
print(ans1)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 2
# 
# *5 points* 
# 
# Assign the value of 572 divided by 8.73 to the variable `ans2` and make sure it's stored as a float.

# In[3]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans2 = 572/8.73
print(ans2)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Strings
# 
# Strings are data types designed to contain single characters or a series of them, such as words or sentences.
# 
# Note that Python can't guess at the meaning of strings, it just understands strings as sequences of characters. This means that two seemingly equal strings like `"Hello world"`, `"hello world"`, and `"hello world "` (note the extra space at the end) appear to be different to Python, since they are composed of different characters. In this example, for instance, we can see how Python is case-sensitive and how the space is treated like any other character. In the same vein, Python can't solve typos.
# 
# [Back to top](#Index:)  
# 
# ### Question 3
# 
# *5 points* 
# 
# Assign the sentence "I am a student" as a string to the variable `ans3`.

# In[4]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans3 = "I am a student"
ans3
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Converting Data Types
# 
# As you have learned, int are data types designed to store integer numbers.
# 
# [Back to top](#Index:) 
# 
# ### Question 4
# 
# *5 points* 
# 
# Take the value of 25.927, convert it to an integer, and assign the result to the variable `ans4`.

# In[5]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans4 = int(25.927)
ans4
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Lists
# 
# In Python, a list is a collection of elements which is **ordered** and **mutable** (it can be changed). Lists can contain any data type such as integers, floats, strings, and even other lists.
# 
# If needed, we can even define a list without any elements in it. This is called an *empty list* and is used when we want to add elements to it in the future.
# 
# ```
# example_list = [1, 2, 3]
# empy_list = []
# ```
# 
# [Back to top](#Index:) 
# 
# ### Question 5
# 
# *5 points* 
# 
# Create a list with the numbers `1,4,9,16,25`, in that order, and assign it to a variable called `list_1`.

# In[6]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
list_1 = [1,4,9,16,25]
list_1
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 6
# 
# *5 points* 
# 
# Create a list with the elements: `1, "Hello", 14, 5.6`, in that order, and assign it to a variable called `list_2`. 

# In[7]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
list_2 = [1, "Hello", 14, 5.6]
print(list_2)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# It is also possible to define nested lists (i.e., a list inside another list). Additionally, lists can have repeated elements.
# 
# [Back to top](#Index:) 
# 
# ### Question 7
# 
# *5 points* 
# 
# Given `list_3 = [3,4,5]`, create a nested list that includes the elements `"Columbia", 11, 24.5, 3, list_3`, in that order, and assign it to a variable called `list_4`.

# In[8]:


### GRADED
### YOUR ANSWER BELOW
list_3 = [3,4,5]

### YOUR SOLUTION HERE
list_4 = ["Columbia", 11, 24.5, 3, list_3]
print(list_4)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# You can access the list items by referring to the index number. Remember, Python starts counting from 0, **not 1**. Additionally, negative indexing means beginning from the end: -1 refers to the last item, -2 refers to the second last item, etc.
# 
# [Back to top](#Index:) 
# 
# ### Question 8
# 
# *5 points* 
# 
# Given `list_5 = [3,4,5,6,7,8,9]`, access the last element of the list and assign it to the variable `list_5_elem`.

# In[12]:


### GRADED
list_5 = [3,4,5,6,7,8,9]
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
list_5_elem = list_5[6]
print(list_5_elem)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:)  
# 
# ### Question 9
# 
# *5 points* 
# 
# Define `list_6 = [10,20,30,"Hello", 5.82,1,"student", "Python"]` and delete the third last element on the list.

# In[19]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
list_6 = [10,20,30,"Hello", 5.82,1,"student", "Python"]

del list_6[-3]
print(list_6)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Tuples
# 
# A tuple is a collection which is **ordered** and **unmutable** (it can't be changed once it has been created). In the same way as lists, tuples allow duplicate members.
# 
# [Back to top](#Index:) 
# 
# ### Question 10
# 
# *5 points* 
# 
# Create a tuple with elements from 10 to 20 and assign it to the variable 'tuple_1'. Get the first three values and assign them to a variable called `sliced_tuple_1`.

# In[26]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
tuple_1 = (10,11,12,13,14,15,16,17,18,19,20)
print(tuple_1)
sliced_tuple_1 = tuple_1[:3]
print(sliced_tuple_1)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Dictionaries
# 
# A very important data type in Python is dictonary. A dictionary is a collection which is mutable and indexed (we access its elements using a key, instead their position in the dictionary). 
# 
# A dictionary holds a `key: value` pair. Each key and its corresponding value are separated by a `:`, whereas each key-value pair in the dictionary is separated by a `,`. Keys in a dictonary must be unique, but values can repeat themselves.
# 
# ```
# {key1: value1, key2: value2, ..., keyN: valueN}
# ```
# 
# As with lists, *empty dictionaries* can also be defined for later use if we don't fill them with any value.
# ```
# empty_dict = {}
# ```
# 
# [Back to top](#Index:) 
# 
# ### Question 11
# 
# *5 points* 
# 
# Create a dictionary with a key "name" with value "Andrew" and a key "age" with value 25. Assign it to a variable called `dict_1`.

# In[1]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
dict_1 = {"name":"Andrew", "age":25}
dict_1
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 12
# 
# *5 points* 
# 
# Create a new key `"city"` in `dict_1` and assign the value `"Seattle"` to it.

# In[3]:


### GRADED
### YOUR ANSWER BELOW
dict_1["city"]="Seattle"
### YOUR SOLUTION HERE
print(dict_1)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 13
# 
# *5 points* 
# 
# Change the value of `"city"` to `"New York"` in `dict_1`. 

# In[5]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
dict_1['city']= 'New York'
dict_1
       
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ##  Writing functions in Python
# 
# In the second part of this assignment, we will be testing your knowledge of the topics covered in Module 3, such as Python built-in functions, user-defined functions loops, and conditional statements.
# 
# 
# ## Methods Scripts
# 
# A function is a bundle of code which only runs when it is called. Python comes with many built-in functions. You can find a list of the functions that come with Python [here]( https://docs.python.org/3/library/stdtypes.html).

# [Back to top](#Index:) 
# 
# ### Question 14
# 
# *5 points* 
# 
# Assign -25.82 to the variable `ans14` and take the absolute value.

# In[1]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans14 = -25.82
ans14=abs(ans14)
print(ans14)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 15
# 
# *5 points* 
# 
# Assign the string "I live in the US" to the variable `ans15`. Next, using the appropriate string method, change all the characters to lower-case letters. Don't forget to assing the result of this operation back to `ans15`.

# In[3]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
ans15 =  "I live in the US"

ans15= ans15.lower()
print(ans15)
###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Conditional if statements
# 
# 
# Sometimes you want your function to do one thing under one condition and another thing under another condition. We can specify this in the function body using the keywords `if`, `else`, and `elif`. 

# [Back to top](#Index:) 
# 
# ### Question 16
# 
# *5 points* 
# 
# Given `num_1`, `num_2`, and the list `values`, write a program that appends the boolean `True` to `values` if `num_1` is less than 0, and appends `False` to values if `num_2` is greater than 0.

# In[6]:


### GRADED

num_1 = -738.9
num_2 = 11
values = []

# Combine two if statements and append the desired elements to an empty list
if num_1 < 0:
    values.append(True)
if num_2 > 0:
    values.append(False)
    
    
print(values)


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## Foor loops
# 
# For loops work on iterable objects.  An iterable object is an object that returns its members one at a time. 
# 
# 
# [Back to top](#Index:) 
# 
# Another basic operator in Python is the remainder function. The corresponding symbol is `%`. This function returns the remainder when first operand is divided by the second
# 
# ### Question 17
# 
# *10 points* 
# 
# Create a program that iterates using a **for loop** over all values of `list_mod`. The program must check each value and append the boolean `True` to the list `result` if the value is even or append the boolean `False` to the list result otherwise.

# In[8]:


### GRADED
### YOUR ANSWER BELOW

list_mod = list(range(1,15))
result = []

### YOUR SOLUTION HERE
for value in list_mod:
    if value % 2 == 0:
        result.append(True)
    else:
        result.append(False)

result


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 18
# 
# *10 points*  
# 
# Given the list `time`, with elements from 7 to 24, use a **for loop** to iterate over it and create a program that appends the string `"Good morning"` to `result_time` if the element in the list `time` is less than or equal to 12, appends `"Good afternoon"` if the element is grater than 12 and less than 20, and appends `"Good night"` otherwise.

# In[27]:


### GRADED
### YOUR ANSWER BELOW

time = list(range(7,25))
result_time = []

### YOUR SOLUTION HERE
for value in time:
    if value <= 12:
        result_time.append("Good morning")
    elif value < 20:
        result_time.append("Good afternoon")
    else:    
        result_time.append("Good night")
###
### YOUR CODE HERE
###
print(result_time)


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# ## User-defined Functions
# 
# As you write more complicated code, built-in Python functions won't be enough. For this reason, Python allows you to create user-defined function. Function are defined using the `def` keyword followed by the name of the function and the arguments you need to pass.
# 
# 
# Arguments are specified after the function name, inside parentheses and a colon is needed after the arguments. You can add as many arguments as you want, just separate them with a comma. Finally, after you wrote the block of instructions you want your function to perform, return a value using the `return` keyword. This will make that value accessible outside the function. Note that the bundle of instructions and the return statement need to be **indented**.

# [Back to top](#Index:) 
# 
# ### Question 19
# 
# *10 points* 
# 
# Create a function called `validate` that takes a number as an argument and checks whether it's even. If it's even, return the string `"even"`; if it's odd, return the string `"odd"`. Keep in mind that, in Python strings, case-sensitivity matters.

# In[34]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE

def validate(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
    

###
### YOUR CODE HERE
###

# Example usage:
x = 7
result = validate(x)
print(f"The number {x} is {result}.")


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# [Back to top](#Index:) 
# 
# ### Question 20
# 
# *10 points*  
# 
# Create a function called `abs_value` that takes a number as an argument and returns its absolute value.

# In[35]:


### GRADED
### YOUR ANSWER BELOW

### YOUR SOLUTION HERE
def abs_value(x):
   return abs(x)

# Example usage:
x = -5
result = abs_value(x)
print(f"The absolute value of {x} is {result}.")

###
### YOUR CODE HERE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###

