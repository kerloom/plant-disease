from flask import Flask, render_template, request
from werkzeug import secure_filename
import lib.predict as predict
import subprocess

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
            #answer = predict.run_inference_on_image(imagePath=secure_filename(f.filename))
            answer = subprocess.check_output(['python', 'lib/predict.py', secure_filename(f.filename)])
            tmp = answer.split('|')
            resultados = []
            for it in tmp:
                splat = it.split('=')
                if len(splat) == 2:
                    nombre = splat[0].title()
                    prob = '{:.2%}'.format(float(splat[1]))
                    resultados.append([nombre, prob])
            return render_template('results.html', resultados=resultados)
        except Exception, e:
            print e
            return 'Error: ' + str(e)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
