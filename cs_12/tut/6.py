# Tax Calculator for FY 2023-24

income = float(input("Enter your annual income: ₹"))
investment = float(input("Enter your investment under Sec 80C: ₹"))
tax = 0

# --- Tax Calculation ---
if income <= 300000:
    tax = 0
elif income <= 700000:
    tax = (income - 300000) * 0.05
elif income <= 1000000:
    tax = (400000 * 0.05) + (income - 700000) * 0.10
elif income <= 1200000:
    tax = (400000 * 0.05) + (300000 * 0.10) + (income - 1000000) * 0.15
elif income <= 1500000:
    tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (income - 1200000) * 0.20
else:
    tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30

# --- Apply 80C Exemption ---
exemption = min(investment, 150000) * 0.30
exemption = min(exemption, 45000)

net_tax = tax - exemption
net_tax = max(net_tax, 0)

# --- Output ---
print("\n--- Tax Summary ---")
print(f"Gross Tax: ₹{tax:,.2f} per month or ₹{tax*12:,.2f} annually")
print(f"Exemption under Sec 80C: ₹{exemption:,.2f}")
print(f"Net Tax Payable: ₹{net_tax:,.2f}")