from flask import Flask     #, escape
# from markupsafe import escape
from db import *

app = Flask(__name__)

@app.get("/register")
def get_register():
    return f'get register'

@app.post("/register")
def post_register():
    return f'user registered'

@app.get("/user")
def get_user():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('select login, phone, birth_date from users')
    res = cur.fetchone()
    user_phone = res[1]
    birth_date = res[2]
    return {"phone"}

@app.post("/user")
def post_user():
    return f'post user'

@app.put("/user")
def put_user():
    return f'put user'

@app.get("/user/funds")
def get_user_funds():
    return f'get user funds'

@app.post("/user/funds")
def post_user_funds():
    return f'post user funds'

@app.get("/user/reservations")
def get_user_reservations():
    return f'get user reservations'

@app.post("/user/reservations")
def post_user_reservations():
    return f'post user reservations'

@app.get("/user/reservations/<reservation_id>")
def get_user_reservation_id(reservation_id):
    return f'get user reservation {reservation_id}'

@app.post("/user/reservations/<reservation_id>")
def post_user_reservation_id(reservation_id):
    return f'post user reservation {reservation_id}'

@app.delete("/user/reservations/<reservation_id>")
def delete_user_reservation_id(reservation_id):
    return f'delete user reservation {reservation_id}'

@app.get("/user/order")
def get_user_checkout():
    return f'get user checkout'

@app.post("/user/order")
def post_user_checkout():
    return f'post user checkout'

@app.put("/user/order")
def put_user_checkout():
    return f'put user checkout'

@app.get("/fitness_center")
def get_fitness_center():
    return f'get fitness center'

@app.get("/fitness_center/<gym_id>")
def get_fitness_center_id(gym_id):
    return f'get fitness center {gym_id}'

@app.get("/fitness_center/<gym_id>/trainer")
def get_trainer(gym_id):
    return f'get gym {gym_id} -- trainer'

@app.get("/fitness_center/<gym_id>/trainer/<trainer_id>")
def get_trainer_id(gym_id, trainer_id):
    return f'get gym {gym_id} -- trainer {trainer_id}'

@app.get("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def get_trainer_rating(gym_id, trainer_id):
    return f'get gym {gym_id} -- trainer {trainer_id} rating'

@app.post("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def post_trainer_rating(gym_id, trainer_id):
    return f'post gym {gym_id} -- trainer {trainer_id} rating'

@app.put("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def put_trainer_rating(gym_id, trainer_id):
    return f'put gym {gym_id} -- trainer {trainer_id} rating'

@app.get("/fitness_center/<gym_id>/services")
def get_services(gym_id):
    return f'get gym {gym_id} services'

@app.get("/fitness_center/<gym_id>/services/<service_id>")
def get_service_id(gym_id, service_id):
    return f'get gym {gym_id} -- service {service_id}'

@app.get("/fitness_center/<gym_id>/loyalty_programs")
def get_loyalty_programs(gym_id):
    return f'get loyalty programs -- gym {gym_id}'

if __name__ == 'main':
    app.run()
