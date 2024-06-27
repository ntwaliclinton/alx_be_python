# pattern_drawing.py

def draw_pattern():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))
        
        # Ensure the size is positive
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Use a while loop to iterate through each row
        row = 0
        while row < size:
            # Use a for loop to print asterisks in each row
            for _ in range(size):
                print("*", end="")
            # Print a newline character after completing each row
            print()
            row += 1
            
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    draw_pattern()

