import json

with open("transactions.json") as f:
    data = json.load(f)

transactions = data.get("data", [])

# Initialize the portfolio dictionary
portfolio = {}

for entry in transactions:
    dt_summary = entry.get("dtSummary", [])
    
    for trxn in dt_summary:
        scheme = trxn['isin']
        folio = trxn['folio']
        nav = float(trxn['nav'])
        closing_balance = float(trxn['closingBalance'])
        cost_value = float(trxn['costValue'])

        if scheme not in portfolio:
            portfolio[scheme] = {}
        if folio not in portfolio[scheme]:
            portfolio[scheme][folio] = {
                'total_units': 0,
                'current_nav': nav,
                'cost_value': 0,
                'market_value': 0
            }

        # Update units and values for each folio
        portfolio[scheme][folio]['total_units'] += closing_balance
        portfolio[scheme][folio]['cost_value'] += cost_value
        portfolio[scheme][folio]['market_value'] = closing_balance * nav

# Calculate total portfolio value and total portfolio gain
total_portfolio_value = 0
total_portfolio_gain = 0

print("Scheme-wise Portfolio Details:")
for scheme, folios in portfolio.items():
    for folio, details in folios.items():
        total_units = details['total_units']
        market_value = details['market_value']
        cost_value = details['cost_value']
        
        total_portfolio_value += market_value
        total_portfolio_gain += (market_value - cost_value)

        # Print details for each scheme and folio
        print(f"Scheme: {scheme}, Folio: {folio}")
        print(f"  Total Units: {total_units:.3f}")
        print(f"  Current Market Value: {market_value:.2f}")
        print(f"  Cost Value: {cost_value:.2f}")
        print(f"  Gain/Loss: {market_value - cost_value:.2f}")

# Print total values
print("\nTotal Portfolio Value: {:.2f}".format(total_portfolio_value))
print("Total Portfolio Gain: {:.2f}".format(total_portfolio_gain))
