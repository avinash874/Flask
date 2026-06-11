### Building Url dynamically
### Variable Rules And URL Building
### URL Building With url_for() Function

from flask import Flask
app=Flask(__name__)

@app.route('/') # route decorator
def welcome():
    return "Avinash Singh Create This App And This App is for learnig flask"

if __name__=="__main__":
    app.run(debug=True)