from cvtailor_app import firestore_upload, firebase_get, proper_data, get_form_data

import numpy as np
from random import seed
from random import randint

import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

if __name__ == '__main__':

    cred = credentials.Certificate("cv-tailor-2021-firebase-adminsdk-fksao-29fb361d14.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

print('hi, this is a revolutionary cv building idea which can disrupt existing apps if given sufficient time to develop')

if input('have you filled in the cv building form before?(y/n) ').lower() == 'y':
    email = input('enter your email: ')
    get_data = db.collection('persons').where('email','==',email.lower().split())

    if len(get_data.get()) == 0:
        form_data = {'email': email}
    else:
        print('the email you entered is not known')
