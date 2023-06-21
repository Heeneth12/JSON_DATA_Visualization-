from flask import Flask, request, render_template
import json



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/search', methods=["POST"])
def search():
    if request.method == "POST":
        if 'myfile' in request.files: 
        # Check if the key 'myfile' exists in request.files

            uploaded_file = request.files['myfile'] 
            # Access the uploaded file
            if uploaded_file.filename.endswith('.json'):
                data_list = json.load(uploaded_file)  
                # Load the JSON data
                return render_template('filter.html', data=data_list)
            
    return "Error: Invalid file or request method"


if __name__ == '__main__':
    app.run()
