import time
from db.database import get_connection
from modules.test_engine import run_bnt_test
from modules.analysis import analyze_score

def patient_signup():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        city = input("Enter your city: ")

        try:
            phone = int(input("Enter your phone number: "))
            age = int(input("Enter your age: "))
        except:
            print("Invalid Number input")
            return
        
        #checking duplicate
        cursor.execute("SELECT * FROM patient WHERE p_number = %s",(phone,))
        if cursor.fetchone():
            print("User already exists!")
            return

        query = "INSERT INTO patient VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (phone, name, email, city, age))
        conn.commit()
        print("Signup successful!")
    
    finally:
        cursor.close()
        conn.close()

def take_test():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        try:
            phone = int(input("Enter your phone number: "))
        except:
            print("Invalid input")
            return

        # check if user exists
        cursor.execute("SELECT * FROM patient WHERE p_number = %s", (phone,))
        if not cursor.fetchone():
            print("User not found. Please sign up first.")
            return

        score = run_bnt_test()

        cursor.execute("INSERT INTO result VALUES (%s,%s)", (phone, score))
        conn.commit()

        print("Analyzing", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)

        level,msg = analyze_score(score)
        print("\nYour Score:", score)
        print("Risk Level: ", level)
        print("Details: ", msg)
    finally:
        cursor.close()
        conn.close()

def view_result():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        try:
            phone = int(input("Enter your phone number: "))
        except:
            print("Invalid input")
            return

        cursor.execute("SELECT result FROM result WHERE p_number = %s", (phone,))
        records = cursor.fetchall()

        if not records:
            print("No result found.")
            return
        
        print("Your test history:")
        for i, r in enumerate(records, 1):
            print(f"{i}. Score: {r[0]} | {analyze_score(r[0])}")
    finally:
        cursor.close()
        conn.close()

def get_recommendation():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        city = input("Enter your city: ").strip()

        cursor.execute("SELECT * FROM doctor WHERE LOWER(d_city) = LOWER(%s)", (city,))
        doctors = cursor.fetchall()

        if not doctors:
            print("No doctors found in your city.")
            return

        print("\nAvailable doctors:")
        for d in doctors:
            print(d)

        try:
            phone = int(input("Enter your phone number: "))
            d_number = int(input("Enter your chosen doctor's ID: "))
        except:
            print("Invalid input")
            return
        
        #validate doctor exists
        valid_ids = [d[0] for d in doctors]
        if d_number not in valid_ids:
            print("Invalid doctor selection")
            return

        cursor.execute("INSERT INTO recommendation VALUES (%s,%s)", (phone, d_number))
        conn.commit()
        print("Recommendation saved!")
    finally:
        cursor.close()
        conn.close()