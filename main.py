from flask import Flask, render_template, request, send_from_directory
from modellogic import predict_image
import os

main = Flask(__name__)

UPLOAD_FOLDER = "uploads"
main.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# hadi katsyb folder incase mabghach ytlia (mabghach nit)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#loader dyl frontend
@main.route('/')
def home():
    return render_template('index.html')

# Serve uploaded images so browser can display them
@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(main.config['UPLOAD_FOLDER'], filename)

#hada handler dyl submission dyal img mn lform
@main.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"] #kyjib img mn formulaire

    if file.filename == "":
        return "khtar image!"

    # Save 
    filename = file.filename
    filepath = os.path.join(main.config["UPLOAD_FOLDER"], filename)
    file.save(filepath) #this guy saves the uploaded img fserver

    result, confidence = predict_image(filepath) #finally hadi liaison m3a model (kysift img lmodel ytretiha wkyjib result)

    #creation dyal url li y9dr ysta3mlo navigateur
    image_url = f'/uploads/{filename}'

    return render_template(
        "Index.html",
        prediction=f"{result} ({confidence:.2f}%)",
        image=image_url
    )


if __name__ == "__main__":
    main.run(debug=True)
        