import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="demo"
)
cr = conn.cursor()
print("enter 1 for signup ")
print("enter 2 for login ")
choose = int(input("Enter    :   "))
def register_user():
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    city = input("Enter your city: ")
    cr.execute("insert into users (name,username,password,city) values (%s, %s, %s, %s)", (name, username, password, city))
    conn.commit()
    print("Signup successful!")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cr.execute("select * from users where username=%s and password=%s", (username, password))
    result = cr.fetchone()
    if result:
        print("Login successful!")
        print("Welcome", result[1])
    else:
        print("Login failed! Invalid username or password.")

if choose == 1:
    register_user()
elif choose == 2:
    login_user()