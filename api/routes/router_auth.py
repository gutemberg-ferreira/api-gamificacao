from app import app
from api.services import helpers
from flasgger import swag_from


@app.route('/auth', methods=['POST'])
@swag_from('../../api_docs/Auth/Post_Auth.yml')
def authenticate():
    return helpers.auth()
