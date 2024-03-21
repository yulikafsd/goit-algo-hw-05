def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            match func.__name__:
                case 'add_contact':
                    return "Wrong format. Please, enter: add [contact_name] [phone_number]."
                case 'change_contact':
                    return "Wrong format. Please, enter: change [contact_name] [phone_number]."
                case _:
                    return "ValueError"
        except KeyError:
            return "KeyError"
        except IndexError:
            if func.__name__ == 'show_phone':
                return "Wrong format. Please, enter: phone [contact_name]."
            else:
                return "IndexError"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    
    # якщо контакта з таким ім'ям немає, записати
    if contacts.get(args[0].lower()) == None:
        contacts[name.lower()] = phone
        return f"Contact {name.capitalize()} with phone {phone} added."
    
    # якщо контакт з таким ім'ям вже є, перепитати
    else:
        user_input = input("Contact with this name already exists.\nChange this contact? Y/N: ")
        if user_input.lower() == 'y':
            return change_contact(args, contacts)
        else:
            return "Contact was not changed."

@input_error
def change_contact(args, contacts):
    name, phone = args
    
    # Якщо ім'я не знайдено, пропонуємо додати
    if contacts.get(args[0].lower()) == None:
        user_input = input("Contact with this name was not found.\nAdd a new contact? Y/N: ")
        if user_input.lower() == 'y':
            return add_contact(args,contacts)
        else:
            return "Contact was not added."

    # Якщо ім'я знайдено, змінюємо
    else:
        contacts[name.lower()] = phone
        return f"{name.capitalize()}'s phone changed to: {phone}."

@input_error
def show_phone(args, contacts):
    name = args[0]

    # Повідомлення про помилку, якщо ім'я не знайдено
    if contacts.get(name.lower()) == None:
        return f"Contact with name {name.capitalize()} was not found"
    
    else:
        # Якщо знайдено, вивід: [номер телефону]
        return contacts[name.lower()]

@input_error
def show_all(contacts):
    
    if len(contacts) == 0:
        return "No contacts were found"
    
    contacts_string = ""
    for key, value in contacts.items():
        # тут простіше було б зробити одразу print кожного контакту, 
        # але за умовами ДЗ всі print мають бути в main, тому:
        contacts_string += f"\n{key.capitalize()}: {value}" 
    return f"Your contacts: {contacts_string}"

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args,contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                if len(command) == 1:
                    print("No command entered.")
                else:
                    print("Invalid command.")

if __name__ == "__main__":
    main()