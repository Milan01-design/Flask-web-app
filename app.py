from flask import Flask, render_template, request
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    skills = ["Python", "JavaScript", "C++", "HTML", "CSS"]
    projects= [
        {"title": "Quiz Master", "desc": "An interactive quiz app.", "tech": "Python, Flask"},
        {"title": "Portfolio Website", "desc": "My personal website.", "tech": "HTML, CSS, JS"},
        {"title": "Chatbot", "desc": "A basic AI assistant.", "tech": "Python"}
    ]
    return render_template('home.html', skills=skills, name="Milan", age=21, city="Chamba", 
                           languages=["Python", "JavaScript", "C++"], projects=projects)

@app.route('/index')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        # Create the uploads folder if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File {file.filename} uploaded successfully! <br> <a href='/'>Go back</a>"
    else:
        return render_template('upload.html')  # Show upload form on GET

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can process the data, e.g., save it to a file or database
    with open("flaskdata.txt", "a") as file:
        file.write(f"Name: {username}, Email: {email}, Message: {message}\n")
    # Here you can add code to send an email or save the data to a database
    return f"<h2>Thank you, {username}!</h2><p>Your message: {message}</p><p>We will contact you at {email}</p>"

@app.route('/about')
def about():
    return render_template('about.html', hobbies=["Coding", "Reading", "Traveling"],
                            ambition=["Become a Software Engineer", "Travel the World", "Learn New Languages"],
                              quote="Keep pushing your limits!")
if __name__ == '__main__':
    app.run(debug=True)