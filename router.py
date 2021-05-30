from flask import url_for
from app import app
from app.views.finance import views
from flask import request
from jinja2 import TemplateNotFound
from app.models.StockList import stocklist

websites = views()

# Index page
@app.route('/', methods=['GET'])
def index():
    return websites.index(stocklist)

@app.route('/stocks', methods=['POST'])
def stocks():
    stocks = request.get_json()
    all_stocks=stocks[slct_stock]
    print(all_stocks)
    return "hello world"

@app.route('/Asset/liquidity', methods=['GET'])
def liquidity():
    return websites.liquidity()

@app.route('/Asset/efficiency', methods=['GET'])
def efficiency():
    return websites.efficiency()

@app.route('/Sales/profitability', methods=['GET'])
def profitability():
    return websites.profitability()

@app.route('/Business/safety', methods=['GET'])
def safety():
    return websites.safety()

@app.route('/Culture/related_party_transaction', methods=['GET'])
def related_party_transaction():
    return websites.related_party_transaction()

if __name__ == "__main__":
    app.run()