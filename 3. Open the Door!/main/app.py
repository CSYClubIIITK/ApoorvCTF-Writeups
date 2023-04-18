from flask import Flask, render_template, abort

app = Flask(__name__)

books_to_show = []
for i in range(12):
    book = {
        'id': i,
        'title': f'Book {i}',
        'author': f'Author {i}'
    }
    books_to_show.append(book)

books = []
for i in range(51):
    book = {
        'id': i,
        'title': f'Book {i}',
        'author': f'Author {i}'
    }
    books.append(book)

books[32]['author'] = "apoorvCTF{1dor5_ar3_ea5y_p3Asy}"

@app.route('/')
def index():
    return render_template('index.html', books=books_to_show)

@app.route('/books/<int:book_id>')
def book(book_id):
    if book_id >= 0 and book_id <= 50:
        book = books[book_id]
    else:
        abort(404)
    return render_template('book.html', book=book)

if __name__ == '__main__':
    app.run()
