from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def calculator_recipes(requests, recipes_name):
    recipe = DATA.get(recipes_name)
    if recipe:
        context = {'recipe': recipe}
        return render(requests, 'calculator/index.html', context)
    else:
        return render(requests, 'calculator/error.html', {'error_message': 'Recipe is not found'})