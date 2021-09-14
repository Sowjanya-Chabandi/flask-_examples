from flask import Flask,request,make_response
app=Flask(__name__)

@app.route('/cookies/<val>')
def set(val):
    s=make_response('Cookies')
    s.set_cookie('my_cookie',val)
    return s

@app.route('/cookies')
def get():
    return str(request.cookies.get('my_cookie'))

if __name__=='__main__':
    app.run(debug=True)
