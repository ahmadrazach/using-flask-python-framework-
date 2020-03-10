
from flask import Flask, render_template,request

app = Flask(__name__)

#notepad
notes=[]
@app.route("/note",methods=["POST","GET"])
def note():
    if request.method=="POST":
        note=request.form.get("note")
        if request.form.get("note")=="clear":
            notes.clear()
        else:
            notes.append(note)
    
    return render_template("note.html",notes=notes)
app.run()