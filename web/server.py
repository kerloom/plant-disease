from flask import Flask, render_template, request
from werkzeug import secure_filename
import lib.predict as predict

UPLOAD_FOLDER = 'img/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#@app.route('/upload')
#def upload_file():
#   return render_template('upload.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save(secure_filename(f.filename))
            answer = predict.run_inference_on_image(imagePath=secure_filename(f.filename))
            return 'Answer: ' + str(answer)
        except Exception, e:
            return 'Error: ' + str(e)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
