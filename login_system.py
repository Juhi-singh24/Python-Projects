username = "Juhi Singh"   # Storing the value of username
password = "juhisingh24"  # storing the value of password


for i in range(3):  # Make a loop for taking the value of username and password from user and compare it with stored values.
            
            username_1 = input("Enter the username : ").strip()   # We use strip() function to remove extra spaces
            password_1 = input("Enter the password : ").strip()

            if (username_1 ==username and password_1 == password):   # Checking the credential is filled correct by user or not
            
                print("Acees Granted")
                print("Welcome to home page")
                break
            
            elif (username_1 != username and password_1 == password):  # Checking the condition when password is correct but username is incorrect
                print("Username is incorrect Try Again")
                

            elif (username_1 == username and password_1 != password): # Checking the condition when password is incorrect but usernam eis correct
             print("Wrong password Try Again")
        

            else:                # When both password and username is incorrect
                  print("Wrong Credential")
                  print('Try again')
else:
     
     print("Sorry! Your Account has locked ")
        

        
        


        
    
    

