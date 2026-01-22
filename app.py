from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')
@app.route('/read-form', methods=['POST'])
def read_form():
   data = request.form
   return {
       'name': data['username'],
       'email': data['useremail'],
       'password': data['userPassword'],
       'Contact': data['userContact']
   }
if __name__ == '__main__':
   app.run(debug=True)