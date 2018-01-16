#Search python file for Compfinder project for Information Retrieval, Fall 2017. Paula Wojcik.
#Do not modify or copy without explicit permission.
#Utilizes SQLite3 for Database.


import sqlite3
from sqlite3 import Error

database="C:\\sqlite\compfinder.db"


class Linko():
	def __init__(self, linkname, numfound, title):
		self.linkname = linkname
		self.numfound = numfound
		self.title = title

def create_connection(database):
	try:
		conn=sqlite3.connect(database)
		return conn
	except Error as e:
		print(e)
	return None


def search(conn, term):
	results=list()
	sql='''SELECT * FROM Articles'''
	cur=conn.cursor()
	cur.execute(sql)

	resultfetch=cur.fetchall()

	for row in resultfetch:
		num=0
		for x in term:
			num+=row[1].count(x)
		if(num>1):
			results.append(Linko(row[2], num, row[0]))
		

	if results:
		z=sorted(results, key=lambda linko:linko.numfound, reverse=True)
		print("\nFound")
		count=0
		for x in z:
			print x.title
			print x.linkname
			print x.numfound
			print "\n"
			count+=1
			if(count==10):
				break
	else:
		print("Nothing found.")
		

def main():
	conn=create_connection(database)
	print conn
	willsearch="yes"
	while willsearch == "yes":
		ser=raw_input("Enter search term: ")
		term=ser.split(" ")
		print term
		with conn:
			search(conn,term)

		willsearch=raw_input("Would you like to search again? ")


main()