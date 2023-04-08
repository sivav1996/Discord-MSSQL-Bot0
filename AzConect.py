import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\MSSQLSERVER01;'
                      'Database=APEX_DATA;'
                      'Trusted_Connection=yes;')


def insert_data(param1, param2, param3, param4, param5, param6):
    cursor = cnxn.cursor()
    query = "INSERT INTO dbo.acc_login (USERNAME, EMAIL, PASS_W, PLATFORM_APEX, OWNER,STAT) VALUES (?, ?, ?,?,?,?)"
    cursor.execute(query, param1, param2, param3, param4, param5, param6)
    cnxn.commit()
    cursor.close()


def get_account_info(person_id):
    cursor = cnxn.cursor()
    cursor.execute(
        f"SELECT USERNAME, EMAIL, PASS_W, PLATFORM_APEX, OWNER,STAT FROM dbo.acc_login Where CHARINDEX('{person_id}', concat(username,stat,owner,email)) > 0")
    rows = cursor.fetchall()
    data_str = ''
    for row in rows:
        data_str += f"""{{
Username\t->{row[0]} 
Email\t\->{row[1]} 
Password\t->{row[2]}
Platform\t->{row[3]} 
Provider\t->{row[4]} 
Status\t->{row[5]}
}}
"""'\n'
    if data_str == '':
        return 'No record found'
    else:
        return data_str


def get_data():
    cursor = cnxn.cursor()

    cursor.execute(
        "SELECT USERNAME, EMAIL, PASS_W, PLATFORM_APEX, OWNER,STAT FROM dbo.acc_login")
    rows = cursor.fetchall()

    # Convert the rows to a string
    data_str = ''
    for row in rows:
        data_str += f"""{{
Username\t->{row[0]} 
Email\t\->{row[1]} 
Password\t->{row[2]}
Platform\t->{row[3]} 
Provider\t->{row[4]} 
Status\t->{row[5]}
}}
"""'\n'

    return data_str
