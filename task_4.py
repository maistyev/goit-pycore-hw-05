from typing import Dict, Tuple, Callable

def input_error(func: Callable) -> Callable:
    '''Decorator that handles exceptions in the input function'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except IndexError as e:
            return str(e)
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return wrapper

def parse_input(user_input: str) -> Tuple[str, str]:
    cmd, *args = user_input.split() # Split the input into command and arguments.
    cmd = cmd.strip().lower() # Convert the command to lowercase.
    return cmd, *args

@input_error
def add_contact(contacts: Dict, name: str, phone: str) -> str:
    '''Function that adds a contact to the dictionary and returns a string with the result
    If the contact already exists, the function returns a string with an error message'''
    if name in contacts:
        raise ValueError(f"Contact {name} already exists with phone number {contacts[name]}")
    contacts[name] = phone
    return f"Contact {name} has been added with phone number {phone}"

@input_error
def change_contact(contacts: Dict, name: str, phone: str) -> str:
    '''Function that changes the phone number of a contact in the dictionary and returns a string with the result
    If the contact does not exist, the function returns a string with an error message'''
    if name not in contacts:
        raise KeyError(f"Contact {name} does not exist")
    contacts[name] = phone
    return f"Contact {name} has been changed to phone number {phone}"

@input_error
def show_phone(contacts: Dict, name: str) -> str:
    '''Function that returns the string with phone number of a contact from the dictionary
    If the contact does not exist, the function returns a string with an error message'''
    if name not in contacts:
        raise KeyError(f"Contact {name} does not exist")    
    return f"Phone number for {name} is {contacts[name]}"

@input_error
def show_all(contacts: Dict) -> str:
    '''Function that returns string with all contacts from the dictionary
    If the dictionary is empty, the function returns a string with an error message'''
    if not contacts:
        raise Exception("No contacts found")
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)
        
        match command:
            case "hello":
                print("Hello! How can I help you?")
            case "add":
                if len(args) != 2:
                    print("Invalid number of arguments for command 'add'. Please enter a name and phone number")
                    continue
                print(add_contact(contacts, *args))
            case "change":
                if len(args) != 2:
                    print("Invalid number of arguments for command 'change'. Please enter a name and phone number")
                    continue
                print(change_contact(contacts, *args))
            case "phone":
                if len(args) != 1:
                    print("Invalid number of arguments for command 'phone'. Please enter a name")
                    continue
                print(show_phone(contacts, *args))
            case "all":
                print(show_all(contacts))
            case "close" | "exit":
                print("Goodbye!")
                break
            case "help":
                print("Commands:\n"
                      "hello - greet the bot\n"
                      "add [name] [phone] - add a contact\n"
                      "change [name] [phone] - change the phone number of a contact\n"
                      "phone [name] - show the phone number of a contact\n"
                      "all - show all contacts\n"
                      "close/exit - close the bot")
            case _:
                print("Invalid command. Please try again")
                print("Commands:\n"
                      "hello - greet the bot\n"
                      "add [name] [phone] - add a contact\n"
                      "change [name] [phone] - change the phone number of a contact\n"
                      "phone [name] - show the phone number of a contact\n"
                      "all - show all contacts\n"
                      "close/exit - close the bot")
                continue

if __name__ == "__main__":
    main()