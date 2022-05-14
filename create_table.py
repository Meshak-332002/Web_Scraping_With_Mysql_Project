#import MySQLdb 
#db = MySQLdb.connect("127.0.0.1","scraping_sample","Sc_Python_Web43","scraping_sample")
import mysql.connector

cnx = mysql.connector.connect(user='scraping_sample',
                             password='Sc_Python_Web43',
                             host='127.0.0.1',
                             database='scraping_sample')
cursor =cnx.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError, msg:
            print "Command skipped: ", msg

executeScriptsFromFile('D:\Python_Repo\Project\MySQL-Python-Web-Scraping\Scripts')
cnx.commit()
