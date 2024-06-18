from flask import Flask
import os

from app import *

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)
    
