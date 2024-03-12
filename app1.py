from flask import Flask,render_template,request,redirect,url_for,send_from_directory
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
import random 
import os
from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='ntharun832jacky@gmail.com'
app.config['MAIL_PASSWORD']='dogo ruiu ogty lrtp'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)


app.secret_key = "tharun_secret" 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class userdetails(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    otp=db.Column(db.Integer, nullable=False)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method =='POST':
        email=request.form['Email']
        psw=request.form['Password']
        existingdata=userdetails.query.filter_by(name=email).first()
        print("\n\n\n\n\n\n\n\n",existingdata)
        if existingdata:
                
            if (check_password_hash(existingdata.password, psw) and existingdata.verified == True):
                return redirect(url_for('home'))
            else:
                return "wrong password"
        else:
                return redirect(url_for('signin'))
        
    return render_template('login.html')




@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['Email']
        psw = request.form['Password']
        password=generate_password_hash(psw)
        phone = request.form['Phone']
        existingdata = userdetails.query.filter_by(name=email).first()

        if not existingdata:
            otp = generate_verification_code()
            new_data = userdetails(name=email, password=password, phone=phone, otp=otp)
            db.session.add(new_data)
            db.session.commit()

            subject = "Welcome to Our Tharun's Platform"
            body = f"""
            <html>
              <body>
                <h1 style="color: #007bff;">Welcome to Tharun validation website!</h1>
                <p style="font-size: 18px;">Your verification code is: <strong>{otp}</strong></p>
                <p style="font-size: 16px; color: #6c757d;">Thank you for signing up!</p>
              </body>
            </html>
            """
            sender = "ntharun832jacky@gmail.com"

            msg = Message(subject, sender=sender, recipients=[email])
            msg.html = body
            mail.send(msg)

            return render_template('validate.html', email=email)

    return render_template('signin.html')


# @app.route("/validate", methods=["GET","POST"])
# def validate():
#     if request.method == 'POST':
#         otp=request.form['otp']
#         email=request.args.get('email')
         
#         print("\n\n\n\n\n\nemail",email)
#         print("\n\n\n\n\n\notp",otp)
#         e_mail=str(email)
#         print("\n\n\n\nemail", e_mail)

#         user=userdetails.query.filter_by(name=e_mail).first()
#         if user:
#             oooot=int(otp)
#             database_otp=int(user.otp)
#         else:
#             print("\n\n\n\n\n\n\n\nuser dose not exsit in database")

        
#         print("\n\n\n\nOTP",otp,email)
#         if(database_otp == oooot):
#             user.verified=True
#             db.session.commit()
#             return redirect(url_for('home'))
#         else:
#             return "wrong otp"
        
#     return render_template('login.html')


@app.route("/validate", methods=["GET", "POST"])
def validate():
    if request.method == 'POST':
        otp = request.form['otp']
        email = request.args.get('email')
         
        print("\nEmail:", email)
        print("OTP:", otp)

        e_mail = str(email)
        print("Formatted Email:", e_mail)

        user = userdetails.query.filter_by(name=e_mail).first()
        if user:
            database_otp = int(user.otp)
            entered_otp = int(otp)
            if database_otp == entered_otp:
                user.verified = True
                db.session.commit()
                return redirect(url_for('home'))
            else:
                return "Wrong OTP"
        else:
            print("User does not exist in the database")
            return "Invalid email address or user does not exist"

    return render_template('login.html')


IMAGE_DIRECTORY = 'wall'

@app.route("/home")
def home():
    image_files = os.listdir(IMAGE_DIRECTORY)
    return render_template('home.html', image_files=image_files)

@app.route('/images/<path:filename>')
def get_image(filename):
    # Serve images from the specified directory
    return send_from_directory(IMAGE_DIRECTORY, filename)


# @app.route("/randomint")
def generate_verification_code():
    return ''.join(str(random.randint(1, 9)) for _ in range(6))

@app.route("/delete_database")
def delete_database():
    db.session.query(userdetails).delete()
    db.session.commit()
    return render_template('login.html')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
        # app.run(debug=True)
        app.run(host='0.0.0.0',debug=True)