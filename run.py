# import os
# #import the Flask class
# #import render_template() function from Flask
# from flask import Flask, render_template


# # the convention is that our variable is called app:  app = Flask(__name__)
# # __name__ is build-in function
# app = Flask(__name__)




# # we use the route decorator to tell Flask what URL should trigger the function that follows
# # @ is app route decorator. It's a way wrapppping function
# # '/' - root directory -> Flask trigger ijndexfunction and return "Herllo World!"
# @app.route('/')
# #
# def index():
#     return render_template("index.html")
    


    
    
# @app.route('/about')
# def about():
#     return render_template("about.html")
    
 
 
    
# @app.route('/contacts')
# def contacts():
#     return render_template("contacts.html")    




# @app.route('/careers')
# def careers():
#     return render_template("careers.html")





# # we're going to reference this built-in variable and say that if __name__ == "__main__":
# # __main__    is the name of the default module in Python
# if __name__ == '__main__':

# # we're going to run our app with the following arguments:
# # the host is going to be set to os.environ.get("IP"). This is an
# #internal environment variable that Cloud9 has set, and we're using the os
# #module from the standard library to get that environment variable for us.
#     app.run(host=os.environ.get('IP'),

# #It's the same with PORT, but this time we're casting it as an int, because it needs to be an integer
#             port=int(os.environ.get('PORT')),
            
# # debug=true because that will allow us to debug our code easier
#             debug=True)


# import os

# import json

# from flask import Flask, render_template



# app = Flask(__name__)


# @app.route('/')
# def index():
#     # we added second argument to render_template (): page_title
#     return render_template("index.html", page_title="Home" )





# @app.route('/about')
# def about():
# # we created empty array
#   data = []
# # Then, using a with block (i/o reading from files)
#   with open("data/company.json", "r") as json_data:
# #set to my data variable to the JSON parsed data that we've sent through.
#         data = json.load(json_data)


# # we added second argument to render_template (): page_title
# #we added third argument to render_template (): list_of_numbers. It will be ordered list or numbers og paragraphs
# #
#   return render_template("about.html", page_title="About",  company_data=data)





# @app.route('/contact')
# def contact():
# # we added second argument to render_template (): page_title
#     return render_template("contact.html", page_title="Contact")





# @app.route('/careers')
# def careers():
# # we added second argument to render_template (): page_title
#     return render_template("careers.html", page_title="Careers")





# if __name__ == '__main__':

#     app.run(host=os.environ.get('IP'),

#             port=int(os.environ.get('PORT')),

#             debug=True)

import os

import json

from flask import Flask, render_template, request, flash



app = Flask(__name__)
# create secret key for our non-permanent message to the user (feadback on his filled and sended form)
app.secret_key = "some_secret"





@app.route('/')

def index():

    return render_template("index.html")





@app.route('/about')

def about():

    data = []

    with open("data/company.json", "r") as json_data:

        data = json.load(json_data)

    return render_template("about.html", page_title="About", company_data=data)



# So I'm going to create a new route decorator: @app.route.("/about/<member_name>")
# And then I'm going to create a new view, which is going to be: about_member
# And that's going to take member_name as an argument.
# So whenever we look at our about URL with something after it, that's going to be passed in to this view.
# So we'll create an empty object, which we're going to use to store our data in later.
# Just as we did in our about view, we're going to open our company.json file for reading and refer to that as json_data.
# We'll then create another variable inside where we pass the data that we've passed through and converted into JSON.
# So data = json.load(json_data)
# And now what we're going to do is iterate through that data array that we've created.
# And we're going to say if obj["url"] == member_name, so that's the variable that we've passed in, then member = object.
# So we can see that those two link, our URL and our member_name have to match.
# And if they do, then we're going to return out this member object so that we can do something with it.
# And just to demonstrate that, we're going to just return some HTML, the same as we did in one of our earlier videos.
# I'm going to return "<h1>" + member["name"] + "</ h1>"


@app.route('/about/<member_name>')
def about_member(member_name):

    member = {}

    

    with open("data/company.json", "r") as json_data:

        data = json.load(json_data)

        for obj in data:

            if obj["url"] == member_name:

                member = obj

    
# this return was before we added member.html( template for each characters)
# return "<h1>" + member["name"]  +"</h1>"
    return render_template("member.html", member=member)
    
    

# we are going to say that the methods that are allowed are GET and POST.
@app.route('/contact', methods=['GET', 'POST'])

def contact():
    if request.method=="POST":
 #if we print here text, then fill form and send it . In terminnal window we see our message and code 200. Code 200 - everything is ok       
 # print ("Hello there!!!")
 
 
 # now we changed print() and typed there print (request.form).
 # in terminal window we can see all our data from message: phone, email, message and cde - 200
 #        print (request.form)
 # now instead print ()we call the Flash() function.
        flash("Thanks {}, we have received your message".format(
            request.form["name"]))

    return render_template("contact.html", page_title="Contact")





@app.route('/careers')

def careers():

    return render_template("careers.html", page_title="Careers")



if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),

            port=int(os.environ.get('PORT')),

            debug=True)