from chalice import Chalice, Response
from jinja2 import FileSystemLoader, Environment
import os

app = Chalice(app_name='hcs3')

def render(tpl_path):
    path, filename = os.path.split(tpl_path)
    return Environment(loader=FileSystemLoader(path or      "./")).get_template(filename).render()

@app.route('/')
def index():
    template = render("index.html")
    return Response(template, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
