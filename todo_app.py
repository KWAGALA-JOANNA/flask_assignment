# import statements
from flask import Flask, render_template, request, redirect, urlfor

# creating an instance
app = Flask(__name__, template_folder='templates')
tasks =[]
@app.route("/")
def index():
    return render_template('index.html')

# creating a new task with a form taking a task name
@app.route('/add_task', methods=['POST'])
def create_task():
    # creating a variable to store our task using request.form.get(name of the task)
    task = request.form.get('task')
    # appending to a list tasks
    tasks.append(task)
    # redirecting to a particular page by passing in the redirect () and urlfor() which are functions
    return redirect(urlfor('index'))

    
# activating debug mode 
if __name__ == '__main__':
    app.run(debug=True)
    