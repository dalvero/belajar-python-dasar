# CLEAR SCREEN FUNCTION
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# PRINT DIVIDER FUNCTION
def print_divider(char = '-', length = 60):
    print(char * length)

# PRINT TITLE FUNCTION
def print_title(title, char = '=', length = 60):
    print(title.center(length, char))