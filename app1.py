from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the directory where your images are stored
IMAGE_DIRECTORY = 'wall'

@app.route('/')
def index():
    # Get a list of all image filenames in the directory
    image_files = os.listdir(IMAGE_DIRECTORY)
    return render_template('samp.html', image_files=image_files)

@app.route('/images/<path:filename>')
def get_image(filename):
    # Serve images from the specified directory
    return send_from_directory(IMAGE_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(debug=True)
