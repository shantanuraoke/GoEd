from flask import Flask
from flask import request
from flask import render_template
import MongoDBFile
app=Flask(__name__)


@app.route('/')
def next():
    return render_template('page1_indexOfBooks.html')
@app.route('/py', methods=['GET', 'POST'])
def server():
    if request.method == 'POST':
        # Then get the data from the form
        tag = request.form['tag']

        # Get the username/password associated with this tag
        bookname, author,location = tag_lookup(tag)
        nsertNewBook(bookname, author, location)
        # Generate just a boring response
        return 'The credentials for %s are %s and %s' % (tag, bookname,author ,location) 
        # Or you could have a custom template for displaying the info
        # return render_template('asset_information.html',
        #                        username=user, 
        #                        password=password)

    # Otherwise this was a normal GET request
    else:   
        return render_template('page1_indexOfBooks.html')
	


	