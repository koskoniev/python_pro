from flask import Flask, request
#, escape
# from markupsafe import escape
# from db import *
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_from_db(query, many=False):
    con = sqlite3.connect('database.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if many:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res

def insert_to_db(query):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()

app = Flask(__name__)

@app.route("/")
def index():
    index_html = """<html>
    <a href=/user>user</a><br>
    <a href=/fitness_center>fitness_center</a><br>
    <a href=/register>get_register</a><br>
    <a href=/fitness_center/1/trainer>fitness_center/1/trainer</a><br>
    <a href=/fitness_center/1/trainer/1>fitness_center/1/trainer/1</a><br>
    <a href=/fitness_center/1/trainer/1/rating>fitness_center/1/trainer/1/rating</a><br>
    <a HREF=https://google.com>search</a><br>
    </html>
    """
    return index_html

    # fitness_center/<gym_id>/trainer/<trainer_id>/rating

@app.get("/register")
def get_register():
    return f"""<form action='/register' method='post'>
      <label for="login">login:</label><br>
      <input type="text" id="login" name="login"><br>
      <label for="password">password:</label><br>
      <input type="password" id="password" name="password"><br>
      <label for="birth_date">birth_date:</label><br>
      <input type="date" id="birth_date" name="birth_date"><br>
      <label for="phone">phone:</label><br>
      <input type="text" id="phone" name="phone"><br><br>
      <input type="submit" value="Submit">
    </form>"""

@app.post("/register")
def post_register():
    form_data = request.form
    insert_to_db(f"""insert into user (login, password, birth_date, phone) 
                values (\'{form_data['login']}\',
                        \'{form_data['password']}\',
                        \'{form_data['birth_date']}\',
                        \'{form_data['phone']}\')""")
    user_name = {form_data['login']}
    return f'user \"{user_name}\" registered'

@app.get("/user")
def get_user():
    res = get_from_db('select login, phone, birth_date from user', True)
    return str(res)

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

@app.get("/user/checkout")
def get_user_checkout():
    return f'get user checkout'

@app.post("/user/checkout")
def post_user_checkout():
    return f'post user checkout'

@app.put("/user/checkout")
def put_user_checkout():
    return f'put user checkout'

@app.get("/fitness_center")
def get_fitness_center():
    res = get_from_db('select name, address from gym')
    return str(res)

@app.get("/fitness_center/<gym_id>")
def get_fitness_center_id(gym_id):
    res = get_from_db(f'select name, address from gym where id={gym_id}', False)
    return str(res)

@app.get("/fitness_center/<gym_id>/trainer")
def get_trainer(gym_id):
    res = get_from_db(f'select * from trainer where gym_id={gym_id}')
    return res

@app.get("/fitness_center/<gym_id>/trainer/<trainer_id>")
def get_trainer_id(gym_id, trainer_id):
    res = get_from_db(f'''select * from trainer 
            where gym_id={gym_id} and trainer_id={trainer_id}''')
    return res

@app.get("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def get_trainer_rating(gym_id, trainer_id):
    res = get_from_db(f'''select * from rating 
            where trainer_id={trainer_id}
            ''')
    return res

@app.post("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def post_trainer_rating(gym_id, trainer_id):
    return f'post gym {gym_id} -- trainer {trainer_id} rating'

@app.put("/fitness_center/<gym_id>/trainer/<trainer_id>/rating")
def put_trainer_rating(gym_id, trainer_id):
    return f'put gym {gym_id} -- trainer {trainer_id} rating'

@app.get("/fitness_center/<gym_id>/services")
def get_services(gym_id):
    res = get_from_db(f'''select * from services 
                where gym_id={gym_id}
                ''')
    return res

@app.get("/fitness_center/<gym_id>/services/<service_id>")
def get_service_id(gym_id, service_id):
    res = get_from_db(f'''select * from services 
                    where gym_id={gym_id} and service_id={service_id}
                    ''')
    return res

@app.get("/fitness_center/<gym_id>/loyalty_programs")
def get_loyalty_programs(gym_id):
    return f'get loyalty programs -- gym {gym_id}'

if __name__ == '__main__':
    app.run()
