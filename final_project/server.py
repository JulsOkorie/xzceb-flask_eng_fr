import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    # Write your code here
    _frenchtext = request.args.get(' _englishtext')
    print(_frenchtext)
    return ("Translated text to French:{}".format(_frenchtext))

@app.route("/french_to_english")
def french_to_english():
    # Write your code here
    _englishtext = request.args.get(' _frenchtext')
    print(_englishtext)
    return ("Translated text to English:{}".format( _englishtext))

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
