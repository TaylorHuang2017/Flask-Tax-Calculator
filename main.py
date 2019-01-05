from flask import Flask, render_template, request
import tax

app = Flask(__name__)

@app.route('/cal', methods=['POST'])
def cal_tax() -> 'html':
    income = int(request.form['income'])
    insurance = int(request.form['insurance'])
    exemption = int(request.form['exemption'])
    before = income-insurance-exemption
    free = 5000 # 免征额
    rule = [
    (80000, 0.45, 15160),
    (55000, 0.35, 7160),
    (35000, 0.3, 4410),
    (25000, 0.25, 2660),     
    (12000, 0.2, 1410),
    (3000, 0.1, 210),
    (0,0.03, 0)
    ]
    title = '个税计算结果'
    mytax = tax.calc_tax(before,free,rule)
    aftertax_income = income - insurance - mytax
    return render_template('results.html',
                            the_title=title,
                            the_income=str(income),
                            the_insurance=str(insurance),
                            the_exemption=str(exemption),
                            the_tax=str(mytax),
                            the_aftertax_income=str(aftertax_income))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                            the_title='最新免费个税计算器')

if __name__ == '__main__':
    app.run(debug=True)