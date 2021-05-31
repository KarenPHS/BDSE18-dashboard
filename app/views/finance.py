from flask import request, render_template, redirect, abort
from app import app

class views:
  def page_not_found(self):
    return abort(404)

  # Render the index page
  def index(self,stocklist):
    return render_template('dashboard.html', stocklist=stocklist)

  def liquidity(self,stocklist):
    return render_template('/Asset/liquidity.html', stocklist=stocklist)

  def efficiency(self,stocklist):
    return render_template('/Asset/efficiency.html', stocklist=stocklist)

  def profitability(self,stocklist):
    return render_template('/Sales/profitability.html', stocklist=stocklist)

  def safety(self,stocklist):
    return render_template('/Business/safety.html', stocklist=stocklist)

  def related_party_transaction(self,stocklist):
    return render_template('/Culture/related_party_transaction.html', stocklist=stocklist)