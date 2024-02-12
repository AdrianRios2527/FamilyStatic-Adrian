from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)

    links_html = "".join(["<div class='display-4'><a href='" + y + "'>" + y + "</a></div>" for y in links])
    return f"""
        <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <style>
                @font-face {{
                    font-family: 'Roboto';
                    src: url('/fonts/Roboto-Regular.ttf') format('truetype');
                    /* Add more src declarations for other Roboto font weights/styles if needed */
                }}
                h1, h3 {{
                    font-family: 'Roboto', sans-serif;
                }}
            </style>
        </head>
        <body class="bg-dark text-white">
            <div class="container">
                <div class="text-center">
                    <h1 class="display-1">Diego Gómez</h1>
                    <h3 class="display-4">Family Static API</h3>
                    <hr/>
                    <ul class="list-unstyled">{links_html}</ul>
                </div>
            </div>
        </body>
        </html>
    """