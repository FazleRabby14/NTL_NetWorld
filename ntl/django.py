from netlify_lambda_wsgi import make_lambda_handler
from myproject.wsgi import application  # Replace `myproject` with your project name

handler = make_lambda_handler(application)
