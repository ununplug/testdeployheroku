from flask import Flask, render_template,request,redirect
import sqlite3
from flask.helpers import url_for
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
    with sqlite3.connect('FIFA_19.db') as conn:
        cur=conn.cursor()
        cur.execute("SELECT Position, Name, Value, Club, Jersey_Number, Overall FROM FIFAinfo;")
        conn.commit()
        all = cur.fetchmany(50)
        return render_template('index.html', datas=all)


@app.route("/search", methods=['POST'])
def search():

    if request.method == 'POST':
        check=request.form.getlist('check')
        keyword = request.form['keyword']
        selectnation = request.form['selectnation']
        selectpos = request.form['selectpos']
        posmin = request.form['posmin']
        posmax = request.form['posmax']
        selectatt = request.form['selectatt']
        attmin = request.form['attmin']
        attmax = request.form['attmax']
        weightmin = request.form['weightmin']
        weightmax = request.form['weightmax']
        heightmin = request.form['heightmin']
        heightmax = request.form['heightmax']
        prefer_foot = request.form['prefer_foot']
        weak_foot = request.form['weak_foot']
        skill_moves = request.form['skill_moves']
        inter_rep = request.form['inter_rep']
        agemin = request.form['agemin']
        agemax = request.form['agemax']
        work_atk = request.form['work_atk']
        work_df = request.form['work_df']


    stringtemp=""
    if check:
        for position in check:
            stringtemp+=position+","
        stringtemp=stringtemp[:-1]    
    if posmin=="":
        posmin = '0'
    else:
        pass
    if posmax=="":
        posmax = '99'
    else:
        pass
    if attmin=="":
        attmin = '0'
    else:
        pass
    if attmax=="":
        attmax = '99'
    else:
        pass
    if heightmin=="":
        heightmin = '0'
    else:
        pass
    if heightmax=="":
        heightmax = '300'
    else:
        pass  
    if weightmin=="":
        weightmin = '0'
    else:
        pass
    if weightmax=="":
        weightmax = '150'
    else:
        pass
    if agemin== "":
        agemin = '16'
    if agemax == "":
        agemax = '45'


    with sqlite3.connect('FIFA_19.db') as conn:
        cur=conn.cursor()
        if stringtemp=="":
            cur.execute("SELECT Position, Name, Value, Club, Jersey_Number, Overall FROM FIFAinfo WHERE Name like '%"+keyword+"%' AND Nationality like '%"+selectnation+"%' AND "+selectpos+" >= "+posmin+" AND "+selectpos+" <= "+posmax+" AND "+selectatt+" >= "+attmin+" AND "+selectatt+" <= "+attmax+" AND Weight >= "+weightmin+" AND Weight <= "+weightmax+" AND Height >= "+heightmin+" AND Height <= "+heightmax+" AND Preferred_Foot like '%"+prefer_foot+"%' AND Weak_Foot like '%"+weak_foot+"%' AND Skill_Moves like '%"+skill_moves+"%' AND International_Reputation like '%"+inter_rep+"%' AND Age >= "+agemin+" AND Age <= "+agemax+" AND Work_Rate like '"+work_atk+"%' AND Work_Rate like '%"+work_df+"' ")
        else:
            cur.execute("SELECT Position, Name, Value, Club, Jersey_Number, Overall FROM FIFAinfo WHERE Name like '%"+keyword+"%' AND Position IN ("+stringtemp+") AND Nationality like '%"+selectnation+"%' AND "+selectpos+" >= "+posmin+" AND "+selectpos+" <= "+posmax+" AND "+selectatt+" >= "+attmin+" AND "+selectatt+" <= "+attmax+" AND Weight >= "+weightmin+" AND Weight <= "+weightmax+" AND Height >= "+heightmin+" AND Height <= "+heightmax+" AND Preferred_Foot like '%"+prefer_foot+"%' AND Weak_Foot like '%"+weak_foot+"%' AND Skill_Moves like '%"+skill_moves+"%' AND International_Reputation like '%"+inter_rep+"%' AND Age >= "+agemin+" AND Age <= "+agemax+" AND Work_Rate like '"+work_atk+"%' AND Work_Rate like '%"+work_df+"' ")
        conn.commit()
        all = cur.fetchmany(50)
        return render_template('search.html',datas=all)
      
     
if __name__ == "__main__":
    app.run(debug=True)