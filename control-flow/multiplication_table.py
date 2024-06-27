# multiplication_table.py

def multiplication_table():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Generate and print the multiplication table using a for loop
        for i in range(1, 10):
            product = number * i
            print(f"{number} * {i} = {product}")

        # The last iteration for 10
        product = number * 10
        print(f"{number} * 10 = {product}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    multiplication_table()

