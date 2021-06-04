#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: lucaspao
"""

# Create Flask App
from flask import Flask, request, render_template
app = Flask(__name__)


# Finds total balance of a document of items with balances like checks or a statement of invoices
def doc_sum(doc):
    sum = 0
    for entry in doc:
        sum += entry["amount"]
    return sum

# Example Data
invoice_statement_1 = [
    {"id": "500", "amount": 100},
    {"id": "501", "amount": 200},
    {"id": "502", "amount": 300},
    {"id": "503", "amount": 400},
    {"id": "504", "amount": 500},
]

invoice_statement_2 = [
    {"id": "505", "amount": 900},
    {"id": "506", "amount": 800},
    {"id": "507", "amount": 700},
    {"id": "508", "amount": 600},
    {"id": "509", "amount": 500},
]

invoice_statement_3 = [
    {"id": "510", "amount": 800},
    {"id": "511", "amount": 100},
    {"id": "512", "amount": 200},
    {"id": "513", "amount": 900},
    {"id": "514", "amount": 500},
]

invoice_statements = [
    {"name": "Invoice #1", "statement": invoice_statement_1, "total": doc_sum(invoice_statement_1)},
    {"name": "Invoice #2", "statement": invoice_statement_2, "total": doc_sum(invoice_statement_2)},
    {"name": "Invoice #3", "statement": invoice_statement_3, "total": doc_sum(invoice_statement_3)},
]

checks = [
    {"name": "Check #1", "id": "12345", "amount": 200},
    {"name": "Check #2", "id": "12346", "amount": 400},
    {"name": "Check #3", "id": "12347", "amount": 600},
    {"name": "Check #4", "id": "12348", "amount": 800},
    {"name": "Check #5", "id": "12349", "amount": 1000}
]    


# Renders static homepage from file "index.html"
@app.route("/")
def index():
    checks_sum = doc_sum(checks)
    
    invoices_sum = 0
    for statement in invoice_statements:
        invoices_sum += doc_sum(statement["statement"])
    
    return render_template(
        "index.html",
        
        # Variables passed to html file
        invoice_statements = invoice_statements,
        invoices_sum = invoices_sum,
        checks = checks,
        checks_sum = checks_sum,
        balance_sum = abs(checks_sum - invoices_sum)
    )

if __name__ == "__main__":
    app.run(debug=True)