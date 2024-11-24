from flask import jsonify, request
from app import db, app
from .models import Book

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(message='Pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_book = Book(
            title=post_data.get('title'),
            author=post_data.get('author'),
            read=post_data.get('read', False)
        )
        db.session.add(new_book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        books = Book.query.all()
        response_object['books'] = [book.to_dict() for book in books]
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    book = Book.query.filter_by(id=book_id).first()
    if request.method == 'PUT':
        if book:
            post_data = request.get_json()
            book.title = post_data.get('title')
            book.author = post_data.get('author')
            book.read = post_data.get('read')
            db.session.commit()
            response_object['message'] = 'Book updated!'
        else:
            response_object['status'] = 'fail'
            response_object['message'] = 'Book not found!'
    if request.method == 'DELETE':
        if book:
            db.session.delete(book)
            db.session.commit()
            response_object['message'] = 'Book removed!'
        else:
            response_object['status'] = 'fail'
            response_object['message'] = 'Book not found!'
    return jsonify(response_object)