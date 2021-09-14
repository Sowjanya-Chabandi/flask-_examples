from flask import Flask,render_template_string,render_template
from flask_caching import Cache

config = {
    "DEBUG": True,          
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)



@app.route("/")
@app.route("/html/<foo>")
def html(foo=None):
    if foo is not None:
        cache.set("foo", foo)
    bar = cache.get("foo")
    return render_template_string(
        "<html><body>foo cache: {{bar}}</body></html>", bar=bar
    )




if __name__=='__main__':
    app.run(debug=True)
