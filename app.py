from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Wilmette Guys Baseball Homepage (coming soon)"
   
  
if __name__ == '__main__':
    app.run()


