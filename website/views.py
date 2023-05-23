from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from flask import Flask
import requests
from bs4 import BeautifulSoup


views = Blueprint('views', __name__)

def get_stock_data(stock_symbol):
    url = f"https://www.marketwatch.com/investing/stock/{stock_symbol}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    price = soup.find('bg-quote', class_='value').text
    closing_price = soup.find('td', class_='table__cell u-semi').text
    nested = soup.find('mw-rangebar', class_='element element--range range--yearly')
    lower = nested.find_all('span', class_='primary')[0].text
    upper = nested.find_all('span', class_='primary')[1].text
    rating = soup.find('li', class_='analyst__option active').text

    return {
        "Stock Symbol": stock_symbol,
        "Stock Price": price,
        "Closing Price": closing_price,
        "52-Week Range": f"{lower} - {upper}",
        "Analyst Rating": rating
    }

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    if request.method == 'POST':
        stock_symbol = request.form.get('stock_symbol')
        custom_symbol = request.form.get('custom_symbol')
        if stock_symbol or custom_symbol:
            stock_data = get_stock_data(stock_symbol or custom_symbol)

            return render_template('stock.html', stock_data=stock_data, user=current_user)
        else:
            return render_template('home.html', error_message='Please select or enter a stock symbol.', user=current_user)

    return render_template('home.html', user=current_user)







