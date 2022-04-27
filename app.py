from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        labor_cost = 15
        material_cost = 25

        area_of_tank_top = pi * (radius * radius)
        area_of_tank_sides = 2 * (pi * (radius * height))
        total_area = area_of_tank_top + area_of_tank_sides
        total_sqft = total_area/144

        total_material_cost = total_sqft * material_cost
        total_labor_cost = total_sqft * labor_cost

        estimate = total_material_cost + total_labor_cost
        return render_template('estimate.html', data=estimate)
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)