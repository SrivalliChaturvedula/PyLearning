user_type = input("Enter user type: ")
match user_type:
    case "admin":
        print("Hello!!!")
    case "guest":
        print("Hello sir")
    case _:
        print("Hello there")