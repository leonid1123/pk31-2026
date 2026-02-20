from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        name = request.form.get('mlp_name')
        mlp_chk = request.form.getlist('chk')  # безопаснее
        print(mlp_chk, name)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


