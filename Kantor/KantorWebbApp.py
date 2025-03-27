from flask import Flask, render_template, request
import tools.databases.DBManager as dbmanager
import domain.currencies as currencies
import domain.resources as resources
import tools.converters.number_converters as number_converters

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def page():
    currencies_list = dbmanager.get_currencies()
    
    if request.method == "POST":
        errors_list = []
        cost = 0
        budget_input_value = request.form["budget"]
        currency = request.form["currency"]
        quantity_input_value = request.form["quantity"]
        currency_in_stock = dbmanager.get_resource_quantity(currency)
        
        try:
            quantity = number_converters.rounded_float(quantity_input_value)
        except ValueError:
            errors_list.append("Ilość musi być liczbą rzeczywistą,")
        
        try:
            budget = number_converters.rounded_float(budget_input_value)
            try:
                if budget >= 0 and quantity >= 0:
                    if quantity > currency_in_stock:
                        errors_list.append(f"Za mało {currency} w magazynie, dostepnych jest {currency_in_stock:.2f} {currency}")
                    else:
                        cost = currencies.cost_count(currency, quantity)
                        if budget >= cost:
                            resources.new_transaction(currency, quantity, cost)
                        else:
                            errors_list.append(f"Twój budżet jest zbyt mały, koszt wynosi {cost:.2f} PLN")
                            cost = 0
                else:
                    errors_list.append("Budżet i ilość muszą być liczbami nieujemnymi")
            except NameError:
                errors_list.append("Nie można obliczyć kosztu")
        except ValueError:
            errors_list.append("Budżet musi być liczbą rzeczywistą,")

        
        
        currencies_list = dbmanager.get_currencies()
        return render_template(
            "kantor.html",
            title="Kantor",
            error=(" ".join(errors_list)),
            data=currencies_list,
            cost=cost,
        )
    
    else:
        return render_template(
            "kantor.html",
            title="Kantor",
            data=currencies_list,
            cost = 0
            )

if __name__ == "__main__":
    app.run(debug=True)