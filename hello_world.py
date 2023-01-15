from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

### Modelo de documentação Swagger para seguir

@app.route("/")
def hello_world():
    """Example endpoint Hello World
        This is using docstrings for specifications.
        ---
        parameters:
          - name: palette
            in: path
            type: string
            enum: ['all', 'rgb', 'cmyk']
            required: true
            default: all
        definitions:
          Palette:
            type: object
            properties:
              palette_name:
                type: array
                items:
                  $ref: '#/definitions/Color'
          Color:
            type: string
        responses:
          200:
            description: A list of colors (may be filtered by palette)
            schema:
              $ref: '#/definitions/Palette'
            examples:
              rgb: ['red', 'green', 'blue']
        """
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }

    return "<p>Hello, World!</p>"