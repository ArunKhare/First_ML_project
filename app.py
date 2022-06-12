import flask

app= flask('__name__')

@app.route('/index',methods=('GET','POST'))

def index():
    
    return 'CICD pipeline has been established'
if __name__ =="__main__":
    app.run(debug=True)