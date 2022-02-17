from flask import Flask , request, render_template


app = Flask(__name__)

#Si no le dices a ROUTE que tipo de metodo HTTP, por defaul usara un GET
@app.route("/")
def index():
    return render_template("index.html")
 


#@app.route("/ebc")
#def HolaEbc():
 #   return"Hola EBC"

#@app.route("/ebc")
#def Welcomegym():
 #   return"Hola EBC"

#@app.route("/", methods=['POST'])
#def AddNewTask():
#  if request.method == 'POST':
      


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
