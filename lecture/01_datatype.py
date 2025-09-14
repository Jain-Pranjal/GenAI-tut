# in this we will be learning the basic datatypes in python

'''
So everything in python is an object and object has 3 things in it
1. value
2. type
3. id

Always check by the id , not by value
'''
name="pranjal"
print(type(name)) # type
print(id(name)) # id
print(name) # value

# So everything is a object in python and they have 3 properties in them 

"""
Mutable vs Immutable
Mutable -> can be changed like list, dict, set
Immutable -> cannot be changed like int, float, str, tuple
"""

col=233.344
print(type(col))
# so python is smart enough to convert the data type automatically

# reverse the string
print(name[::-1])
# just by adding the -1 we can reverse the string


"""
so here we learn about the dealing with the other than english language so we need to encode them to use in the code 

# Sometime we need to write in any other language and for that we will be using the encode function
"""
name2="प्रांजल"
encoded = name2.encode("utf-8")  # encode to bytes
print(encoded)  # print the encoded bytes
decoded = encoded.decode("utf-8")  # decode the bytes back to string
print(decoded)  # print the decoded string


# TUPLES : they are immutable in nature 
tup=(1,2,3,4,5)
print(type(tup))
print(tup[0]) # accessing the first element of the tuple
# tup[0]=100 # this will give error as tuple is immutable


# LIST:  they are mutable in nature
lst=[1,2,3,4,5]
print(type(lst))
lst.append(6) # adding the element to the list
print(lst)

# AS LIST ARE MUTABLE THEY CHANGE THE ORIGINAL OBJECT  

lst.reverse() # this will reverse the list
print(lst) # original list is changed
# print(lst1) # this will print None as reverse function does not return anything

 

 #OPERATOR OVERLOADING
# so in python we can use the same operator for different data types like + operator is used for both int and str 
'''
so using the same operator for different data types is called operator overloading and it will behave differently based on the data type so thats why we can use the same operator for different data types
'''

# function overriding 
'''With this only we have the function overriding that is done in case of inheritance of class and child class by defining the same function name in both the class and child class '''

# DICT : they are mutable in nature and theu are key value pair
# order dont matter in dict as we can access the value by key 
dct={"name":"pranjal","age":20}
print(type(dct))

dict1={
    "name":"pranjal",
    "age":20,
    "marks":{
        "maths":90,
        "science":95
    }
}



print(dict1["marks"]["maths"]) # accessing the nested dict

# to remove use del
del dict1["age"]
print(dict1)
print(f"is marks key present in dict1 : {'marks' in dict1}") # to check if key is present in dict or not

print(dict1.keys()) # to get all the keys in the dict
print(dict1.values()) # to get all the values in the dict
print(dict1.items()) # to get all the items in the dict

