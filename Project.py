#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class AccountingReport:
    """
    This class represents a financial report for a company, calculating various financial metrics 
    such as gross profit, operating profit, net profit, EBIT, tax, EAIT, and interest.
    """

    def __init__(self, company_name):
        """
        Initializes the accounting report with the company name and financial inputs.
        
        Args:
            company_name (str): Name of the company.
        """
        self.company_name = company_name
        self.sales = 0
        self.beginning_inventory = 0
        self.purchases = 0
        self.purchase_returns = 0
        self.purchase_discounts = 0
        self.freight = 0
        self.closing_inventory = 0
        self.cogs = 0
        self.operating_expenses = 0
        self.interest = 0
        self.tax_rate = 0

    def get_user_inputs(self):
        """
        Collects user inputs for the financial figures of the company.
        """
        print(f"\nEnter financial details for {self.company_name}:")
        
        self.sales = float(input("Enter total sales (in BDT): "))
        self.beginning_inventory = float(input("Enter beginning inventory (in BDT): "))
        self.purchases = float(input("Enter total purchases (in BDT): "))
        self.purchase_returns = float(input("Enter purchase returns (in BDT): "))
        self.purchase_discounts = float(input("Enter purchase discounts (in BDT): "))
        self.freight = float(input("Enter freight charges (in BDT): "))
        self.closing_inventory = float(input("Enter closing inventory (in BDT): "))
        self.operating_expenses = float(input("Enter total operating expenses (in BDT): "))
        self.interest = float(input("Enter total interest paid (in BDT): "))
        self.tax_rate = float(input("Enter tax rate (as a percentage, e.g., 20 for 20%): ")) / 100

    def calculate_cogs(self):
        """
        Calculates the cost of goods sold (COGS).
        
        Formula: COGS = Beginning Inventory + Purchases - Purchase Returns - Purchase Discounts + Freight - Closing Inventory
        """
        return (
            self.beginning_inventory + 
            self.purchases - 
            self.purchase_returns - 
            self.purchase_discounts + 
            self.freight - 
            self.closing_inventory
        )

    def calculate_gross_profit(self):
        """
        Calculates the gross profit as Sales - COGS.
        """
        self.cogs = self.calculate_cogs()
        return self.sales - self.cogs

    def calculate_operating_profit(self):
        """
        Calculates the operating profit as Gross Profit - Operating Expenses.
        """
        gross_profit = self.calculate_gross_profit()
        return gross_profit - self.operating_expenses

    def calculate_ebit(self):
        """
        Calculates the Earnings Before Interest and Taxes (EBIT).
        """
        return self.calculate_operating_profit()

    def calculate_net_profit_before_tax(self):
        """
        Calculates the Net Profit Before Tax as EBIT - Interest.
        """
        ebit = self.calculate_ebit()
        return ebit - self.interest

    def calculate_tax(self):
        """
        Calculates the tax amount as Net Profit Before Tax * Tax Rate.
        """
        net_profit_before_tax = self.calculate_net_profit_before_tax()
        return net_profit_before_tax * self.tax_rate

    def calculate_eait(self):
        """
        Calculates the Earnings After Interest and Taxes (EAIT).
        """
        net_profit_before_tax = self.calculate_net_profit_before_tax()
        tax = self.calculate_tax()
        return net_profit_before_tax - tax

    def generate_report(self):
        """
        Generates a detailed financial report for the company.
        """
        print("\nFinancial Report for", self.company_name)
        print("-" * 50)
        
        gross_profit = self.calculate_gross_profit()
        operating_profit = self.calculate_operating_profit()
        ebit = self.calculate_ebit()
        net_profit_before_tax = self.calculate_net_profit_before_tax()
        tax = self.calculate_tax()
        eait = self.calculate_eait()
        
        print(f"Sales: BDT {self.sales:.2f}")
        print(f"Beginning Inventory: BDT {self.beginning_inventory:.2f}")
        print(f"Purchases: BDT {self.purchases:.2f}")
        print(f"Purchase Returns: BDT {self.purchase_returns:.2f}")
        print(f"Purchase Discounts: BDT {self.purchase_discounts:.2f}")
        print(f"Freight: BDT {self.freight:.2f}")
        print(f"Closing Inventory: BDT {self.closing_inventory:.2f}")
        print(f"Cost of Goods Sold (COGS): BDT {self.cogs:.2f}")
        print(f"Gross Profit: BDT {gross_profit:.2f}")
        print(f"Operating Expenses: BDT {self.operating_expenses:.2f}")
        print(f"Operating Profit: BDT {operating_profit:.2f}")
        print(f"Earnings Before Interest and Taxes (EBIT): BDT {ebit:.2f}")
        print(f"Interest: BDT {self.interest:.2f}")
        print(f"Net Profit Before Tax: BDT {net_profit_before_tax:.2f}")
        print(f"Tax ({self.tax_rate * 100}%): BDT {tax:.2f}")
        print(f"Earnings After Interest and Taxes (EAIT): BDT {eait:.2f}")
        
        self.evaluate_performance(eait)

    def evaluate_performance(self, eait):
        """
        Evaluates the company's financial performance based on EAIT.
        """
        if eait > 0:
            print("\nConclusion: The company's financial performance is GOOD as it made a profit.")
        else:
            print("\nConclusion: The company's financial performance is BAD as it incurred a loss.")

if __name__ == "__main__":
    # Step 1: Get the company name from the user
    company_name = input("Enter the company's name: ")
    
    # Step 2: Create an instance of AccountingReport with the company name
    report = AccountingReport(company_name)
    
    # Step 3: Get financial details from the user
    report.get_user_inputs()
    
    # Step 4: Generate the financial report
    report.generate_report()


# In[ ]:




