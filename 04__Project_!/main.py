from bardapi import Bard
import os

token = 'eQjsdwMgYEwJdfRhHrkXudjgSiWi1Uso1197ajiH7YpHfQ11lU68lXY-jRVnSgRXxG_6kw.'
os.environ["_BARD_API_KEY"]=token

message = input("Enter your Prompt : ")
print(Bard().get_answer(str(message)))