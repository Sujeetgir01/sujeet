#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def sujeet():
    return render_template("D:sm.html")
@app.route("/sujeet",methods=["POST"])
def rs ():
    if request.method=="POST":
        num1=int (request.form["a"])
        num2=int (request.form["b"])
        t=num1+num2
        print(t)
        return render_template("d:sm.html",tiles=t)
if __name__=="__main__" :
    app.run()


# In[ ]:




