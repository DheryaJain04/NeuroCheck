from db.database import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    #clear old data
    cursor.execute("DELETE FROM recommendation")
    cursor.execute("DELETE FROM patient")
    cursor.execute("DELETE FROM doctor")
    conn.commit()

    try:
        # Doctors
        cursor.execute("""
        INSERT INTO doctor VALUES
        (9000000011, 'Dr Anika Sharma', 'anika.sharma@gmail.com', 'Delhi', 'Saket'),
        (9000000012, 'Dr Raj Kapoor', 'raj.kapoor@gmail.com', 'Mumbai', 'Andheri'),
        (9000000013, 'Dr Nidhi Jain', 'nidhi.jain@gmail.com', 'Delhi', 'Janakpuri'),
        (9000000014, 'Dr Arjun Singh', 'arjun.singh@gmail.com', 'Bangalore', 'Indiranagar'),
        (9000000015, 'Dr Priya Gupta', 'priya.gupta@gmail.com', 'Delhi', 'Connaught Place'),
        (9000000016, 'Dr Rohit Mehta', 'rohit.mehta@gmail.com', 'Mumbai', 'Bandra'),
        (9000000017, 'Dr Sanya Malhotra', 'sanya.malhotra@gmail.com', 'Chennai', 'T Nagar'),
        (9000000018, 'Dr Vikram Verma', 'vikram.verma@gmail.com', 'Hyderabad', 'Banjara Hills'),
        (9000000019, 'Dr Ananya Kapoor', 'ananya.kapoor@gmail.com', 'Kolkata', 'Salt Lake'),
        (9000000020, 'Dr Aryan Singh', 'aryan.singh@gmail.com', 'Pune', 'Shivaji Nagar')
        """)
        conn.commit()

        # Patients
        cursor.execute("""
        INSERT INTO patient VALUES
        (8000000011, 'Amit Sharma', 'amit.sharma@gmail.com', 'Delhi', 38),
        (8000000012, 'Payal Patel', 'payal.patel@gmail.com', 'Mumbai', 59),
        (8000000013, 'Rahul Kumar', 'rahul.kumar@gmail.com', 'Delhi', 65),
        (8000000014, 'Neha Singh', 'neha.singh@gmail.com', 'Bangalore', 68),
        (8000000015, 'Rajiv Mehra', 'rajiv.mehra@gmail.com', 'Chennai', 40),
        (8000000016, 'Sneha Reddy', 'sneha.reddy@gmail.com', 'Hyderabad', 55),
        (8000000017, 'Karan Malhotra', 'karan.malhotra@gmail.com', 'Kolkata', 47),
        (8000000018, 'Pooja Iyer', 'pooja.iyer@gmail.com', 'Chennai', 62),
        (8000000019, 'Rohit Jain', 'rohit.jain@gmail.com', 'Pune', 51),
        (8000000020, 'Ankit Gupta', 'ankit.gupta@gmail.com', 'Delhi', 44)
        """)
        conn.commit()

        # Reccommendations
        cursor.execute("""
        INSERT INTO recommendation VALUES
        (8000000011, 9000000011),
        (8000000012, 9000000012),
        (8000000013, 9000000013),
        (8000000014, 9000000014),
        (8000000015, 9000000017),
        (8000000016, 9000000018),
        (8000000017, 9000000019),
        (8000000018, 9000000017),
        (8000000019, 9000000020),
        (8000000020, 9000000015)
        """)
        conn.commit()
    
    except Exception as e:
        print("Seeding error:", e)

    finally:
        cursor.close()
        conn.close()