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
    
    
    soft_glam = {
    	"eye_shape": ["Almond", "Upturned"],
    	"lip_volume": ["Full", "Medium"],
    	"eyebrow_shape": ["Arch", "High-arch"],
    	"nose_type": ["Snub", "Button"],
    	"face_shape": ["Heart", "Oval"],
    }

    name = {
    	"eye_shape": ["Almond", "Upturned"],
    	"lip_volume": ["Full", "Medium"],
    	"eyebrow_shape": ["Arch", "High-arch"],
    	"nose_type": ["Snub", "Button"],
    	"face_shape": ["Heart", "Oval"],
    }
    
    name = {
    	"eye_shape": ["Almond", "Upturned"],
    	"lip_volume": ["Full", "Medium"],
    	"eyebrow_shape": ["Arch", "High-arch"],
    	"nose_type": ["Snub", "Button"],
    	"face_shape": ["Heart", "Oval"],
    }
    
    name = {
    	"eye_shape": ["Almond", "Upturned"],
    	"lip_volume": ["Full", "Medium"],
    	"eyebrow_shape": ["Arch", "High-arch"],
    	"nose_type": ["Snub", "Button"],
    	"face_shape": ["Heart", "Oval"],
    }
    
    scores = {
    	"Soft Glam": 0;
    	"name": 0;
    	"name": 0;
    	"name": 0;
    	"name": 0;
    }    
    
    
    if eye_shape in soft_glam["eye_shape"]:
    	scores["Soft Glam"] +=1
    if lip_volume in name["lip_volume"]:
    	scores["name"] +=1
    if eyebrow_shape in name["eyebrow_shape"]:
    	scores["name"] +=1
    if nose_type in name["nose_type"]:
    	scores["name"] +=1
    if face_shape in name["face_shape"]:
    	scores["name"] +=1
    	
    	
    if eye_shape in name["eye_shape"]:
    	scores["name"] +=1
    if lip_volume in name["lip_volume"]:
    	scores["name"] +=1
    if eyebrow_shape in name["eyebrow_shape"]:
    	scores["name"] +=1
    if nose_type in name["nose_type"]:
    	scores["name"] +=1
    if face_shape in name["face_shape"]:
    	scores["name"] +=1
    
    
    if eye_shape in name["eye_shape"]:
    	scores["name"] +=1
    if lip_volume in name["lip_volume"]:
    	scores["name"] +=1
    if eyebrow_shape in name["eyebrow_shape"]:
    	scores["name"] +=1
    if nose_type in name["nose_type"]:
    	scores["name"] +=1
    if face_shape in name["face_shape"]:
    	scores["name"] +=1
    
    
    if eye_shape in name["eye_shape"]:
    	scores["name"] +=1
    if lip_volume in name["lip_volume"]:
    	scores["name"] +=1
    if eyebrow_shape in name["eyebrow_shape"]:
    	scores["name"] +=1
    if nose_type in name["nose_type"]:
    	scores["name"] +=1
    if face_shape in name["face_shape"]:
    	scores["name"] +=1
    
    
    if eye_shape in name["eye_shape"]:
    	scores["name"] +=1
    if lip_volume in name["lip_volume"]:
    	scores["name"] +=1
    if eyebrow_shape in name["eyebrow_shape"]:
    	scores["name"] +=1
    if nose_type in name["nose_type"]:
    	scores["name"] +=1
    if face_shape in name["face_shape"]:
    	scores["name"] +=1
    
    
    result = max(scores, key=scores.get)
    
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