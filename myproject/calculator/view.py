from flask import render_template, Blueprint
from myproject.calculator.forms import UserIncomeForm, Theme
from myproject.modles import UserIncome, db

calculator_blueprint = Blueprint('calculator', __name__)


def GrossSalaryCalculator(basic, da, hra, conveyance, lta, others):
    return basic + da + hra + conveyance + lta + others


def HRA(basic, city, job, hra=100000000, da=0, rent=100000000):
    if city == '1' and job == '1':
        return min(abs(hra), abs(basic * 0.5), abs(rent - (basic * 0.1)))
    elif city == '1' and job == '2':
        return min(abs(hra), abs((basic + da) * 0.5), abs(rent - (basic * 0.1)))
    elif city == '2' and job == '1':
        return min(abs(hra), abs(basic * 0.4), abs(rent - (basic * 0.1)))
    elif city == '2' and job == '2':
        return min(abs(hra), abs((basic + da) * 0.4), abs(rent - (basic * 0.1)))


def IncomeChargeable(gross_salary, professional_tax=0, hra_rebate=0):
    return gross_salary - (50000 + professional_tax + hra_rebate)


def TaxableIncome(income_chargeable, ac, ad, add, addb, ae, ag, agg, agga, aggc, atta, au):
    return income_chargeable - (ac + ad + add + addb + ae + ag + agg + agga + aggc + atta + au)


def TaxIncome(taxable_income):
    if taxable_income < 250000:
        return 0
    elif taxable_income < 500000:
        return (taxable_income - 250000) * 0.05
    elif taxable_income < 1000000:
        return (taxable_income - 500000) * 0.2 + 12500
    else:
        return (taxable_income - 1000000) * 0.3 + 112500


def TaxRebate(taxable_income, tax_in_income):
    if taxable_income <= 500000:
        return tax_in_income
    else:
        return 0


def HnECess(tax_in_income):
    if tax_in_income > 12500:
        return tax_in_income * 0.04
    else:
        return 0


def TaxPayable(tax_in_income, tax_rebate, cess):
    return tax_in_income + cess - tax_rebate


@calculator_blueprint.route('/income', methods=['GET', 'POST'])
def income():
    form = UserIncomeForm()
    theme = '1'
    form1 = Theme()
    if form1.validate_on_submit():
        theme = form1.theme.data
    if form.validate_on_submit():
        gross_salary = GrossSalaryCalculator(form.basic.data, form.da.data, form.hra.data,
                                             form.conveyance.data, form.lta.data,
                                             form.others.data)

        hra_calculation = HRA(form.basic.data, form.city.data, form.job.data, form.hra.data, form.da.data,
                              form.rent.data)

        income_chargeable = IncomeChargeable(gross_salary, form.p_tax.data, hra_calculation)

        taxable_income = TaxableIncome(income_chargeable, form.ac.data, form.ad.data, form.add.data, form.addb.data,
                                       form.ae.data, form.ag.data, form.agg.data, form.agga.data, form.aggc.data,
                                       form.atta.data, form.au.data)

        tax_in_income = TaxIncome(taxable_income)

        tax_rebate = TaxRebate(taxable_income, tax_in_income)

        cess = HnECess(tax_in_income)

        tax_payable = TaxPayable(tax_in_income, tax_rebate, cess)

        user_details = UserIncome(name=form.name.data, age=form.age.data, city=form.city.data, job=form.job.data,
                                  basic=form.basic.data,
                                  da=form.da.data, hra=form.hra.data, conveyance=form.conveyance.data,
                                  lta=form.lta.data, others=form.others.data, rent=form.rent.data,
                                  professional_tax=form.p_tax.data, ac=form.ac.data, ad=form.ad.data, add=form.add.data,
                                  addb=form.addb.data, ae=form.ae.data, ag=form.ag.data, agg=form.agg.data,
                                  agga=form.agga.data, aggc=form.aggc.data, atta=form.atta.data, au=form.au.data)

        db.session.add(user_details)
        db.session.commit()

    else:
        gross_salary = hra_calculation = income_chargeable = taxable_income = cess = 0
        tax_in_income = tax_rebate = tax_payable = 0

    return render_template('income.html', form=form, form1=form1, theme=theme, gross_salary=gross_salary,
                           hra_calculation=hra_calculation,
                           income_chargeable=income_chargeable, taxable_income=taxable_income, cess=cess,
                           tax_in_income=tax_in_income, tax_rebate=tax_rebate, tax_payable=tax_payable)