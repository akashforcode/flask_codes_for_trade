from flask import Flask, render_template, request, jsonify, Response
from flask import Flask, render_template
from kite_trade import *

#########EXIT SERVER



app = Flask(__name__)

##########KITE login####################
#################VARIABLE DEFINE#############
call_strike="aa"
put_strike="bb"

lb=[47100, 47200, 47300, 47400, 47500]

#cspb=int(input("input strike price for current banknifty:::"))
cspb=46000
lb=[cspb-200,cspb-100,cspb,cspb+100,cspb+200]


f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:BANKNIFTY24MAR46000PE"))
################all option strike price###
from datetime import datetime, timedelta

def next_wednesday():
    today = datetime.today()
    days_ahead = (2 - today.weekday()) % 7  # Calculate days until next Wednesday (Wednesday is represented by 2)
    next_wednesday_date = today + timedelta(days=days_ahead)
    return next_wednesday_date.strftime("%Y-%m-%d")

print("Date of upcoming Wednesday:", next_wednesday())



yr=int(next_wednesday()[2:4])
mm=int(next_wednesday()[5:7])
dd=(next_wednesday()[8:10])
print(yr,mm,dd)

yr=str(yr)
mm=str(mm)
dd=str(dd)

datew=yr+mm+dd
bankoptionputpe="BANKNIFTY"+datew+"46800"+"PE"
print(bankoptionputpe)

#lb=[47100, 47200, 47300, 47400, 47500]

lbsp=[]
lbsc=[]
for i in range(5):
    bankoptionputpe="BANKNIFTY"+datew+str(lb[i])+"PE"
    bankoptionputce="BANKNIFTY"+datew+str(lb[i])+"CE"
    lbsp.append(bankoptionputpe)
    lbsc.append(bankoptionputce)
print(bankoptionputpe)
print(bankoptionputce)

print(lbsp)
print(lbsc)


#options = ['Option 1', 'Option 2', 'Option 3']
options =lbsc


#############FUNCTIONS###############
import time
def buy_option(n):
    for i in range(1):
        #print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              #tradingsymbol=e2.get(),
                              tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option(n):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              #tradingsymbol=e2.get(),
                              tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)

##############FUCNTION#############


###########LIVE
import pandas as pd




def generate_data():
    count = 0
    while True:
        yield f"data: {count}\n\n"
        count += 1
        time.sleep(1)

@app.route('/data')
def data():
    return Response(generate_data(), mimetype='text/event-stream')


###########LIVE







def function1():
    buy_option(15)
    # This is the first function you want to execute
    return "1 LOT QUANTITY BUY OPTION EXECUTED!"

def function2():
    sell_option(15)   
    # This is the second function you want to execute
    return "1 LOT QUANTITY SELL OPTION EXECUTED!"

def function3():
    buy_option(90)
    # This is the first function you want to execute
    return "6 LOT QUANTITY  BUY OPTION EXECUTED!"

def function4():
    sell_option(90)   
    # This is the second function you want to execute
    return "6 LOT QUANTITY SELL OPTION EXECUTED!"




@app.route('/execute_function1', methods=['POST'])
def execute_function1():
    if request.method == 'POST':
        result = function1()
        return jsonify({'result': result})

@app.route('/execute_function2', methods=['POST'])
def execute_function2():
    if request.method == 'POST':
        result = function2()
        return jsonify({'result': result})

@app.route('/execute_function3', methods=['POST'])
def execute_function3():
    if request.method == 'POST':
        result = function3()
        return jsonify({'result': result})

@app.route('/execute_function4', methods=['POST'])
def execute_function4():
    if request.method == 'POST':
        result = function4()
        return jsonify({'result': result})

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = None

    if request.method == 'POST':
        selected_option = request.form['option']

    return render_template('index.html', options=options, selected_option=selected_option)

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        selected_option = request.form['selected_option']
        action = request.form['action']
        result = f"Processing with {action} for {selected_option}"
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
