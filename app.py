import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pasta_dishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tuser@myfirstcluster-1aric.mongodb.net/pasta_dishes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

# ---This route return all recipes from database on Main page---
@app.route('/get_receipts')
def get_receipts():
    return render_template("receipts.html", receipts=mongo.db.receipts.find())

# ---This route redirect the user to Add receipt Page---
@app.route('/add_receipt')
def add_receipt():
    return render_template("addreceipt.html", 
                            receipts=mongo.db.receipts.find(),
                            categories=mongo.db.categories.find())

# ---This route allows the user to send data from form to MongoDb and redirect the user to Main Page---
@app.route('/insert_receipt', methods=['POST'])
def insert_receipt():
    receipts = mongo.db.receipts
    receipts.insert_one(request.form.to_dict())
    return redirect (url_for('get_receipts'))

# ---This route allows to edit selected recipe ---
@app.route('/edit_receipt/<receipt_id>')
def edit_receipt(receipt_id):
    the_receipt =  mongo.db.receipts.find_one({"_id": ObjectId(receipt_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editreceipt.html', receipt=the_receipt, categories=all_categories)

# ---This route allows to send edited recipe to MongoDB with updated information and after redirect user to main Page---
@app.route('/update_receipt/<receipt_id>', methods=["POST"])
def update_receipt(receipt_id):
    receipts = mongo.db.receipts
    the_receipt=mongo.db.receipts.find_one({"_id": ObjectId(receipt_id)})
    receipts.update({'_id': ObjectId(receipt_id)},
    {
        'receipt_name':request.form.get('receipt_name'),
        'serves':request.form.get('serves'),
        'prep': request.form.get('prep'),
        'cook_time': request.form.get('cook_time'),
        'ingredients':request.form.get('ingredients'),
        'description':request.form.get('description'),
        'img_link':request.form.get('img_link'),
        'category_name': request.form.get('category_name'),
    })
    return redirect(url_for('get_receipts'))


# ---This route provide full information about selected recipe
@app.route("/receipt/<receipt_id>")
def receipt_description(receipt_id):
    one_receipt = mongo.db.receipts.find_one({"_id": ObjectId(receipt_id)})
    return render_template("description.html", receipt=one_receipt)

# ---This route allows to delete selected recipe permanently
@app.route("/delete_receipt/<receipt_id>")
def delete_receipt(receipt_id):
    receipt= mongo.db.receipts
    receipt.delete_one({"_id": ObjectId(receipt_id)})
    return redirect(url_for("get_receipts"))


#----- Section for Receipts Categories -----


# ---This route return all recipe categories
@app.route("/get_categories")
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())

# ---This route send new category to MongoDb and after redirect user to page with all categories ---
@app.route("/insert_category", methods=["POST"])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for("get_categories"))

# ---This route allow to delete selected category and after redirect user to page with all categories ---
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    category= mongo.db.categories
    category.delete_one({"_id": ObjectId(category_id)})
    return redirect(url_for("get_categories"))

# ---This route allow to add new category ---
@app.route("/add_category")
def add_category():
    return render_template("addcategory.html")

#----- Buy Receipt Books about Pasta -----

@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
