# from fastapi import FastAPI

# app=FastAPI()

# @app.get('/hello')

# def say_hello(name):
#   return {"Greetiing ":f"hello  {name}"}



from fastapi import FastAPI

app=FastAPI()
users = []

@app.get("/add")
def add_users(name, password):
  users.append({
    
        "username":name,
        "password" :password
      })
  return users
  
@app.get("/delete")
def delete_user(name):
  for user in users:
    if user["username"] == name:
      users.remove(user)
      
@app.get("/all")
def get_all():
  return users



 