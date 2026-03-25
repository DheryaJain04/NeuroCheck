import os
import time
import subprocess
from modules.patient import patient_signup, take_test, view_result, get_recommendation
from modules.doctor import doctor_signup, view_patients
from modules.seed_data import seed_data

def main():
    subprocess.run("cls", shell=True)
    if not os.path.exists("seed_done.flag"):
        seed_data()
        open("seed_done.flag", "w").close()

    print("\nWelcome to NeuroCheck - Alzheimer’s Assessment Tool")
    print("------------------------------------------------------")

    user = input("Are you a DOCTOR or PATIENT: ").strip().lower()
    if user not in ["doctor", "patient"]:
        print("Invalid role! Please restart and choose Doctor or Patient.")
        return

    if user == "patient":
        while True:
            subprocess.run("cls", shell=True)
            time.sleep(2)
            print("\n==============================")
            print("        PATIENT MENU")
            print("==============================")
            print("1. Sign Up")
            print("2. Take Test")
            print("3. View Result")
            print("4. Get Recommendation")
            print("5. Exit")
            
            try:
                ch = int(input("Enter choice: "))
            except:
                print("Please enter a valid number")
                input("Press Enter to continue...")
                continue

            if ch == 1:
                patient_signup()
            elif ch == 2:
                take_test()
            elif ch == 3:
                view_result()
            elif ch == 4:
                get_recommendation()
            elif ch == 5:
                print("Thank you for using NeuroCheck!!")
                break
            else:
                print("Invalid choice")
                input("Press Enter to continue...")
            time.sleep(2)

    elif user == "doctor":
        while True:
            time.sleep(2)
            subprocess.run("cls", shell=True)
            print("\n==============================")
            print("        DOCTOR MENU")
            print("==============================")
            print("1. Sign Up")
            print("2. View Patients")
            print("3. Exit")

            try:
                ch = int(input("Enter choice: "))
            except:
                print("Please enter a valid number")
                input("Press Enter to continue...")               
                continue

            if ch == 1:
                doctor_signup()
            elif ch == 2:
                view_patients()
            elif ch == 3:
                print("Thank you for using NeuroCheck!!")
                break
            else:
                print("Invalid choice")
                input("Press Enter to continue...")  
            time.sleep(2)          

if __name__ == "__main__":
    main()