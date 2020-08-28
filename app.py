from flask import Flask, render_template, url_for, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit_form', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_data_csv(data)
            message_ = "Form submitted!!  I'll contact you soon!"
            return render_template('Thankyou.html', message_=message_)
        except:
            message_ = 'NO FORM SAVED'
            return render_template('Thankyou.html', message_=message_)
    else:
        message_ = "Try Again!"
        return render_template('Thankyou.html', message_=message_)


def write_data_csv(data):
    name = data['name']
    email = data['email']
    subject = data['subject']
    messsage = data['message']
    #with open('database.txt', 'a') as f:
     #   f.write("name: {}, email: {}, subject: {}, message: {}".format(name, email, subject, messsage))
    with open('db.csv', 'w', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([name, email, subject, messsage]) 