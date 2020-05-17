## Recipe App
---
Milestone Project 3: Data Centric Development - Code Institute

This web application allow to view, add, update and delete recipes and recipes categories.

In this Project I use my new knowledges such as MongoDB, Flask, Python, Materializecss framework.

### Deployment
---
The App deployed on [HEROKU](https://pasta-dishes.herokuapp.com/).

This Project was created and developed in GitPod IDE. 

Stored in GitHub repository https://github.com/aleksandrsg/receipts and Heroku https://pasta-dishes.herokuapp.com/

1. To deploy Project have to make registration on www.heroku.com
2. Press button NEW on the top right corner
3. Choose function: Create New App
4. Type App name: pasta-dishes
5. Choose a region : Europe
6. Push button CREATE APP 
7. Go back to GitPod IDE and make connection with Heroku
8. Type in terminal: $ heroku login -i 
9. Type in terminal: $ heroku git:remote -a pasta-dishes
10. Type in terminal: $ git add .
11. Type in terminal: $ git commit -m "Any your comment"
12. Type in terminal: $ git push heroku master
13. Go back to Heroku, choose pasta-dishes on the left side 
14. Press button OPEN APP on the top right coner
15. App works.

### UX
---
Project wireframe you could find in directory Static / Wireframe. 

To create wireframes I used free online resource https://wireframe.cc/. 

* As an app user I could find my favorite Pasta recipe.

* As an app user I could add any Pasta recipe which I created on my own and share it with public.

* As an app user I able to update previously published recipe.

* As an app user I able to delete previously published recipe.

* As an app user I could find other products related to pasta recipes.

### Technologies used
---
To develop Project the author use the following basic web technologies:

* HTML,
* CSS,
* Materializecss framework,
* Flask framework,
* PyMongo,
* MongoDB,
* jQuery,
* Jinja.

### Testing
---
The project was created, developed and tested in GitPod IDE step by step manualy.

During the app developing and testing was the following main issues:

1. While testing Add Recipe functionality input data from Form did not flow correctly to MongoDB.
Recipe Document had only _id:ObjectId('') other data was missing (receipt_name, serves, prep, cook_time, ingredients,
description, img_link, category_name). 
The problem was solved by adding to each INPUT tag following attributes "ID" and "NAME".
<input id="receipt_name" name="receipt_name" type="text" class="validate" required>

2. While testing Edit Recipe functionality recipe category data did not flow to Form from MongoDB.
The category field was empty. The problem was found and solved by adding in file APP.PY,
the following code "categories=all_categories" :

@app.route('/edit_receipt/<receipt_id>')
def edit_receipt(receipt_id):
    the_receipt =  mongo.db.receipts.find_one({"_id": ObjectId(receipt_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editreceipt.html', receipt=the_receipt, categories=all_categories)

3. App did not opened in Heroku. The problem was solved by updating requirements.txt file.

### Database
---
Data stored in MongoDB Atlas cloud.

For the Project purposes was created DB: pasta_dishes.

DB consists from three collections inside it (categories, receipts, books).

Collection Categories has the following structure:

* _id:ObjectId("1234567890")
* category_name: "ABC".

Collection Books has the following structure:

* _id:ObjectId("1234567890")
* name: " "
* cover: " "
* language:" "
* author: " "
* publisher: " "
* pages: " "
* image: " "
* price: " "

Collection Receipts has the following structure:

* _id:ObjectId("1234567890")
* receipt_name: " "
* serves: " "
* prep:" "
* cook_time: " "
* ingredients: " "
* description: " "
* img_link: " "
* category_name: " "