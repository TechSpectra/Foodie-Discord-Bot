ingredients_to_foods = {
    'tomatoes': ['spaghetti', 'salsa', 'caprese salad', 'tomato soup', 'pizza'],
    'chicken': ['grilled chicken', 'chicken curry', 'chicken soup', 'chicken tacos', 'chicken salad'],
    'rice': ['fried rice', 'rice pudding', 'stir-fry', 'rice and beans', 'rice paper rolls'],
    'eggs': ['omelette', 'scrambled eggs', 'fried rice', 'eggs benedict', 'deviled eggs'],
    'potatoes': ['mashed potatoes', 'french fries', 'potato salad', 'potato soup', 'potato pancakes'],
    'onions': ['onion rings', 'onion soup', 'caramelized onions', 'fajitas', 'onion dip'],
    'lettuce': ['salad', 'lettuce wraps', 'BLT sandwich', 'taco salad', 'caesar salad'],
    'broccoli': ['steamed broccoli', 'broccoli cheddar soup', 'stir-fried broccoli', 'broccoli casserole', 'roasted broccoli'],
    'carrots': ['carrot cake', 'carrot soup', 'glazed carrots', 'carrot salad', 'carrot and raisin salad'],
    'bell peppers': ['stuffed bell peppers', 'fajitas', 'bell pepper stir-fry', 'bell pepper pasta', 'bell pepper omelette'],
    'pasta': ['spaghetti', 'lasagna', 'fettuccine alfredo', 'penne alla vodka', 'macaroni and cheese'],
    'fish': ['grilled fish', 'fish tacos', 'fish and chips', 'baked fish', 'fish curry'],
    'shrimp': ['shrimp scampi', 'shrimp pasta', 'shrimp cocktail', 'spicy shrimp stir-fry', 'shrimp gumbo'],
    'beef': ['beef stew', 'beef stir-fry', 'beef tacos', 'beef burgers', 'roast beef'],
    'cheese': ['cheeseburger', 'grilled cheese sandwich', 'cheese omelette', 'macaroni and cheese', 'cheese fondue'],
    'mushrooms': ['mushroom soup', 'stuffed mushrooms', 'mushroom risotto', 'mushroom pizza', 'mushroom pasta'],
    'zucchini': ['zucchini noodles', 'zucchini bread', 'stuffed zucchini', 'zucchini fries', 'zucchini soup'],
    'avocado': ['avocado toast', 'guacamole', 'avocado salad', 'avocado sushi', 'avocado smoothie'],
    'spinach': ['spinach salad', 'spinach quiche', 'creamed spinach', 'spinach pasta', 'spinach and feta stuffed chicken'],
    'bacon': ['BLT sandwich', 'bacon and eggs', 'bacon-wrapped shrimp', 'bacon-wrapped asparagus', 'bacon mac and cheese'],
    'pork': ['pork chops', 'pork stir-fry', 'pulled pork sandwich', 'pork ribs', 'pork curry'],
    'corn': ['corn on the cob', 'corn chowder', 'cornbread', 'corn salad', 'corn salsa'],
    'peas': ['pea soup', 'mashed peas', 'pea and ham risotto', 'pea salad', 'pea and mint pasta'],
    'milk': ['milkshake', 'cereal with milk', 'rice pudding', 'pancakes', 'chocolate milk'],
    'bread': ['sandwich', 'toast', 'garlic bread', 'French toast', 'bread pudding'],
    'garlic': ['garlic bread', 'garlic shrimp', 'garlic roasted potatoes', 'garlic chicken', 'garlic pasta'],
    'bell peppers': ['stuffed bell peppers', 'fajitas', 'bell pepper stir-fry', 'bell pepper pasta', 'bell pepper omelette'],
    'cherry tomatoes': ['cherry tomato salad', 'pasta with cherry tomatoes', 'cherry tomato bruschetta', 'roasted cherry tomatoes', 'caprese skewers'],
    'lemon': ['lemonade', 'lemon chicken', 'lemon bars', 'lemon sorbet', 'lemon poppyseed muffins'],
    'lime': ['margarita', 'lime chicken', 'key lime pie', 'lime sorbet', 'lime rice'],
    'cucumber': ['cucumber salad', 'tzatziki sauce', 'cucumber sandwiches', 'cucumber soup', 'cucumber cocktails'],
    'apples': ['apple pie', 'apple crisp', 'apple sauce', 'caramel apples', 'apple coleslaw'],
    'honey': ['honey glazed chicken', 'honey mustard dressing', 'honey roasted carrots', 'honey butter', 'honey drizzled yogurt'],
    'chocolate': ['chocolate cake', 'chocolate chip cookies', 'chocolate mousse', 'chocolate fondue', 'chocolate milkshake'],
    'olive oil': ['salad dressing', 'roasted vegetables', 'marinades', 'pasta sauce', 'hummus'],
    'butter': ['baked goods', 'pancakes', 'sauteed vegetables', 'buttered toast', 'mashed potatoes'],
    'sugar': ['desserts', 'baking', 'sweet beverages', 'syrups', 'candied nuts'],
    'salt': ['seasoning', 'brines', 'cured meats', 'salted caramel', 'pickles'],
    'pepper': ['seasoning', 'sauces', 'roasted meats', 'stir-fries', 'grilled vegetables'],
    'cumin': ['curries', 'taco seasoning', 'chili', 'spicy dips', 'roasted vegetables'],
    'coriander': ['curries', 'salsas', 'spiced rice', 'marinades', 'stir-fries'],
    'ginger': ['ginger tea', 'stir-fries', 'gingerbread', 'marinades', 'spicy soups'],
    'garlic powder': ['seasoning', 'sauces', 'roasted meats', 'marinades', 'spicy dips'],
    'paprika': ['seasoning', 'sauces', 'roasted meats', 'soups', 'stuffed peppers'],
    'cinnamon': ['baking', 'desserts', 'spiced beverages', 'oatmeal', 'cinnamon rolls'],
    'vanilla extract': ['baking', 'desserts', 'smoothies', 'pancakes', 'ice cream'],
    'flour': ['bread', 'pasta', 'cakes', 'cookies', 'pie crust'],
    'oil': ['stir fry', 'sauteed vegetables', 'salad dressing', 'baked goods'], 
    'coffee': ['latte', 'cappuccino', 'iced coffee', 'coffee cake', 'tiramisu'],
    'celery': ['soup', 'stir fry', 'salad', 'stuffing', 'celery sticks with peanut butter'],
    'jalapeno': ['nachos', 'salsa', 'quesadillas', 'poppers', 'chili'],
    'mayonnaise': ['sandwiches', 'salads', 'dips', 'tuna salad', 'coleslaw'],
    'sour cream': ['tacos', 'baked potato topper', 'dips', 'cheesecake', 'stroganoff'],
    'cream cheese': ['cheesecake', 'dips', 'bagels', 'creamy sauces', 'frosting'],
    'peanut butter': ['sandwiches', 'cookies', 'pie', 'granola', 'with apples'],
    'chocolate chips': ['cookies', 'chocolate chip pancakes', 'trail mix', 'milkshakes', 'bark'],
    'banana': ['banana bread', 'smoothies', 'pancakes', 'banana pudding', 'ice cream'],
    'strawberries': ['shortcake', 'smoothies', 'salad', 'syrup', 'pie'],
    'blueberries': ['muffins', 'pancakes', 'syrup', 'pie', 'salad'],
    'walnuts': ['salad', 'trail mix', 'bakery items', 'walnut stuffed dates', 'cereal topping'],
    'almonds': ['almond butter', 'baked goods', 'salads', 'almond milk', 'granola'],
    'soy sauce': ['stir fry', 'marinade', 'dipping sauce', 'glaze', 'dressing'],
    'worcestershire': ['marinade', 'gravy', 'dips', ' Caesar dressing', 'bloody mary'],
    'yogurt': ['smoothies', 'parfaits', 'tzatziki', 'lassi', 'frozen yogurt'], 
    'oats': ['oatmeal', 'granola', 'cookies', 'muesli', 'bread'],
    'sesame seeds': ['topping for Asian foods', 'tahini', 'bagels', 'salads', 'stir fries'],
    'pineapple': ['pineapple upside down cake', 'smoothies', 'salsa', 'grilled', 'fried rice'], 
    'coconut': ['curry', 'pie', 'macaroons', 'rice', 'milk'],
    'turmeric': ['curry', 'soup', 'tea', 'rice', 'sauce'],
    'cranberries': ['trail mix', 'muffins', 'sauce', 'salad', 'relish'],
    'pumpkin': ['pie', 'soup', 'muffins', 'ravioli filling', 'risotto'],
    'basil': ['pesto', 'Caprese salad', 'pasta sauce', 'soups', 'basil lemonade'],
    'oregano': ['pizza', 'pasta sauce', 'salad dressing', 'meats', 'focaccia'],
    'parsley': ['tabbouleh', 'sauces', 'salads', 'garnish', 'chimichurri sauce'], 
    'mint': ['mojitos', 'desserts', 'salads', 'tea', 'chutney'],
    'rosemary': ['roasted meats', 'bread', 'sauces', 'herbed butter', 'cocktails'],
    'vinegar': ['salad dressing', 'pickles', 'sauces', 'marinades', 'shrubs'],
    'mustard': ['sandwiches', 'salad dressing', 'glaze', 'sauce', 'pretzels'],  
    'ketchup': ['burgers', 'fries', 'hot dogs', 'sauce', 'meatloaf'],
    'bbq sauce': ['ribs', 'chicken', 'burgers', 'meatballs', 'baked beans'],
    'soy beans': ['edamame', 'tofu', 'soy milk', 'tempeh', 'miso'],
    'lentils': ['dal', 'stew', 'salad', 'soup', 'bolognese'], 
    'quinoa': ['salad', 'pilaf', 'stuffed peppers', 'chili', 'burgers'],
    'chia seeds': ['pudding', 'smoothies', 'granola', 'yogurt', 'energy bars'],
    'greek yogurt': ['smoothies', 'dips', 'pancakes', 'salad dressing', 'tzatziki'],
    'mozzarella': ['pizza', 'caprese', 'lasagna', 'eggplant parm', 'stuffed shells'],
    'feta': ['salad', 'stuffed veggies', 'pasta', 'omelette', 'bruschetta'], 
    'prosciutto': ['pizza', 'pasta', 'antipasto', 'stuffed chicken', 'melons'],
    'balsamic vinegar': ['salad dressing', 'bruschetta', 'fruit dessert', 'glaze', 'risotto'],
    'sun dried tomatoes': ['pasta', 'pizza', 'sandwiches', 'salads', 'tapenade'],
    'capers': ['pasta puttanesca', 'tuna salad', 'chicken piccata', 'sauce', 'salad'],
    'celery': ['soup', 'stir fry', 'salad', 'stuffing', 'celery sticks with peanut butter'],
    'carrot': ['carrot cake', 'carrot soup', 'glazed carrots', 'carrot salad', 'carrot and raisin salad'], 
    'cabbage': ['coleslaw', 'stuffed cabbage rolls', 'soup', 'salad', 'sauerkraut'],
    'cauliflower': ['roasted cauliflower', 'cauliflower rice', 'soup', 'mash', 'pizza crust'],
    'sweet potato': ['roasted', 'fries', 'soup', 'pie', 'fritters'],
    'beet': ['pickled beets', 'borscht', 'salad', 'roasted', 'smoothies'],
    'butternut squash': ['soup', 'risotto', 'ravioli filling', 'roasted', 'curry'], 
    'eggplant': ['parmigiana', 'baba ganoush', 'stir fry', 'grilled', 'ratatouille'], 
    'zucchini': ['noodles', 'bread', 'stuffed', 'fries', 'soup'],
    'artichoke': ['dip', 'stuffed', 'pasta', 'pizza', 'risotto'],
    'asparagus': ['roasted', 'risotto', 'quiche', 'stir fry', 'soup'],
    'arugula': ['salad', 'pesto', 'pizza', 'sandwich', 'pasta'], 
    'broccoli rabe': ['sauteed', 'pasta', 'omelette', 'risotto', 'grilled'],
    'brussels sprouts': ['roasted', 'slaw', 'hash', 'soup', 'pasta'],
    'fennel': ['braised', 'salad', 'risotto', 'soup', 'grilled'],
}



def suggest_foods(ingredients):
    suggested_foods = set()
    for ingredient in ingredients:
        # Check for the ingredient in both singular and plural forms
        if ingredient in ingredients_to_foods:
            suggested_foods.update(ingredients_to_foods[ingredient])
        elif ingredient.endswith('s'):
            singular_form = ingredient[:-1]
            plural_form = ingredient
            if singular_form in ingredients_to_foods:
                suggested_foods.update(ingredients_to_foods[singular_form])
            elif plural_form in ingredients_to_foods:
                suggested_foods.update(ingredients_to_foods[plural_form])
    
    if suggested_foods:
        return suggested_foods
    else:
        return ["No specific suggestions based on the provided ingredients."]

"""user_input = input("Enter a list of raw ingredients (comma-separated): ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(',')]
suggested_foods = suggest_foods(user_ingredients)

print("Possible foods you can make with these ingredients:")
for food in suggested_foods:
    print("- " + food)"""
