# Portfolio Calculator

This project calculates the total portfolio value, gain/loss, and applies FIFO (First-In-First-Out) to manage transactions based on different brokers and schemes. It processes mutual fund transactions and computes the current value of the portfolio.

## Features

- **FIFO Transactions**: Ensures that older units are sold first.
- **Portfolio Summary**: Computes the current portfolio value, including remaining units and their market value.
- **Gain/Loss Calculation**: Calculates the total gain or loss based on current NAV and the cost price of units held.

## Assignment Tasks

1. **Total Portfolio Value**:
    - Calculated as the sum of remaining units multiplied by the NAV of each scheme.
    
2. **Total Portfolio Gain**:
    - Calculated as the difference between the current value and acquisition cost of units held.


## How to Run the Code

### Prerequisites

- Python 3.x
- Install the `mstarpy` library for fetching NAV data:
  
  ```bash
  pip install mstarpy
install mstarpy

Run the Script:
```bash
  python portfolio_calculator.py
