# Interpolation
unit_price = 165.78
quantity = 5 
total_price = unit_price * quantity 
phrase = "The product costs %f. I bought %d. I paid in total %f" % (unit_price, quantity, total_price)
print(phrase)

unit_price = 165.78
quantity = 6 
total_price = unit_price * quantity 
phrase = f"The product costs {unit_price}. I bought {quantity}. I paid in total {unit_price * quantity}"
print(phrase)

# Create a program that has two variables named first_name and last_name.
# Ask the user to input the first name and then ask to input the last name and store them in the variables separately.
# Create a variable named full_name and store the concatenated first and last names.
# At the end of the program print the phrase:
# Your full name is: FIRSTNAME LASTNAME
# Where FIRSTNAME and LASTNAME is the content of the full_name variable.

first_name = input("First name: ")
last_name =  input("Last name: ")
full_name = first_name + " " + last_name
phrase = f"Your full name is: {full_name}"
print(phrase)

# Create a program that asks the user for a word and stores
# this word in a variable named 'word'.
# Then print the content of the variable 20 times using string multiplication.
# Remember to put a space so the words don't print "stuck together".

word = input("Enter a word: ")
print((word + ' ') * 20)

product_name = input('Enter the name of the product: ')
price = float(input('Enter the price of the product: '))
quantity = int(input('Enter the quantity of products: '))

total = price * quantity

print('The product %s costs R$ %.2f, you bought %d and will pay R$ %.2f' % (product_name, price, quantity, total))

# e strings - Lesson 2
# Learning more about strings

email = "evaldowolkers@gmail.com"
at_index = email.index("@")
username = email[0:at_index]
print ("The username is:", username)

# The provider's name
email = "evaldowolkers@gmail.com"
at_index = email.index("@")
dot_index = email.index(".")
provider = email[at_index+1:dot_index]
print ("The provider's name is:", provider)

# another exercise
# What is the result of the following code if the user enters the email maria.silva@teste.com.br?

email = input("Enter your email: ")

var1, var2 = email.split("@")
# var1 = maria.silva, 
# var2 = teste.com.br 
var3, var4 = var1.split(".")
# var3 = maria
# var4 = silva 

var5, var6, var7 = var2.split(".")
# var5 = teste
# var6 = com 
# var7 = br

print(f"var3: {var3}\n"
      f"var4: {var4}\n"
      f"var5: {var5}\n"
      f"var6: {var6}\n"
      f"var7: {var7}\n")
