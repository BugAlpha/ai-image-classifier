# ai-image-classifier
 
A simple web app that lets you upload an image and get back a classification from a MobileNetV2 model. Built with Flask and Keras.
 
## Project structure
 
```
ai-image-classifier/
├── main.py         # Flask routes
├── modellogic.py   # Model loading and prediction
├── model.h5        # Pre-trained MobileNetV2 weights
└── templates/
    └── index.html  # Upload form and results page
```
 
## Getting started
 
```bash
git clone https://github.com/BugAlpha/ai-image-classifier.git
cd ai-image-classifier
pip install flask tensorflow pillow
python main.py
```
 
Then open `http://127.0.0.1:5000` in your browser, upload an image, and the app will return a predicted label with a confidence score.
 
## How it works
 
Flask handles the upload and saves the image to a local `uploads/` folder. It then passes the file path to `modellogic.py`, which preprocesses the image and runs it through the saved MobileNetV2 model. The result a class label and confidence percentage gets rendered back on the page alongside the uploaded image.
 
## License
 
Public domain — do whatever you want with it. See [LICENSE](LICENSE) for details.
 
