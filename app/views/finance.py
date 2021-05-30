from flask import request, render_template, redirect, abort
from app import app

class views:
  def page_not_found(self):
    return abort(404)

  # Render the index page
  def index(self,stocklist):
    return render_template('dashboard.html', stocklist=stocklist)

  def liquidity(self):
    return render_template('/Asset/liquidity.html')

  def efficiency(self):
    return render_template('/Asset/efficiency.html')

  def profitability(self):
    return render_template('/Sales/profitability.html')

  def safety(self):
    return render_template('/Business/safety.html')

  def related_party_transaction(self):
    return render_template('/Culture/related_party_transaction.html')