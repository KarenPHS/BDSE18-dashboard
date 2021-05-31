from flask import url_for
import pandas as pd
from app import db
from app import app
from app.views.finance import views
from flask import request
from flask import jsonify
from app.models.StockList import stocklist

websites = views()
stock_list = None
# Index page
@app.route('/', methods=['GET'])
def index():
    return websites.index(stocklist)


@app.route('/stocks', methods=['POST'])
def stocks():
    """
    :params:
        slct_stock: list
            selected corp.
        type: str
            資料欄位
    :return:
    """
    request_data = request.get_json()
    # get param data
    if request_data == {'slct_stock': []}:
        pass
    else:
        print(request_data)
        slct_stock = request_data["slct_stock"]

        # query data from db
        sql_cmd = "select {}, company, abbr, time_q from two_year"
        stock_ids = [_id.split()[0] for _id in slct_stock]
        for idx in range(len(stock_ids)-1):
            sql_cmd += "company=\"{}\" or ".format(stock_ids[idx])
        sql_cmd += "company=\"{}\";".format(stock_ids[-1])
        df = pd.read_sql_query(sql_cmd, db.engine)

        # sort data by time
        df['datetime'] = pd.to_datetime(df['time_q'], format="%Y/%m")
        df.sort_values(by=['datetime'], inplace=True, ascending=True)
        # transform data to json
        # global df
        return "success"

@app.route('/Asset/liquidity', methods=['GET'])
def liquidity():
    return websites.liquidity(stocklist)

@app.route('/Asset/efficiency', methods=['GET'])
def efficiency():
    return websites.efficiency(stocklist)

@app.route('/Sales/profitability', methods=['GET'])
def profitability():
    return websites.profitability(stocklist)

@app.route('/Business/safety', methods=['GET'])
def safety():
    return websites.safety(stocklist)

@app.route('/Culture/related_party_transaction', methods=['GET'])
def related_party_transaction():
    return websites.related_party_transaction(stocklist)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run()