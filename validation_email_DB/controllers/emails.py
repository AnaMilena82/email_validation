from flask import Flask, render_template, request, redirect, session, url_for, flash
from __init__ import app
from models.email import Email


@app.route('/', methods = ['GET'])    
def get_email():
    return render_template("index.html")


@app.route('/', methods = ['POST'])    
def post_email():
    data = {
        "email": request.form["email"],
        
    }
    if not Email.validate_email(data):
        # redirigir a la ruta donde se renderiza el formulario de dojo
        return redirect('/')
    email = Email.new_email(data)
    flash("Email ingresado satisfactoriamente", "success")
    
    return redirect(url_for('success'))
    

@app.route('/success')
def success():
    #Obtener los datos almacenados en la variable de sesión
    emails = Email.get_all_email()
         
    return render_template('success.html', emails=emails)


@app.route("/success/delete/<int:id>", methods=[ 'POST'])
def delete_user_by_id(id):
    data = {
        "id" : id
    }
    # llamar al método de clase get all para obtener todos los amigos
    Email.delete_email(data)
    return redirect('/success')
