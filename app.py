from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    leave_type = None
    job_type = None
    if request.method == 'POST':
        job_type = request.form.get('job_type')

        if job_type in ['large_company', 'public_servant']:
            leave_type = '年休'
        else:
            leave_type = '有給'

    return render_template('form.html', leave_type=leave_type, job_type=job_type)

if __name__ == '__main__':
    app.run(debug=True)