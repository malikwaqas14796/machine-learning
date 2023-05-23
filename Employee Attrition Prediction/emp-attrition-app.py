import pandas as pd
import importlib
import numpy as np
import seaborn as sns
from tkinter import *
from tkinter import Text, Tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import os

from sklearn.model_selection import train_test_split
from sklearn import linear_model, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import pylab as pl
# from sklearn.linear_model import LogisticRegression
from collections import Counter
import matplotlib.pyplot as plt

#creating login window
rootLogin = Tk()
rootLogin.geometry("500x400")
rootLogin.configure(background='white')
rootLogin.title("Attrition System Login")

#global variables for login input fields
user = StringVar()
paswd=StringVar()

#global variables for main window fields
ln=StringVar()
fn1 = StringVar()
fn2=StringVar()
fn3=StringVar()
fn4=StringVar()
fn5=StringVar()
fn6=StringVar()
fn7=StringVar()
fn8=StringVar()
fn9=StringVar()
fn10=StringVar()

#getting data_set of employees
data_set = pd.read_csv('Employee Attrition.csv')
C = pd.DataFrame(data_set)


#function which predicts attrition
def getAttrition():

    #getting field values
    entry_1=ln.get()
    entry_2=fn1.get()
    entry_3=fn2.get()
    entry_4=fn3.get()
    entry_5=fn4.get()
    entry_6=fn5.get()
    entry_7=fn6.get()
    entry_8=fn7.get()
    entry_9=fn8.get()
    entry_10=fn9.get()

    #converting field value to float
    ent_1 = float(entry_1)
    ent_2 = float(entry_2)
    ent_3 = float(entry_3)
    ent_4 = float(entry_4)
    ent_5 = float(entry_5)
    ent_6 = float(entry_6)
    ent_7 = float(entry_7)
    ent_8 = float(entry_8)
    ent_9 = float(entry_9)
    ent_10 = float(entry_10)

    #getting label
    Y = C.loc[:, 'Attrition']
    #X = C.loc[:, 'BusinessTravel':'YearWithCurrManager']

    #getting features
    X = C.loc[:,['Age','DailyRate','DistanceFromHome','EmployeeNumber','HourlyRate','MonthlyIncome','MonthlyRate','NumCompaniesWorked','TotalWorkingYears','OverTime']]

    #splitting data into testing and training 80% for testing and 20% for training
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    print("Keys" + str(data_set.keys()))
    #x_train = pd.get_dummies(X_train)
    #x_test = pd.get_dummies(X_test)
   # print(x_test);
    #y_train = pd.get_dummies(Y_train)
   # y_test = pd.get_dummies(Y_test)

    #print(x_train)
    #print(Y_test)

    #predecition models
    model = RandomForestClassifier()
    # model = linear_model.LinearRegression()
    # model = KNeighborsClassifier(n_neighbors=3)
    # model =DecisionTreeClassifier()

    #training model
    model.fit(x_train, y_train)
    tr_acc = []
    ts_acc = []

    #getting training and testing accuracy
    ts_acc.append(model.score(x_test, y_test))
    tr_acc.append(model.score(x_train, y_train))

    #prediction on input values
    x_new=[[ent_1,ent_2,ent_3,ent_4,ent_5,ent_6,ent_7,ent_8,ent_9,ent_10]]
    predict = model.predict(x_new)


    print("Prediction" + str(predict))
    predc=str(predict)
    print("Training Accuracy" + str(tr_acc))
    print("Testing Accuracy" + str(ts_acc))

    #checking if attrition or not message will be displayed accordingly
    if predc=="['Yes']":
        entry_11=fn10.set( "Employee will leave the company");
    elif predc=="['No']":
        entry_11 = fn10.set("Employee will not leave the company");

#feature selection function
def feature():

    Y = C.loc[:, 'Attrition']
    X = C.loc[:, 'BusinessTravel':'YearWithCurrManager']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # print("Keys" + str(data_set.keys()))
    x_train = pd.get_dummies(X_train)
    x_test = pd.get_dummies(X_test)

    y_train = pd.get_dummies(Y_train)
    y_test = pd.get_dummies(Y_test)

    # print(x_train)
    # print(Y_test)

    model = RandomForestClassifier()
    # model = linear_model.LinearRegression()
    # model = KNeighborsClassifier(n_neighbors=3)
    # model =DecisionTreeClassifier()
    model.fit(x_train, y_train)
    tr_acc = []
    ts_acc = []
    ts_acc.append(model.score(x_test, y_test))
    tr_acc.append(model.score(x_train, y_train))
    predict = model.predict(x_test)
    # print("Prediction" + str(predict))

    print("Training Accuracy" + str(tr_acc[0]))
    print("Testing Accuracy" + str(ts_acc[0]))
    cm = metrics.confusion_matrix(
        y_test.values.argmax(axis=1), predict.argmax(axis=1))

    # feature Importance
    f_imp = list(model.feature_importances_)
    f_imp.sort(reverse=True)
    x_train.columns
    th = f_imp[8]
    th_dict = {}
    cols = x_train.columns

    for idx, i in enumerate(model.feature_importances_):
        if i >= th:
            th_dict[cols[idx]] = (i * 100)

    sns.barplot(x=list(th_dict.values()), y=list(th_dict.keys()), orient='h')
    plt.xlabel("Importance")
    plt.ylabel("Features")
    cols_names = list(th_dict.keys())
    cols_names
    plt.show()

#function to display how many employees have left the company and how many stayed
def attritionlabel():

    data_set = pd.read_csv('Employee Attrition.csv')
    C = pd.DataFrame(data_set)

    #plotting the graph
    y_bar = np.array([C[C['Attrition'] == 'No'].shape[0]
                      , C[C['Attrition'] == 'Yes'].shape[0]])
    x_bar = ['No (0)', 'Yes (1)']  # Bar Visualization
    plt.bar(x_bar, y_bar,color='b')
    plt.xlabel('Labels/Classes')
    plt.ylabel('Number of Instances')
    plt.title('Distribution of Labels/Classes in the Dataset')
    plt.show()

#function to display number of female and male in the dataset
def gender():

    #plotting the graph
    y_bar = np.array([C[C['Gender'] == 'Female'].shape[0]
                         , C[C['Gender'] == 'Male'].shape[0]])
    x_bar = ['Female (0)', 'Male (1)']  # Bar Visualization
    plt.bar(x_bar, y_bar,color='r')
    plt.xlabel('Labels/Classes')
    plt.ylabel('Number of Instances')
    plt.title('Distribution of Labels/Classes in the Dataset')
    plt.show()
#function to display marital status graph
def marital():

    #plotting the graph
    y_bar = np.array([C[C['MaritalStatus'] == 'Single'].shape[0]
                     , C[C['MaritalStatus'] == 'Married'].shape[0],C[C['MaritalStatus'] == 'Divorced'].shape[0]],)
    x_bar = ['Single (0)', 'Married (1)','Divorced(2)']  # Bar Visualization
    plt.bar(x_bar, y_bar,color='g')
    plt.xlabel('Labels/Classes')
    plt.ylabel('Number of Instances')
    plt.title('Distribution of Labels/Classes in the Dataset')
    plt.show()

#plotting confusion matrix
def confmatrix():

    Y = C.loc[:, 'Attrition']
    X = C.loc[:, 'BusinessTravel':'YearWithCurrManager']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    print("Keys" + str(data_set.keys()))
    x_train = pd.get_dummies(X_train)
    x_test = pd.get_dummies(X_test)

    y_train = pd.get_dummies(Y_train)
    y_test = pd.get_dummies(Y_test)

    print(x_train)
    # print(Y_test)

    model = RandomForestClassifier()
    # model = KNeighborsClassifier(n_neighbors=3)

    # model =DecisionTreeClassifier()
    # model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    tr_acc = []
    ts_acc = []

    ts_acc.append(model.score(x_test, y_test))
    tr_acc.append(model.score(x_train, y_train))
    predict = model.predict(x_test)
    print("Prediction" + str(predict))

    print("Training Accuracy" + str(tr_acc))
    print("Testing Accuracy" + str(ts_acc))
    cm = metrics.confusion_matrix(
        y_test.values.argmax(axis=1), predict.argmax(axis=1))

    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax)
    plt.title("Confusion Matrix Using Random Forest")
    plt.show()

#function to get correlation between features and label
def heatMap():

    corr = C.corr()
    plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True)
    plt.title("Correlations HeatMap")
    plt.show()

#function to exit the system
def exitt():
    exit()

#main window that will be displayed right after login
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("dashboard bilal 5.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render,width="1800", height="1000")
        img.image = render
        img.place(x=-50, y=-30)


def mainwindow():
    username = user.get()
    password = paswd.get()

    #checking credentials
    if username=='1' and password=='1':

        #hiding login window
        rootLogin.withdraw()

        #creating main window on top level

        root=Toplevel()
        app = Window(root)
        #setting dimensions of main window


        root.geometry("1400x800")
        #root.configure(background='brown')
        #main window header
        root.title("Employee Dashboard")


        #main window input fields

        entry_1=Entry(root,textvar=ln)
        entry_1.place(x=345,y=195,height=30)


        entry_2=Entry(root,textvar=fn1)
        entry_2.place(x=345,y=232,height=30)


        entry_3=Entry(root,textvar=fn2)
        entry_3.place(x=345,y=270,height=30)


        entry_4=Entry(root,textvar=fn3)
        entry_4.place(x=345,y=308,height=30)



        entry_5=Entry(root,textvar=fn4)
        entry_5.place(x=345,y=345,height=30)


        entry_6=Entry(root,textvar=fn5)
        entry_6.place(x=345,y=382,height=30)


        entry_7=Entry(root,textvar=fn6)
        entry_7.place(x=345,y=425,height=30)


        entry_8=Entry(root,textvar=fn7)
        entry_8.place(x=345,y=465,height=30)


        entry_9=Entry(root,textvar=fn8)
        entry_9.place(x=345,y=510,height=30)


        entry_10=Entry(root,textvar=fn9)
        entry_10.place(x=345,y=550,height=30)

        entry_11=Entry(root,textvar=fn10,width=50, font=("TimesNewRoman",25,"bold"),fg='red' )
        entry_11.place(x = 645,   y = 575,  width=627,   height=91, )
        entry_11.config(state=DISABLED)

        #main window buttons
        b1=Button(root,text="SUBMIT",width=16,bg='forest green',fg='white', font=("TimesnewRoman",12,"bold"),command=getAttrition)
        b1.place(x=205,y=630)

        b2=Button(root,text="Heat Map",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=heatMap)
        b2.place(x=720,y=180)


        b3=Button(root,text="Job Satisfaction",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=print())
        b3.place(x=720,y=280)

        b4=Button(root,text="Confusion Matrix",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=confmatrix)
        b4.place(x=720,y=230)

        b5=Button(root,text="Selected Features",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=feature)
        b5.place(x=970,y=280)

        b6=Button(root,text="Male & Female",width=18,bg='gray11',fg='white',font=("arial",12,"bold"),command=gender)
        b6.place(x=970,y=230)

        b7=Button(root,text="Marital Details",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=marital)
        b7.place(x=970,y=180)

        b8=Button(root,text="Attrition Graph",width=18,bg='gray11',fg='white',font=("TimesnewRoman",12,"bold"),command=attritionlabel)
        b8.place(x=850,y=330)

        b9=Button(root,text="X",width=2,height=1,bg='red',fg='gray11',font=("TimesnewRoman",12,"bold"),command=exitt)
        b9.place(x=1286,y=36)

        #creating infinite loop for main window
        root.mainloop()
    #if wrong crdentials
    else:
        messagebox.showinfo("Error", "Wrong Credentials")



#Login window
class Login(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("logobilal2.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render,width="950", height="1000")
        img.image = render
        img.place(x=-250, y=-0)
#header
app1 = Login(rootLogin)
#loginLabel= Label (rootLogin, text="Sign In", relief="solid",width=10,bg='yellow',fg='black',font=("TimesNewRoman",20,"bold"))
#loginLabel.place(x=150,y=30)

#username field and label
usernameLabel=Label(rootLogin,text="User Name",relief="solid",width=18,bg='DarkGoldenrod1',fg='black',font=("TimesNewRoman",10,"bold"))
usernameLabel.place(x=80,y=170)
username=Entry(rootLogin,textvar=user,width=24,bg='gray20',fg='white')
username.place(x=250,y=170)

#password field and label
passwordLabel=Label(rootLogin,text="Password",relief="solid",width=18,bg='DarkGoldenrod1',fg='black',font=("TimesNewRoman",10,"bold"))
passwordLabel.place(x=80,y=230)
password=Entry(rootLogin,textvar=paswd,width=24,bg='gray20',fg='white')
password.place(x=250,y=230)
password.config(show="*")
#login button
loginbutton=Button(rootLogin,text="Login",width=10,bg='forestgreen',fg='white',font=("TimesnewRoman",10,"bold"),command=mainwindow)
loginbutton.place(x=200,y=290)

#infinite loop for login window
rootLogin.mainloop()

