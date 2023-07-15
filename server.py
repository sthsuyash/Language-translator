from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder="templates",
            static_folder="static")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)
    # return "Translated text to French"


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)
    # return "Translated text to English"


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8080)
