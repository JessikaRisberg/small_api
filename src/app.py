"""
Mini Flask API mini file
"""

from flask import Flask, Response
import json


def create_app():
    """
    Factory function for flask application
    :return: app object
    """
    app = Flask(__name__)

    @app.get('/api/v1.0/first')
    def first_get():
        data = {
            'name': 'Jane',
            'age': 34
        }

        return Response(json.dumps(data), 200, content_type='application/json')
    return app


if __name__ == '__main__':
    create_app().run()
