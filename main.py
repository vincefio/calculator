
from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Calculator')
import operator

#Create main frame
frm = ttk.Frame(root, padding=10, width=200, height=200, style='Danger.TFrame')
frm.grid()

firstNumber = None
secondNumber = None
allowNumbersInEntry = True
currentOperator = None

# Function to enter numbers into the entry
def enterNum(buttonNum):
    #print('function hit')
    global allowNumbersInEntry
    displayBox.insert("end",buttonNum)
    #if allowNumbersInEntry is False then erase the display box & set to true
    #print('allowNumbersInEntry is', allowNumbersInEntry)
    if allowNumbersInEntry == False:
        displayBox.delete(0, 'end')
        allowNumbersInEntry = True
        enterNum(buttonNum)

#make the Clear button work
def clearEntry(placeHolder):
    #currentEntry = displayBox.get()
    #print('clear Entry function hit with current entry being', currentEntry)
    displayBox.delete(0, 'end')

#Function for +/-/and / buttons
def operations(operator):
    #print('operator function working')
    #With each operator get what is currently in the entry in preparation for the next instructions
    global currentOperator
    currentEntry = displayBox.get()
    if operator =='+':
        #print('operator is addition')
        #addition function pass in currentEntry
        currentOperator = '+'
        addFunction(currentEntry)

    if operator=='-':
        #print('operator is subtraction')
        currentOperator = '-'
        addFunction(currentEntry)
    if operator=='/':
        currentOperator = '/'
        addFunction(currentEntry)
        #print('operator is division')

#addition function
def addFunction(firstEntry):
    global firstNumber
    global allowNumbersInEntry
    firstNumber = firstEntry
    allowNumbersInEntry = False
    #print('firstNumber for the addition equation is', firstNumber)
    #print('allowNumberInEntry is', allowNumbersInEntry)

#equals function
def equalsFunction(placeholder):
    global secondNumber
    secondNumber = displayBox.get()
    #print('Second number when = is', secondNumber)
    equationAndAnswer()

def equationAndAnswer():
    global firstNumber
    global secondNumber
    global currentOperator
    answer = None

    if currentOperator == '+':
        answer = int(firstNumber) + int(secondNumber)
        displayBox.delete(0, 'end')
        displayBox.insert("end", answer)
        #print('answer is', answer)
    if currentOperator == '-':
        answer = int(firstNumber) - int(secondNumber)
        displayBox.delete(0, 'end')
        displayBox.insert("end", answer)
    if currentOperator == '/':
        answer = int(firstNumber) / int(secondNumber)
        displayBox.delete(0, 'end')
        displayBox.insert("end", answer)

#Create text box
displayBox = ttk.Entry(frm, text='Full name:')
displayBox.grid(column=0, row=0, columnspan=3)

#Create Buttons
button1 = ttk.Button(frm, width=10, text="1", command= lambda arg1=1: enterNum(arg1))   #command=enterNum(1
button1.grid(column=0, row=1)

button2 = ttk.Button(frm, width=10, text="2", command= lambda arg1=2: enterNum((arg1)))
button2.grid(column=1, row=1)

button3 = ttk.Button(frm, width=10, text="3", command= lambda arg1=3: enterNum((arg1)))
button3.grid(column=2, row=1)

button4 = ttk.Button(frm, width=10, text="4", command= lambda arg1=4: enterNum((arg1)))
button4.grid(column=0, row=2)

button5 = ttk.Button(frm, width=10, text="5", command= lambda arg1=5: enterNum((arg1)))
button5.grid(column=1, row=2)

button6 = ttk.Button(frm, width=10, text="6", command= lambda arg1=6: enterNum((arg1)))
button6.grid(column=2, row=2)

button7 = ttk.Button(frm, width=10, text="7", command= lambda arg1=7: enterNum((arg1)))
button7.grid(column=0, row=3)

button8 = ttk.Button(frm, width=10, text="8", command= lambda arg1=8: enterNum((arg1)))
button8.grid(column=1, row=3)

button9 = ttk.Button(frm, width=10, text="9", command= lambda arg1=9: enterNum((arg1)))
button9.grid(column=2, row=3)

button0 = ttk.Button(frm, width=10, text="0", command= lambda arg1=0: enterNum((arg1)))
button0.grid(column=0, row=4)

buttonPlus = ttk.Button(frm, width=10, text="+", command= lambda arg1='+': operations(arg1))
buttonPlus.grid(column=1, row=4)

buttonMinus = ttk.Button(frm, width=10, text="-", command= lambda arg1='-': operations(arg1))
buttonMinus.grid(column=2, row=4)

buttonDivide = ttk.Button(frm, width=10, text="/", command= lambda arg1='/': operations(arg1))
buttonDivide.grid(column=0, row=5)

buttonClear = ttk.Button(frm, width=10, text="C", command= lambda arg1='placeHolder': clearEntry(arg1))  #figure out the clear
buttonClear.grid(column=1, row=5)

buttonEqual = ttk.Button(frm, width=10, text="=", command= lambda arg1='=': equalsFunction(arg1))
buttonEqual.grid(column=2, row=5)

root.mainloop()