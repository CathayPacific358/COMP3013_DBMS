# Wu Shuyang 1730026119

import pymysql
# Open database connection
db = pymysql.connect("localhost", "root", "", "test")

# prepare a cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT)"""
cursor.execute(sql)

sql_insert = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
                VALUES('%s','%s',%d,'%c',%d)"""
data = [('Mary', 'Smith', 19, 'F', 1800), ('Gary', 'Lee', 21, 'M', 2000), ('Becky', 'Bucked', 21, 'F', 2800),
        ('Flora', 'Aniston', 17, 'F',2300 )]
try:
    # Execute the SQL command
    for each in data:
        cursor.execute(sql_insert % each)
    # Commit your changes in the database.
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
sql = """ SELECT count(SEX)
       FROM EMPLOYEE
       WHERE SEX = 'F'"""

try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()
    print("There are %d female employee(s) in the company" % results[0])
    print("\n")
except:
    # Print error megs
    print("Error: unable to fetch data")

sql = """SELECT *
       FROM EMPLOYEE
       WHERE AGE<20"""
try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        # Now print fetched result
        print("fname = %s, lname = %s, age = %d, sex = %s, income=%d" %
              (fname, lname, age, sex, income))
except:
    # Print error megs
    print("Error: unable to fetch data")
    print("\n")
sql = """UPDATE employee
       SET INCOME = 2000
       WHERE INCOME <2000"""
try:
    # Execute the SQL command
    cursor.execute(sql)

    # Commit your changes in the database
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()
sql = """SELECT FIRST_NAME,LAST_NAME
       FROM EMPLOYEE
       WHERE INCOME >= 2000"""
try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        # Now print fetched result
        print("fname = %s, lname = %s" %
              (fname, lname))
except:
    # Print error megs
    print("Error: unable to fetch data")
print("\n")
sql = """DELETE FROM EMPLOYEE
       WHERE AGE<18"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    
sql = "SELECT * FROM EMPLOYEE"
try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[0]
        age = row[2]
        sex = row[3]
        income = row[4]

        # Now print fetched result
        print("fname = %s, lname = %s, age = %d, sex = %s, income=%d" %
              (fname, lname, age, sex, income))
except:
    # Print error megs
    print("Error: unable to fetch data")

try:
    # Execute the SQL command
    cursor.execute(sql)

    # Commit your changes in the database
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()
# disconnect from server
db.close()
