# from flask import Flask 
# app = Flask(__name__) 
# @app.route('/') 
# def hello(): return 'Hello, World!'

# from flask import Flask #flask 가죠오기
# import sys
# application = Flask(__name__) #flask name 선언 (application이라는 변수에 flask 프로젝트를 초기화시켜서 실행)

# @application.route("/") #flask 웹 페이지 경로 ( 우리가 위에사 생성한 application에 대한 route 경로 설정)
# #http://<우리 기본 주소>/ 와 같은 경로를 이야기
# def hello(): #경로에서 실행될 기능 선언
#     return "Hello goorm"

# if __name__ == "__main__":
#     application.run(host='127.0.0.1', port = 8000, debug= True) #호스트 주소와 port number 선언

from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
 
@app.route('/')
@app.route('/<int:num>')
def inputTest(num=None):
    return render_template('main.html', num=num)
    
@app.route('/calculate',methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputTest',num=temp))
 
if __name__ == '__main__':
    app.run(debug= True)

