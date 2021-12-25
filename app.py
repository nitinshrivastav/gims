#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def ashish():
    return render_template('ice.html')
@app.route('/userdetail',methods=['GET','POST'])
def hjggjjgjg():
    if(request.method=='POST'):
        n1=int(request.form['x'])
        n2=int(request.form['y'])
        total=n1+n2
        return render_template('ice.html',nitin=total)
if __name__=='__main__':
    app.run()

