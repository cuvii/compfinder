#Crawler python file for Compfinder project for Information Retrieval, Fall 2017. 
#Utilizes BeautifulSoup for assistance with crawling format.
#Web crawler that traverses arxiv's tech section of the site for research articles.


import urllib2
from operator import itemgetter
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error

link='https://arxiv.org/corr/home'
page=urllib2.urlopen(link)

willsearch="yes"

database="C:\\sqlite\compfinder.db"

def create_connection(database):
	try:
		conn=sqlite3.connect(database)
		return conn
	except Error as e:
		print(e)
	return None

def create_article(conn, article):
	sql='''INSERT INTO Articles(Title, Abstract, Link)
			VALUES(?,?,?)'''
	cur=conn.cursor()
	cur.execute(sql,article)
	return cur.lastrowid

def crawl(conn):
	soup= BeautifulSoup(page, 'html.parser')

	for link in soup.find_all('a'):
		link_text=link.text
		if(link_text.find("cs.")!=-1):
			print(link.get('href'))
			primarypage= urllib2.urlopen(link.get('href'))
			primarysoup= BeautifulSoup(primarypage, 'html.parser')
			
			for primarylink in primarysoup.find_all('a', title="Abstract"):
				print primarylink.get('href')
				lk=str((primarylink.get('href')))
				secondarypage=urllib2.urlopen('https://arxiv.org'+primarylink.get('href'))
				secondarysoup=BeautifulSoup(secondarypage, 'html.parser')
				text=str(secondarysoup.find('blockquote'))
				title=str(secondarysoup.find_all("h1", {"class":"title mathjax"}))
				title=title[67:-6]
				a=("https://arxiv.org"+primarylink.get('href'))

				x=(title, text, a)
				print x
				create_article(conn, x)
				print("added")
		


def main():
	conn=create_connection(database)
	print conn

	with conn:
		crawl(conn)




main()
