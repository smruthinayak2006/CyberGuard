def display_section(title):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)



def display_dictionary(data):

    for key, value in data.items():

        formatted_key = key.replace("_", " ").title()

        print(f"\n{formatted_key}:")

        display_value(value)



def display_value(value):


    if isinstance(value, list):

        for item in value:

            if isinstance(item, dict):

                print("-" * 30)

                for k, v in item.items():

                    if v == 1:
                        v = True

                    elif v == 0:
                        v = False


                    print(
                        f"{k}: {v}"
                    )

            else:

                print(item)


    elif isinstance(value, dict):

        for k, v in value.items():

                    if v == 1:
                        v = True

                    elif v == 0:
                        v = False


                    print(
                        f"{k}: {v}"
                    )

    else:

        print(value)