from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# Sample data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Book resource
class BookList(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'List of books',
                'examples': {
                    'application/json': books
                }
            }
        }
    })
    def get(self):
        """Get all books
        ---
        responses:
          200:
            description: A list of books
        """
        return jsonify(books)

    @swag_from({
        'responses': {
            201: {
                'description': 'Book added successfully'
            },
            400: {
                'description': 'Missing fields'
            }
        },
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'author': {'type': 'string'}
                    },
                    'required': ['title', 'author']
                }
            }
        ]
    })
    def post(self):
        """Add a new book
        ---
        parameters:
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
              required:
                - title
                - author
        responses:
          201:
            description: Book added successfully
          400:
            description: Missing fields
        """
        data = request.json
        if not all(key in data for key in ('title', 'author')):
            return {'message': 'Missing fields'}, 400
        book = {
            'id': len(books) + 1,
            'title': data['title'],
            'author': data['author']
        }
        books.append(book)
        return {'message': 'Book added successfully', 'book': book}, 201

class Book(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'Book found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'author': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Book not found'
            }
        },
        'parameters': [
            {
                'name': 'book_id',
                'in': 'path',
                'required': True,
                'type': 'integer'
            }
        ]
    })
    def get(self, book_id):
        """Get a book by ID
        ---
        parameters:
          - name: book_id
            in: path
            required: True
            type: integer
        responses:
          200:
            description: Book found
          404:
            description: Book not found
        """
        book = next((book for book in books if book['id'] == book_id), None)
        if book:
            return jsonify(book)
        return {'message': 'Book not found'}, 404

    @swag_from({
        'responses': {
            204: {
                'description': 'Book deleted successfully'
            },
            404: {
                'description': 'Book not found'
            }
        },
        'parameters': [
            {
                'name': 'book_id',
                'in': 'path',
                'required': True,
                'type': 'integer'
            }
        ]
    })
    def delete(self, book_id):
        """Delete a book by ID
        ---
        parameters:
          - name: book_id
            in: path
            required: True
            type: integer
        responses:
          204:
            description: Book deleted successfully
          404:
            description: Book not found
        """
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            return {'message': 'Book not found'}, 404
        books = [book for book in books if book['id'] != book_id]
        return '', 204

    @swag_from({
        'responses': {
            200: {
                'description': 'Book updated successfully'
            },
            404: {
                'description': 'Book not found'
            }
        },
        'parameters': [
            {
                'name': 'book_id',
                'in': 'path',
                'required': True,
                'type': 'integer'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'author': {'type': 'string'}
                    },
                    'required': ['title', 'author']
                }
            }
        ]
    })
    def put(self, book_id):
        """Update a book by ID
        ---
        parameters:
          - name: book_id
            in: path
            required: True
            type: integer
          - name: body
            in: body
            required: True
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
              required:
                - title
                - author
        responses:
          200:
            description: Book updated successfully
          404:
            description: Book not found
        """
        data = request.json
        book = next((book for book in books if book['id'] == book_id), None)
        if book:
            book.update(data)
            return {'message': 'Book updated successfully', 'book': book}, 200
        return {'message': 'Book not found'}, 404

# Add resource routes
api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
