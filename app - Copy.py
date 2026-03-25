from flask import Flask , render_template  #import the file 
app= Flask(__name__) #to store the done done function 
@app.route("/")#specify where my app needs to go to 
def home():#what the application is supposed to do
    return render_template("html_structure.html")

if __name__=="__main__":
    app.run(debug=True) #if this variable actually contaicn main function msde changes