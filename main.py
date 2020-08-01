from flask import Flask, jsonify



app = Flask(__name__)
app.config['DEBUG']= True
 
list = [
    {
        'id': 0,
        'fullname': 'godaddy',
        'phone': '4444444',
        'email': 'test@test.com'
        
    },
    {
        'id': 1,
        'fullname': 'Amazon',
        'phone': '454555',
        'email': 'test@test.com'
        
    },
    {
        'id': 2,
        'fullname': 'google',
        'phone': '43433444',
        'email': 'test@test.com'
        
    },
    {
        'id': 3,
        'fullname': 'Microsoft',
        'phone': '46767677',
        'email': 'test@test.com'
        
    },
]

@app.route('/', methods=['GET'])
def sercice():
    return "<h1> TALLER mi App </h1>"

@app.route('/v1/empresas', methods=['GET'])
def empresa():
    return jsonify (list)
@app.route('/v1/servicios', methods=['GET'])
def servicio():
    return jsonify (list)



if __name__ =='__main__':
  app.run()

