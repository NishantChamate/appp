import firebase_admin
from firebase_admin import db, credentials

# Authenticate to Firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://qwerty-64a73-default-rtdb.asia-southeast1.firebasedatabase.app/"})

# Creating reference to root node
ref = db.reference("/calculations")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def store_result(operation, num1, num2, result):
    ref.push({
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    })

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        store_result("Addition", num1, num2, result)
    elif choice == '2':
        result = subtract(num1, num2)
        store_result("Subtraction", num1, num2, result)
    elif choice == '3':
        result = multiply(num1, num2)
        store_result("Multiplication", num1, num2, result)
    elif choice == '4':
        result = divide(num1, num2)
        store_result("Division", num1, num2, result)
    else:
        result = "Invalid input"
    
    print("Result:", result)