import pyautogui as pg

def get_user_input():
    while True:
        try:
            user_input = pg.prompt("Please enter a response:\n\n1. Yes\n2. No", title="User Input", default="")
            if user_input is None:
                raise ValueError("User closed the input dialog")
            
            if user_input.lower() in ['yes', 'no']:
                return user_input.lower()
            else:
                pg.alert("Invalid input. Please enter 'Yes' or 'No'.", title="Error")
        except Exception as e:
            pg.alert(f"An error occurred: {str(e)}", title="Error")

def main():
    pg.alert("Welcome to the Advanced User Interaction Script!", title="Greetings")

    while True:
        response = get_user_input()

        if response == 'yes':
            pg.alert("Thank you for your honesty. Exiting the script.", title="Goodbye")
            break
        elif response == 'no':
            pg.alert("That's great to hear! Let's continue.", title="Continue")

if __name__ == "__main__":
    main()
