from flask import Flask
from flask import request
from flask import render_template
from .MDB import MgDB
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('page1_indexOfBooks.html')
@app.route('/',methods=['POST'])

def next():
    if request.method=='POST':
        bookname = request.form['BookName']
        bookid = request.form['BookID']
        location = request.form['Location']
        MgDB.insertNewBook(self, bookName, bookid, location)
    return render_template('page1_indexOfBooks.html')
	
	
	
