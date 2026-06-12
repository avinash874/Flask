### Building Url dynamically
### Variable Rules And URL Building
### URL Building With url_for() Function

from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/') # route decorator
def welcome():
    return "Avinash Singh Create This App And This App is for learnig flask"

@app.route('/success/<int:score>')
def success(score):
    # return "The person has passed and the score is "+str(score)
    return "<html><body><h1>The Result is passed </h1></body></html>"

@app.route('/fail/<int:score>')
def fail(marks):
    return "The person has fail and the score is "+str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
  # url_for() function is used to build a URL to the specific function
if __name__=="__main__":
    app.run(debug=True)