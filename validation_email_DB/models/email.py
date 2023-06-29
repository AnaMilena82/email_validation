
from config.mysqlconnection import connectToMySQL
from flask import flash
import re
from __init__ import BASE_DE_DATOS

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all_email(cls):
        query = "SELECT * FROM emails;"
        emails = []
        results = connectToMySQL(BASE_DE_DATOS).query_db(query)
        
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def new_email(cls, data ):
        query = "INSERT INTO emails ( email , created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        return connectToMySQL(BASE_DE_DATOS).query_db( query, data )        

    @staticmethod
    def validate_email(data):
        email = data["email"]
        existing_email = Email.get_email_by_address(data['email'])
        if existing_email:
            flash("El correo electrónico ya existe.", "error")
            return None
        
        is_valid = True # asumimos que esto es true

        if not EMAIL_REGEX.match(email):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def get_email_by_address(email):
        query = "SELECT * FROM emails WHERE email = %(email)s"
        result = connectToMySQL(BASE_DE_DATOS).query_db(query, {"email": email})
        if result:
            return result[0]  # Retorna el primer resultado encontrado
        else:
            return None

    @classmethod
    def delete_email(cls, data ):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(BASE_DE_DATOS).query_db( query, data )