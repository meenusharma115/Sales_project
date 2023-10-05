import os
from flask import Flask, render_template, request, redirect, url_for
from calculations import calculate_total_revenue, calculate_average_price, find_best_selling_item, create_sales_trend_chart

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            upload_folder = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_folder)

            total_revenue = calculate_total_revenue(upload_folder)
            average_price = calculate_average_price(upload_folder)
            best_selling_item = find_best_selling_item(upload_folder)

            sales_trend_chart = url_for('plot_sales_trend', filename=filename)
            # chartpath= plot_sales_trend(upload_folder)
            # sales_trend_chart = url_for(chartpath)


            result = {
                'total_revenue': total_revenue,
                'average_price': average_price,
                'best_selling_item': best_selling_item,
                'filename': filename  # Pass the filename for the chart
            }

    return render_template('index.html', result=result)

@app.route('/plot_sales_trend/<filename>')
def plot_sales_trend(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    chart_path = create_sales_trend_chart(file_path)
    return chart_path



if __name__ == '__main__':
    app.run(debug=True)