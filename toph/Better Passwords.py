def password(temp_password):
   
    temp_password=temp_password.replace("s","$")
    temp_password=temp_password.replace("i","!")
    temp_password=temp_password.replace("o","()")
    x=temp_password[0].upper()
    temp_password=x+temp_password[1:]+"."

    return temp_password
temp_password=input().lower()
if len(temp_password) < 16:
    print(password(temp_password))
