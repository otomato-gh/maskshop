from flask import Flask, request, render_template, redirect, url_for
import requests
from requests.adapters import HTTPAdapter
import json
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DecimalField, FileField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length
import os, time


app = Flask(__name__)
app.config.from_object('settings')
app.config.from_object('version')
app.config.from_object('init')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['INITDB'] = os.getenv('INITDB')


from flask_bootstrap import Bootstrap
Bootstrap(app)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    picture = FileField('picture')
    submit = SubmitField(label='Add')

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
    return headers

@app.route('/healthz')
def healthz():
    return 'Healthy'

@app.route('/version')
def version():
    return app.config['VERSION']


@app.route('/login', methods=['POST'])
def login():
    user = request.values.get('username')
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', user)
    return response


@app.route('/logout', methods=['GET'])
def logout():
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', '', expires=0)
    return response

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    print("i'm in submit")
    print("name"+request.values.get('name'))
    response = app.make_response(redirect(request.referrer))
    picture = request.files['picture']
    filename = secure_filename(picture.filename)
    picture.save(os.path.join(
        app.static_folder, 'img', filename
    ))
    r = requests.post("http://api/mask",
                    data = { "name": request.values.get('name'),
                            "type": request.values.get('type'),
                            "price": request.values.get('price'),
                            "picture": filename})
    print(r.text)
    return response

@app.route('/')
def home():
    headers = getForwardHeaders(request)
    user = request.cookies.get("user", "")
    form = MyForm()

    out = "Choose a mask:<br>"
    r = requests.get("http://api/mask", headers=headers)
    if r.status_code != 500:
        print(r.text)
        masks = json.loads(r.text)
        print(masks)
    return render_template(
        'front.html',
        masks=masks,
        user=user,
        form=form
    )


def run_app():
    if app.config['INITDB'] == 'true':
        print("Waiting for the api to become available")
        # dirty workaround to allow api to come up
        time.sleep(5)
        s = requests.Session()
        s.mount('http://api/mask', HTTPAdapter(max_retries=5))
        for mask in app.config['INIT_ITEMS']:
            print("Inserting "+json.dumps(mask))
            #now try to init
            r = requests.post("http://api/mask",
                            json = mask,
                            headers = {'content-type':'application/json'})
            print(r.text)
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)

if __name__ == '__main__':
    run_app()
