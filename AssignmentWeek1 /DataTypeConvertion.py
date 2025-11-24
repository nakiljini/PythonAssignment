
#1 .Task: Convert the following values to the specified types and print the results

#Convert 3.75 to an integer and print the value

val =3.75
intValue=int(val)
print(intValue)

#Convert "123" to a float and print the value

val ="123"
floatValue=float(val)
print(floatValue)

#Convert 0 to a boolean and print the value

val =0
boolValue=bool(val)
print(boolValue)

#Convert False to a string and print the value
val = False
strValue = str(val)
print(strValue)



# 2. Convert all characters in the string to uppercase. x = "hello"
x="hello"
upperCaseValue=x.upper()
print(upperCaseValue)

#3. Given x = 5 and y = 3.14, calculate z = x + y and determine
# the data type of z. And convert it to integer.

x = 5
y = 3.14
z = x + y
print(type(z))
print(int(z))

#4. Given the string s = 'hello', perform the following operations:
#Convert the string to uppercase.

s = 'hello'
upperCaseValue=s.upper()
print(upperCaseValue)
#Replace 'e' with 'a'.

replaceString=s.replace('e', 'a')
print(replaceString)


#Check if the string starts with 'he'.

startWithString =s.startswith('he')
print(startWithString)

#Check if the string ends with 'lo'.

endWithString = s.endswith('lo')
print(endWithString)