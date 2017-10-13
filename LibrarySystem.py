from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/update')
def update():
    return render_template('update_publication.html')


@app.route('/newpublication')
def create_book():
    return render_template('create_publication.html')


@app.route('/viewpublications')
def viewpublications():
    return render_template('view_all_publications.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')


if __name__ == '__main__':
    app.run()
