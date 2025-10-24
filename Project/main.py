from doctors import add_doctor,doctor_details,check_availability
from patients import reg_patient,get_patient_history
from appointment import book_appointment,cancel_appointment,view_schedule,generate_daily_app,appointment




def show_menu():
      print('''
              1.Add Doctor
              2.Register Patient
              3.Book Appointment
              4.Cancel Appointment
              5.View Doctors Schedule
              6.View Patient History
              7.Generate Daily Appointment_list
              8.Check Doctor Availability
              9.View All Appointments
              10.All doctors list
              11.Exit

''')



def main():
    while True:
         show_menu()
         choice=input("enter your choice : ")
         if choice == "1":
             d_id =  input("enter doctor id : ").strip()
             name =  input("enter doctor name : ").strip().title()
             speciality = input("enter doctor speciality :")
             avail = input("Please Provide Doctor's Available Days: ").strip().title()
             add_doctor(d_id,name,speciality,avail)
        
         elif choice == "2":
             p_id = int(input("enter patient id : "))
             p_name = input("enter patient name : ")
             age = int(input("enter your age : "))
             contact = int(input("enter yur contact details : "))
             reg_patient(p_id,p_name,age,contact)
         elif choice == "3":
             p_id = int(input("enter patient id : "))
             dr_id=input("enter doctor id : ")
             date=input("enter date : ")
             time=input("enter time : ")
             book_appointment(p_id,dr_id,date,time)
         elif choice == "4":
             p_id=int(input("enter patient id : "))
             cancel_appointment(p_id)
         elif choice == "5":
             d_id=int(input("enter DR.Id :  "))
             date=input("enter date : ")
             if date == date:
                 print(f"Dr.{name} have an appointment on {date}")
             else:
                print( "No Schedule found on that date" )
         elif choice == "6":
             p_id=int(input("enter patient id : "))
             if p_id == p_id:
                 print(f"Patient ID {p_id} details\nName : {p_name}\nAge : {age}\nContact : {contact}: ")
             else:
                 print("Not found ! ")
         elif choice == "7":
             date=input("enter date : ")
             if date==date:
                 print(f"Appointments on {date} :\nDoctor Name : {name}\nPatient Name : {p_name}\nTime : {time}")
             else:
                 print("No appointment todays ")
         elif choice == "8":
             check_availability()
         elif choice == "9":
             view_all_appointments = appointment
             print(view_all_appointments)
         elif choice == "10":
             all_doctors = doctor_details
             print(all_doctors)
         elif choice == "11":
             print("Thank you for choosing DOCMAN Clinic !")
             break
         else:
             print("Invalid option ")
         
   




if __name__ =="__main__":
    main()