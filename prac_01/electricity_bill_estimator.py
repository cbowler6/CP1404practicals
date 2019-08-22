TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    tariff = input("which tariff? 11 or 31:")
    daily_use = int(input("daily use(kWh)"))
    days_in_billing_period = int(input("how many days in the billing period:"))
    estimated_bill = tariff * daily_use * days_in_billing_period
    print("estimated bill:", estimated_bill)



main()
