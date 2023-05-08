from flask import Blueprint, render_template, request
from flask_login import login_required, current_user



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


from flask import Flask
import requests
from bs4 import BeautifulSoup


@views.route('/stock')
@login_required
def stock():
    symbol = request.args.get('symbol')
    url = f'https://www.marketwatch.com/investing/stock/{symbol}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find_all('bg-quote', {'class': 'value'})[0].text
    return render_template('stock.html', symbol=symbol, price=price, user=current_user)



