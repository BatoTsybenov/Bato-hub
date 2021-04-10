fullname = "John doe"
msg = "we are looking at string functions in Python."
print(fullname.strip())
print(fullname.upper())
print(fullname.title())
print(msg.replace('.' , '!!!!!!!').title())
print(msg.replace('Python','Bato'))

msg1 = fullname.title() + ", " + msg
print(msg1)
print(fullname.upper() + ", " + msg)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(fullname.upper() + "\t\t\t, " + msg)
msg2 = fullname.title() + " \n\t\t\t" + msg
print(msg2)
print(msg2.replace('\t', ''))
print((msg2.strip()))

msg3 = '\n\t\t\t' + fullname.title() + ", " + msg
print(msg3)
print(msg3.strip())
print('*************************')
msg3 = '\n\t\t\t' + fullname.title() + ", " + msg
msg4 = f"{fullname.title()} , {msg} cool day i believe"
print("fstring")
print(msg4.strip() + '!!!!')

num = 456
num2 = 600
print(num + num2)
print(num / num2)
print(num - num2)
print(f"num + num2 = {num + num2}")

print("value of num is : " + str(num))
print("num + num2 = " + str(num +num2))

num3 = "753"
print(f"num + num3 = {num + int(num3)}")
print(f"4 ** 2 = {4**2}")

num4 = 45.55
print(f"num + num2 = {num + float(num4)}")

print(int(45.4988))






#06/02/2021
# https://www.integralist.co.uk/posts/data-types-and-data-structures/
# https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42
print(16/2)
#arrays




