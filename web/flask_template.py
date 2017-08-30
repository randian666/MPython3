#!/usr/bin/env python3

from flask import Flask,request,render_template
'''
一定要把模板放到正确的templates目录下
用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
'''
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username'];
    pwd=request.form['password'];
    if username=='admin' and pwd=='123456':
        re_params={'username':username}
        return render_template('signin-ok.html',**re_params)
    fail_params={'username':username,'message':'Bad username or password'}
    return render_template('form.html',**fail_params)

if __name__ == '__main__':
    app.run()