from db.run_sql import run_sql 

from models.user import User 


def save(user):
    sql = "INSERT INTO users (name, job) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.job]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id 
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['job'], row['id'])
        users.append(user)

    return users

def select(id):
    user = None 
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['job'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)
        

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET(user_id, name, job) = (%s, %s, %s) WHERE id = %s"
    values = [user.name, user.job, user.id]
    run_sql(sql, values)