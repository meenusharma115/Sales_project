import pandas as pd
import os
import matplotlib.pyplot as plt

def calculate_total_revenue(csv_file):
    df = pd.read_csv(csv_file, encoding='latin1')
    total_revenue = (df['Sales']).sum()
    return total_revenue

def calculate_average_price(csv_file):
    df = pd.read_csv(csv_file, encoding='latin1')
    average_price = df['Sales'].sum()/df['Quantity'].sum()
    return average_price

def find_best_selling_item(csv_file):
    df = pd.read_csv(csv_file, encoding='latin1')
    best_selling_item = df.loc[df['Quantity'].idxmax()]['Product Name']
    return best_selling_item

def create_sales_trend_chart(csv_file):
    df = pd.read_csv(csv_file, encoding='latin1')
    #df['date'] = pd.to_datetime(df['Order Date']).dt.to_period('M')
    df2=df.groupby(pd.to_datetime(df['Order Date']).dt.to_period('M'))['Sales'].sum().reset_index()
    df2.plot('Order Date','Sales')
    chart_filename = 'static/sales_trend.png'
    plt.savefig(chart_filename)
    chart_filename = 'static/sales_trend.png'
    plt.close()
    return chart_filename