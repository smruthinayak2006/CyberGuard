def display_section(title):

    print("\n" + "=" * 50)

    print(title)

    print("=" * 50)



def display_dictionary(data):

    for key, value in data.items():

        formatted_key = key.replace("_", " ").title()

        print(f"{formatted_key}: {value}")