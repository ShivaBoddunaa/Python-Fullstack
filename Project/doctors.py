doctor_details=[{
    
   "Doctor ID": "1",
   "Doctor Name" : "Ben Akhil",
   "Doctor Speciality" : "dermatologist",
   "Doctor Availability":['Mon','Tue','Wed']
}, 
{ 
   "Doctor ID": "2",
   "Doctor Name" : "Alu Arjun",
   "Doctor Speciality" : "cardiology",
   "Doctor Availability":['Thur','Fri','Sat']
 
 
}]


def add_doctor(d_id,name,speciality,avail):
   avail = avail.split(',')
   doctor_details.append({
       "Doctor ID": d_id,
       "Doctor Name" : name,
       "Doctor Speciality" : speciality,
       "Doctor Availability":avail
       
})
   print("doctor details added successfully!")
   
def all_doctors():
   return doctor_details
# def reg_patient(patient_id,p_name,age,contact):


def check_availability():
   print('='*70)
   for doctor in doctor_details:
      print('='*70)
      for k,v in doctor.items():
         print(f'-{k}: {v}')
# def check_availability(dr_id,date,time):
#    doctor_details.append({
      
      
#    })
    
    