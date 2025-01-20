# Create the file and write initial data
with open("product.txt", "w") as file:
    file.write("1,apple,100,10\n")
    file.write("2,banana,200,20\n")
    file.write("3,orange,300,30\n")

# Add new products
def add_product(product_id, product_name, product_price, product_stock):
    with open("product.txt", "a") as file:
        file.write(f"{product_id},{product_name},{product_price},{product_stock}\n")

add_product(4, "mango", 400, 10)
add_product(5, "grape", 500, 20)

# View all products
def view_product():
    with open("product.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# Purchase a product
def purchase_product(product_id, quantity):
    updated_products = []
    product_found = False
    with open("product.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            prod_id, product_name, product_price, product_stock = line.strip().split(",")
            if int(prod_id) == product_id:
                product_found = True
                if int(product_stock) >= quantity:
                    product_stock = int(product_stock) - quantity
                    print(f"Purchase of {quantity} {product_name} successful.")
                else:
                    print(f"Insufficient stock for {product_name}.")
                    product_stock = int(product_stock)  # Retain original stock
            updated_products.append(f"{prod_id},{product_name},{product_price},{product_stock}\n")
    
    if not product_found:
        print(f"Product with ID {product_id} not found.")

    # Write the updated data back to the file
    with open("product.txt", "w") as file:
        file.writelines(updated_products)

# Test the functions
view_product()
purchase_product(1, 2)
view_product()

