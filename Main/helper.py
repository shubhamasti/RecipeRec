import mysql.connector as m

con = m.connect(host = "localhost", user = "root", password = "root1234",
                 database = "rrs")

def password_check(username, password):
    cursor = con.cursor()

    cursor.execute('select password from users where username = "'+username+'"')
    passwd = cursor.fetchall()
   
    if (password,) in passwd:
        return username
    return 0

def user_exists(username):
    cursor = con.cursor()
   
    cursor.execute('select username from users')
    users = cursor.fetchall()
    
    if (username,) in users:
        return username
    return 0

def getUserId(username):
    cursor=con.cursor()
    
    cursor.execute('select user_id from users where username="'+username+'"')
    user_id=cursor.fetchall()[0][0]
    return user_id

def signup_input(username, password, veg, allergen_list =  'None' ):
    cursor = con.cursor()
   
    insert = 'insert into users(username, password, veg, allergen_list) values (%s,%s,%s,%s)'
    userdetails = [username, password, veg, allergen_list]
    cursor.execute(insert, userdetails)
    con.commit()

    return username

def checkBookmark(username, rec_id):
    cursor = con.cursor()
    
    query = 'SELECT * FROM bookmarks WHERE rec_id = %s AND user_id = %s'
    values = (rec_id, getUserId(username))
    
    cursor.execute(query, values)
    result = cursor.fetchall()
    
    if result:
        return 1
    return 0

def bookmark(username, rec_id):
    cursor = con.cursor()
    
    query = 'INSERT INTO bookmarks (rec_id, user_id) VALUES (%s, %s)'
    values = (rec_id, getUserId(username))
    
    cursor.execute(query, values)
    con.commit()

def getBookmarks(username):
    cursor = con.cursor()

    user_id = getUserId(username)
    query = 'SELECT rec_id FROM bookmarks WHERE user_id = %s'
    
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    
    return result

def getAllergenList(username):
    cursor = con.cursor()
    
    cursor.execute('select allergen_list from users where username="'+username+'"')
    result = cursor.fetchall()
    if result[0][0] == None:
        return []
    return result[0][0].split(',')

def getUserInfo(username):
    cursor = con.cursor()
    
    cursor.execute('select * from users where username="'+username+'"')
    user_info=cursor.fetchall()[0]
    return user_info

def updateUsername(old_username, new_username):
    cursor = con.cursor()

    query = 'UPDATE users SET username = %s WHERE username = %s'
    values = (new_username, old_username)
    cursor.execute(query, values)
    con.commit()

def updateUserInfo(username, veg, allergens):
    cursor = con.cursor()

    if veg:
        query = 'UPDATE users SET veg = %s WHERE username = %s'
        values = (veg, username)
        cursor.execute(query, values)
        con.commit()
    if allergens == 'None' or allergens == 'NA':
        query = 'UPDATE users SET allergen_list = NULL WHERE username = %s'
        values = (username,)
        cursor.execute(query, values)
        con.commit()
    elif allergens:
        query = 'UPDATE users SET allergen_list = %s WHERE username = %s'
        values = (allergens, username)
        cursor.execute(query, values)
        con.commit()