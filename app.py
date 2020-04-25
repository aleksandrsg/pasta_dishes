import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pasta_dishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tuser@myfirstcluster-1aric.mongodb.net/pasta_dishes?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')


@app.route('/get_receipts')
def get_receipts():
    return render_template("receipts.html", receipts=mongo.db.receipts.find())


@app.route('/add_receipt')
def add_receipt():
    return render_template("addreceipt.html", receipts=mongo.db.receipts.find())


@app.route('/insert_receipt', methods=['POST'])
def insert_receipt():
    receipts = mongo.db.receipts
    receipts.insert_one(request.form.to_dict())
    return redirect (url_for('get_receipts'))

@app.route('/edit_receipt/<receipt_id>')
def edit_receipt(receipt_id):
    the_receipt =  mongo.db.receipts.find_one({"_id": ObjectId(receipt_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editreceipt.html', receipt=the_receipt)

@app.route('/update_receipt/<receipt_id>', methods=["POST"])
def update_receipt(receipt_id):
    receipts = mongo.db.receipts
    receipts.update( {'_id': ObjectId(receipt_id)},
    {
        'receipt_name':request.form.get('receipt_name'),
        'serves':request.form.get('serves'),
        'prep': request.form.get('prep'),
        'cook_time': request.form.get('cook_time'),
        'ingredients':request.form.get('ingredients')
    })
    return redirect(url_for('get_tasks'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
