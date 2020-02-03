from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField,SelectField,BooleanField
from wtforms import RadioField
from wtforms import validators, ValidationError

class ContactForm(Form):


   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])



   Age = BooleanField('15-18')
   Age1 = BooleanField('19-22')
   Age2 = BooleanField('23-26')
   Age3 = BooleanField('27-30')
   Age4 = BooleanField('31-35')
   Age5 = BooleanField('36-40')
   Age6 = BooleanField('41')

   Music = BooleanField('Turkish Pop')
   Music1 = BooleanField('Rock')
   Music2 = BooleanField('Pop')
   Music3 = BooleanField('R&B')
   Music4 = BooleanField('Metal')
   Music5 = BooleanField('Deep House')
   Music6 = BooleanField('Rap')
   Music7 = BooleanField('Turkish Rap')
   Music8 = BooleanField('Latin')
   Music9 = BooleanField('Classical Music')
   Music10 = BooleanField('Electronical Music')
   Music11 = BooleanField('Indie ')

   Fav = BooleanField('Metallica-Master of Puppets')
   Fav1 = BooleanField('Queen-Bohemian Rhapsody')
   Fav2 = BooleanField('The Weeknd-Starboy')
   Fav3 = BooleanField('RTchaikovsky-Swan Lake')
   Fav4 = BooleanField('Ceza-Yerli Plaka')
   Fav5 = BooleanField('Eminem-Lose Yourself')

   Artist = BooleanField('Duman')
   Artist1 = BooleanField('Sagopa Kajmer')
   Artist2 = BooleanField('The Beatles')
   Artist3 = BooleanField('Metallica')
   Artist4 = BooleanField('Maroon5')
   Artist5 = BooleanField('Scorpions')
   Artist6 = BooleanField('Britney Spears')

   Movie = BooleanField('Action')
   Movie1 = BooleanField('Drama')
   Movie2 = BooleanField('Fantastic')
   Movie3 = BooleanField('Crime')
   Movie4 = BooleanField('Horror')
   Movie5 = BooleanField('Animation')
   Movie6 = BooleanField('Romantic')

   submit = SubmitField("Send")
