from flask import Flask, request

app = Flask(__name__)
app.config.from_object(__name__)

posts = []

@app.route("/")
def index():
    return f'Numero de Posts {len(posts)}'

@app.route("/p/<string:slug>/")
def show_post(slug):
    return 'Mostrando el post {}'.format(slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id):
    return "post_form {}".format(post_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
