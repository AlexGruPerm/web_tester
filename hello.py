import logging
from flask import Flask, url_for, render_template, request, make_response, redirect

#https://ru.wikibooks.org/wiki/Flask

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    #resp = make_response(render_template(...))
    #resp.set_cookie('username', 'XYZ')
    #return resp
    return "index page"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        s = '--post--'
    elif request.method == 'GET':
        s = "get var=" + request.args.get('var','000')
        if request.args.get('var','000') != "123":
             return redirect(url_for('second'))
    else:
        s = '--no--'
    #request.base_url
    username = request.cookies.get('username')
    return "var=" + s + "(" +request.base_url + ")["+ str(username) +"]"

@app.route('/hello/<name>')
def hello2(name=None):
    logging.debug("call hello2")
    return render_template('hello.html', name=name)

@app.route('/sec')
def second():
    return render_template('hello.html', name="abc")

if __name__ == "__main__":
    logging.debug("before run ....")
    app.debug = True
    #with app.test_request_context():
    #    print(url_for('index'))
    #    print(url_for('show_user_profile', username='John Doe'))
    app.run()



