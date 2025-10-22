 
appointment=[{
   
   "p_id" : "142345",
   "d_id" :  "23456",
   "date" :   "23467",
   "time" :   "346"
   
   
}]    
    
def book_appointment(p_id,dr_id,date,time):
   appointment.append({
      "p_id" : p_id,
   "d_id" :  dr_id,
   "date" :   date,
   "time" :   time
})
   print(f"appointment booked successfull!\nyour id number{p_id}")
   

def cancel_appointment(p_id):
    appointment.clear()
    print(f"appointment : {p_id} is cancel")
    

def view_schedule(d_id,date):
    d_id = appointment.get("d_id")
    date = appointment.get("date")
   #  print(f"Schedule DR.ID {d_id}\n Date: {date}")
    print("Not found any Schedule ! ")
    
    
    
def generate_daily_app(name,p_name,date,time):
   appointment.append({
      
      "name" : name,
      "p_name" : p_name,
      " date ": date,
      "time" : time
      
   })
   


def view_all_appointments():
   return appointment
   
    
    