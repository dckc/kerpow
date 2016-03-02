from flask import Flask
app = Flask(__name__)



from heroes import hero_info


@app.route("/")
def hello():
    heroes = hero_info()
    items = [
        '<li><a href="{pg}"><img src="{img}" /></a></li>'.format(pg=pg, img=img)
        for (pg, img) in heroes]
    return '<ul>' + '\n'.join(items) + '</ul>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
