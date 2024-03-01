import spacy
from flask import Flask, render_template, request
from spacy import displacy

app = Flask(__name__)

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def show_ents(doc):
    for ent in doc.ents:
        print(f"{ent.text} - Start: {ent.start_char}, End: {ent.end_char}, Label: {ent.label_}, Entity Type: {spacy.explain(ent.label_)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def ner():
    text = request.form['text']
    doc = nlp(text)
    show_ents(doc)

    # Generate named entity visualizations using displacy
    displacy_render = displacy.render(doc, style='ent', page=True)

    return render_template('index.html', result=displacy_render)

if __name__ == '__main__':
    app.run(debug=True)
