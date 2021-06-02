import json
import pandas as pd
from app import db
from app import app
from app.views.finance import views
from flask import request
from app.models.StockList import stocklist, bankruptcy_stocklist

websites = views()
Retained_earnings_assets = None
negative_two_years = None
earning_before_tax_margin = None
Income_Before_Tax_and_Interests_assets = None
Operating_margin = None
Debt_Equity_Ratio = None
Net_Asset_Value_per_Share_F = None
ration_of_interest_expense = None
l4 = None
i69 = None
net_income_change_rate = None
l3 = None
l17 = None
Interest_Coverage_Ratio = None
current_liab_current_assets = None
debt_ratio = None
stock_ids_cache = None
# Index page
@app.route('/', methods=['GET'])
def index():
    return websites.index(stocklist, bankruptcy_stocklist)


@app.route('/stocks', methods=['POST'])
def stocks():
    """
    :params:
        slct_stock: list
            selected corp.
    :return:
    """
    # get param data
    request_data = request.get_json()
    slct_stock = request_data["slct_stock"]

    # query data from db
    sql_cmd = "select * from two_year where "
    stock_ids = [_id.split()[0] for _id in slct_stock]

    global stock_ids_cache
    if stock_ids == stock_ids_cache:
        return "success"
    elif not stock_ids:
        return "success"
    else:
        stock_ids_cache = stock_ids
    for idx in range(len(stock_ids)-1):
        sql_cmd += "company=\"{}\" or ".format(stock_ids[idx])
    sql_cmd += "company=\"{}\";".format(stock_ids[-1])
    df = pd.read_sql_query(sql_cmd, db.engine)

    # *100%
    df['Retained_earnings_assets']=df['Retained_earnings_assets']*100
    df['Income_Before_Tax_and_Interests_assets']=df['Income_Before_Tax_and_Interests_assets']*100
    df['current_liab_current_assets']=df['current_liab_current_assets']*100

    # sort data by time
    df['datetime'] = pd.to_datetime(df['time_q'], format="%Y/%m")
    df.sort_values(by=['datetime'], inplace=True, ascending=True)
    # transform data to json

    for type in ["Retained_earnings_assets","negative_two_years","earning_before_tax_margin","Income_Before_Tax_and_Interests_assets","Operating_margin","Debt_Equity_Ratio","Net_Asset_Value_per_Share_F","ration_of_interest_expense","l4","i69","net_income_change_rate","l3","l17","Interest_Coverage_Ratio","current_liab_current_assets","debt_ratio"]:
        return_data = dict()
        if type == "negative_two_years":
            for idx, row in df.iterrows():
                abbr = row.get("abbr")
                time = row.get("time_q")
                value = row.get(type)
                if time not in return_data:
                    return_data[time] = dict()
                if "values" not in return_data[time]:
                    return_data[time]["values"] = list()
                if "categorie" not in return_data[time]:
                    return_data[time]["categorie"] = time

                return_data[time]["values"].append({
                    "value": value,
                    "rate": abbr
                })
        else:
            for idx, row in df.iterrows():
                abbr = row.get("abbr")
                time = row.get("time_q")
                value = row.get(type)
                if time not in return_data:
                    return_data[time] = dict()
                return_data[time]["Time"] = time
                return_data[time][abbr] = value
        globals()[type] = json.dumps(list(return_data.values()),ensure_ascii=False)
    return "success"

@app.route('/Asset/current_liab_current_assets', methods=['GET'])
def current_liab_current_assets():
    return websites.current_liab_current_assets(stocklist, bankruptcy_stocklist,current_liab_current_assets)

@app.route('/Asset/l17', methods=['GET'])
def l17():
    return websites.l17(stocklist, bankruptcy_stocklist,l17)

@app.route('/Sales/earning_before_tax_margin', methods=['GET'])
def earning_before_tax_margin():
    return websites.earning_before_tax_margin(stocklist, bankruptcy_stocklist,earning_before_tax_margin)

@app.route('/Sales/Income_Before_Tax_and_Interests_assets', methods=['GET'])
def Income_Before_Tax_and_Interests_assets():
    return websites.Income_Before_Tax_and_Interests_assets(stocklist, bankruptcy_stocklist,Income_Before_Tax_and_Interests_assets)

@app.route('/Sales/l3', methods=['GET'])
def l3():
    return websites.l3(stocklist, bankruptcy_stocklist,l3)

@app.route('/Sales/l4', methods=['GET'])
def l4():
    return websites.l4(stocklist, bankruptcy_stocklist,l4)

@app.route('/Sales/negative_two_years', methods=['GET'])
def negative_two_years():
    return websites.negative_two_years(stocklist, bankruptcy_stocklist,negative_two_years)

@app.route('/Sales/Net_Asset_Value_per_Share_F', methods=['GET'])
def Net_Asset_Value_per_Share_F():
    return websites.Net_Asset_Value_per_Share_F(stocklist, bankruptcy_stocklist,Net_Asset_Value_per_Share_F)

@app.route('/Sales/net_income_change_rate', methods=['GET'])
def net_income_change_rate():
    return websites.net_income_change_rate(stocklist, bankruptcy_stocklist,net_income_change_rate)

@app.route('/Sales/Operating_margin', methods=['GET'])
def Operating_margin():
    return websites.Operating_margin(stocklist, bankruptcy_stocklist,Operating_margin)

@app.route('/Sales/Retained_earnings_assets', methods=['GET'])
def Retained_earnings_assets():
    return websites.Retained_earnings_assets(stocklist, bankruptcy_stocklist,Retained_earnings_assets)

@app.route('/Business/Debt_Equity_Ratio', methods=['GET'])
def Debt_Equity_Ratio():
    return websites.Debt_Equity_Ratio(stocklist, bankruptcy_stocklist,Debt_Equity_Ratio)

@app.route('/Business/debt_ratio', methods=['GET'])
def debt_ratio():
    return websites.debt_ratio(stocklist, bankruptcy_stocklist,debt_ratio)

@app.route('/Business/Interest_Coverage_Ratio', methods=['GET'])
def Interest_Coverage_Ratio():
    return websites.Interest_Coverage_Ratio(stocklist, bankruptcy_stocklist,Interest_Coverage_Ratio)

@app.route('/Business/ration_of_interest_expense', methods=['GET'])
def ration_of_interest_expense():
    return websites.ration_of_interest_expense(stocklist, bankruptcy_stocklist,ration_of_interest_expense)

@app.route('/Culture/i69', methods=['GET'])
def i69():
    return websites.i69(stocklist, bankruptcy_stocklist,i69)


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=5000)