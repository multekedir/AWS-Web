from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def getUsers():
    output = subprocess.getoutput("awk -F: '{ print $1}' /etc/passwd").split('\n')
    for i in output:
        print(i)
    return output

@app.route('/')
def home():
    users = getUsers()
    return render_template('index.html', userData=users)

    #return '''<p>The language value is: {}</p>'''.format( output)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
