from db.database import get_connection

def doctor_signup():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        city = input("Enter your city: ").strip()
        address = input("Enter your address: ").strip()

        try:
            phone = int(input("Enter your phone number: "))
        except:
            print("Invalid phone number")
            return

        # check duplicate
        cursor.execute("SELECT * FROM doctor WHERE d_number = %s", (phone,))
        if cursor.fetchone():
            print("Doctor already exists!")
            return

        cursor.execute("INSERT INTO doctor VALUES (%s,%s,%s,%s,%s)",(phone, name, email, city, address))
        conn.commit()
        print("Doctor signup successful!")
    finally:
        cursor.close()
        conn.close()


def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        try:
            d_number = int(input("Enter your phone number: "))
        except:
            print("Invalid input")
            return

        # check doctor exists
        cursor.execute("SELECT * FROM doctor WHERE d_number = %s", (d_number,))
        if not cursor.fetchone():
            print("Doctor not found. Please sign up first.")
            return

        query = """
        SELECT p.p_name, p.p_email, p.p_age, p.p_number, r.result
        FROM patient p
        JOIN recommendation rec ON p.p_number = rec.p_number
        JOIN doctor d ON rec.d_number = d.d_number
        JOIN result r ON p.p_number = r.p_number
        WHERE d.d_number = %s
        """
        cursor.execute(query, (d_number,))
        records = cursor.fetchall()

        if not records:
            print("No patients found.")
            return

        print("\nYour Patients:\n")
        for r in records:
            print(r)
    finally:
        cursor.close()
        conn.close()