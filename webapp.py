from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/page1", methods=["POST"])
def render_page1():
    eye_shape = request.form.get("eye_shape")
    lip_volume = request.form.get("lip_volume")
    eyebrow_shape = request.form.get("eyebrow_shape")
    nose_type = request.form.get("nose_type")
    face_shape = request.form.get("face_shape")
    
    
    if eye_shape == '':
        reply1 = ""
    elif face_shape == "":
        reply1 = ""
    elif lip_volume == "":
        reply1 = ""
    elif eyebrow_shape == "":
        reply1 = ""
    elif nose_type == "":
        reply1 = ""

    return render_template(
	'page1.html',
	response1 = f"Eye shape: {eye_shape}",
	response2 = f"Lip volume: {lip_volume}",
	response3 = f"Eyebrow shape: {eyebrow_shape}",
	response4 = f"Nose type: {nose_type}",
	response5 = f"Face shape: {face_shape}",
	response6 = f"The best makeup style that'll suit you is: {result}."
)
    
if __name__=="__main__":
    app.run(debug=True)