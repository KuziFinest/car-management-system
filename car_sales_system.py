# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize inventory and sales records
inventory = []  # List of dictionaries to store car inventory
sales_records = []  # List of dictionaries to store sales data


# Function to add a new car
def add_car():
    car = {
        "Brand": input("Enter car brand: "),
        "Model": input("Enter car model: "),
        "Price": float(input("Enter car price: ")),
        "Quantity": int(input("Enter car quantity: "))
    }
    inventory.append(car)
    print("Car added successfully!")


# Function to update car details
def update_car():
    model = input("Enter the car model to update: ")
    for car in inventory:
        if car["Model"] == model:
            print("Current details:", car)
            car["Price"] = float(input("Enter new price: "))
            car["Quantity"] = int(input("Enter new quantity: "))
            print("Car updated successfully!")
            return
    print("Car model not found!")


# Function to delete a car
def delete_car():
    model = input("Enter the car model to delete: ")
    global inventory
    inventory = [car for car in inventory if car["Model"] != model]
    print("Car deleted successfully!")


# Function to view inventory
def view_inventory():
    if not inventory:
        print("No cars in inventory!")
    else:
        df = pd.DataFrame(inventory)
        print("\nInventory:\n", df)


# Function to process a sale
def process_sale():
    model = input("Enter the car model to sell: ")
    for car in inventory:
        if car["Model"] == model and car["Quantity"] > 0:
            quantity = int(input("Enter quantity to sell: "))
            if quantity <= car["Quantity"]:
                car["Quantity"] -= quantity
                sales_records.append({
                    "Model": model,
                    "Quantity": quantity,
                    "Total Price": quantity * car["Price"]
                })
                print(f"Sold {quantity} units of {model}.")
                return
            else:
                print("Not enough quantity in stock!")
                return
    print("Car model not found or out of stock!")


# Function to analyze sales
def analyze_sales():
    if not sales_records:
        print("No sales records to analyze!")
        return

    # Convert sales_records to a DataFrame
    sales_df = pd.DataFrame(sales_records)
    
    print("\nSales Records:\n", sales_df)

    # Analyze best-selling models
    best_selling = sales_df.groupby("Model")["Quantity"].sum().sort_values(ascending=False)
    print("\nBest-Selling Models:\n", best_selling)

    # Revenue analysis
    total_revenue = sales_df["Total Price"].sum()
    print(f"\nTotal Revenue Generated: {total_revenue}")


# Function to generate visualizations
def generate_visualizations():
    if not sales_records:
        print("No sales data to visualize!")
        return

    # Convert sales_records to a DataFrame
    sales_df = pd.DataFrame(sales_records)

    # Bar chart: Sales per model
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Model", y="Quantity", data=sales_df.groupby("Model").sum().reset_index())
    plt.title("Sales per Model")
    plt.show()

    # Pie chart: Revenue contribution by model
    plt.figure(figsize=(8, 5))
    sales_df.groupby("Model")["Total Price"].sum().plot.pie(autopct="%1.1f%%")
    plt.title("Revenue Contribution by Model")
    plt.show()


# Main menu
def main_menu():
    while True:
        print("\nCar Sales Management System")
        print("1. Add New Car")
        print("2. Update Car Details")
        print("3. Delete Car")
        print("4. View Inventory")
        print("5. Process Sale")
        print("6. Analyze Sales")
        print("7. Generate Graphs")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_car()
        elif choice == 2:
            update_car()
        elif choice == 3:
            delete_car()
        elif choice == 4:
            view_inventory()
        elif choice == 5:
            process_sale()
        elif choice == 6:
            analyze_sales()
        elif choice == 7:
            generate_visualizations()
        elif choice == 8:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the system
main_menu()