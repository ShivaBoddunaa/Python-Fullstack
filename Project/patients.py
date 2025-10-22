patient=[{
    
   "p_id": "001",
   "name" : "janu",
   "age" : "23",
   "contact" : "23456"
}, 
{ 
   "p_id": "002",
   "name" : "nilofer",
   "age" : "24",
   "contact" : "234567"
 
 
}]


def reg_patient(p_id,p_name,age,contact):
    patient.append({
       "patient_id": p_id,
       "name" : p_name,
       "age" : age,
       "contact" : contact
})
    print("Patient detials register successfull!")
    
    


def get_patient_history(p_id):
   patient.append({
      
      "patient_id" : p_id      
 })
    
    
    
    
