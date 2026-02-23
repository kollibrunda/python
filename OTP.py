import random
otp=random.randint(100000, 999999)
print("your OTP is:",otp)
entered_otp=int(input("enter the OTP:"))
if entered_otp==otp:
    print("OTP is veriied succesfuly")
else:
    print("invalid otp.please try again.")

