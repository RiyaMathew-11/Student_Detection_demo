from flask import Flask, render_template, request, send_from_directory, session
import os
from werkzeug.utils import secure_filename
app = Flask(__name__, static_url_path="/static",template_folder='templates',
            static_folder='static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'bbeb363596b1d2b0f049'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_image():

    uploaded_img = request.files['uploaded-file']
    # Extracting uploaded data file name
    img_filename = secure_filename(uploaded_img.filename)
    # Upload file to database (defined uploaded folder in static path)
    uploaded_img.save('static/uploads/' + img_filename)
    # Storing uploaded file path in flask session
    session['uploaded_img_file_path'] = os.path.join(
        app.config['UPLOAD_FOLDER'], img_filename)
    
    print(session['uploaded_img_file_path'])

    return render_template('display_image.html')

    # imagefile = request.files['imagefile']
    # image_path = "./static/uploads/" + imagefile.filename
    # imagefile.save(image_path)
    # return render_template('display_image.html', image_path=image_path, imagefile=imagefile)


@app.route('/show_image')
def display_image():
    image_path = session.get('uploaded_img_file_path', None)
    return render_template('show_image.html', user_image=image_path)


if __name__ == '__main__':
    app.run(port=5500, debug=True)
