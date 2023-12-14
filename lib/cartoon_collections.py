
# import ipdb


def roll_call_dwarves(dwarf):
    for index, value in enumerate(dwarf):
        print(f'{index + 1}. {value}')


def summon_captain_planet(planeteer_calls):
    converted_list = [f"{x.title()}!" for x in planeteer_calls]
    return (converted_list)


def long_planeteer_calls(short_words):
    return any(len(call) > 4 for call in short_words)


def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]

    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None


# ipdb.set_trace()
