from flask import request, render_template, redirect, abort
from app import app

class views:
  def page_not_found(self):
    return abort(404)

  # Render the index page
  def index(self,stocklist, bankruptcy_stocklist):
    return render_template('dashboard.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist)

  def current_liab_current_assets(self,stocklist,bankruptcy_stocklist,current_liab_current_assets):
    return render_template('/Asset/current_liab_current_assets.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist, data=current_liab_current_assets)

  def l17(self, stocklist, bankruptcy_stocklist,l17):
    return render_template('/Asset/l17.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist, data=l17)

  def earning_before_tax_margin(self, stocklist, bankruptcy_stocklist,earning_before_tax_margin):
    return render_template('/Sales/earning_before_tax_margin.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist, data=earning_before_tax_margin)

  def Income_Before_Tax_and_Interests_assets(self, stocklist, bankruptcy_stocklist,Income_Before_Tax_and_Interests_assets):
    return render_template('/Sales/Income_Before_Tax_and_Interests_assets.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Income_Before_Tax_and_Interests_assets)

  def l3(self, stocklist, bankruptcy_stocklist,Income_Before_Tax_and_Interests_assets):
    return render_template('/Sales/l3.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Income_Before_Tax_and_Interests_assets)

  def l4(self, stocklist, bankruptcy_stocklist,l4):
    return render_template('/Sales/l4.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=l4)

  def negative_two_years(self, stocklist, bankruptcy_stocklist,negative_two_years):
    return render_template('/Sales/negative_two_years.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist, data=negative_two_years)

  def Net_Asset_Value_per_Share_F(self, stocklist, bankruptcy_stocklist, Net_Asset_Value_per_Share_F):
    return render_template('/Sales/Net_Asset_Value_per_Share_F.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist, data=Net_Asset_Value_per_Share_F)

  def net_income_change_rate(self, stocklist, bankruptcy_stocklist,net_income_change_rate):
    return render_template('/Sales/net_income_change_rate.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=net_income_change_rate)

  def Operating_margin(self, stocklist, bankruptcy_stocklist,Operating_margin):
    return render_template('/Sales/Operating_margin.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Operating_margin)

  def Retained_earnings_assets(self, stocklist, bankruptcy_stocklist,Retained_earnings_assets):
    return render_template('/Sales/Retained_earnings_assets.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Retained_earnings_assets)

  def Debt_Equity_Ratio(self, stocklist, bankruptcy_stocklist,Debt_Equity_Ratio):
    return render_template('/Business/Debt_Equity_Ratio.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Debt_Equity_Ratio)

  def debt_ratio(self, stocklist, bankruptcy_stocklist,debt_ratio):
    return render_template('/Business/debt_ratio.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=debt_ratio)

  def Interest_Coverage_Ratio(self, stocklist, bankruptcy_stocklist,Interest_Coverage_Ratio):
    return render_template('/Business/Interest_Coverage_Ratio.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=Interest_Coverage_Ratio)

  def ration_of_interest_expense(self, stocklist, bankruptcy_stocklist,ration_of_interest_expense):
    return render_template('/Business/ration_of_interest_expense.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=ration_of_interest_expense)

  def i69(self, stocklist, bankruptcy_stocklist,i69):
    return render_template('/Culture/i69.html', stocklist=stocklist, bankruptcy_stocklist=bankruptcy_stocklist,data=i69)

