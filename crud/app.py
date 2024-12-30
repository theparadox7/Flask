from flask import Flask


if __name__ == '__main__' :
    app = create_app()
    app.run('127.0.0.1') 
    