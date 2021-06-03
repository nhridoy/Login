import psycopg2

### Creating Database ###
Host = 'localhost'
Database = 'user'
User = 'postgres'
Port = '5432'
Password = 'admin'

con = psycopg2.connect(f"dbname='{Database}' user='{User}' password='{Password}' host='{Host}' port='{Port}'")
cur = con.cursor()

### CREATE Date TABLE ###
cur.execute("CREATE TABLE if NOT EXISTS user_data (Full_Name TEXT, Email TEXT, Password TEXT)")
con.commit()


def insertData(u_Name="", u_Email="", u_Password=""):
    ### Getting Email ###
    cur.execute(f"select email from user_data where email = '{u_Email}'")
    mail = cur.fetchall()
    if not mail:
        ### INSERT Date DATA ###
        cur.execute("INSERT INTO user_data (Full_Name, Email, Password) VALUES (%s,%s,%s)", (u_Name, u_Email, u_Password))
        con.commit()
        err = '''<div id="message">
                        <p id="letter" class="valid"><b>Success</b></p>
                    </div>'''
    else:
        err = '''<div id="message">
                        <p id="letter" class="invalid"><b>Email Already Registered Please Login</b></p>
                    </div>'''
    # err = ''''''
    return err
    print(mail)
# insertData()