from flask import Flask,render_template,request,jsonify

obj=Flask('__name__')

@obj.route('/')
def home():
    return 'Welcome to Flask'

@obj.route('/Calculator',methods=['GET'])
def calc():
    operation=request.json["operation"]
    num1=int(request.json["number1"])
    num2=int(request.json["number2"])

    if operation=='add':
        result=num1+num2
    elif operation=='div':
        result=num1/num2
    elif operation=='mul':
        result=num1*num2
    elif operation=='sub':
        result=num1-num2
    else: pass
    return jsonify(result)

if __name__=='__main__':
    obj.run(debug=False)