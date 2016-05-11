from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, Item, User
 
engine = create_engine('postgresql://catalog:sillypassword@localhost/catalog')
# connect to a databse catalog (with USER 'catalog' and PASSWORD 'sillypassword')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create a dummy user
User1 = User(name="Hello World", email="helloworld9711@helloworld.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# add 1st restaurant: UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")
session.add(restaurant1)
session.commit()

# add items for 1st restaurant
item1 = Item(user_id=1, name="French Fries", description="with garlic and parmesan", restaurant=restaurant1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce", restaurant=restaurant1)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream", restaurant=restaurant1)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Sirloin Burger", description="Made with grade A beef", restaurant=restaurant1)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Root Beer", description="16oz of refreshing goodness", restaurant=restaurant1)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Iced Tea", description="with Lemon", restaurant=restaurant1)
session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Grilled Cheese Sandwich", description="On texas toast with American Cheese", restaurant=restaurant1)
session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices", restaurant=restaurant1)
session.add(item8)
session.commit()


# add 2nd restaurant: Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")
session.add(restaurant2)
session.commit()

# add items for 2nd restaurant
item1 = Item(user_id=1, name="Chicken Stir Fry", description="with your choice of noodles vegetables and sauces", restaurant=restaurant2)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Peking Duck", description=" a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", restaurant=restaurant2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Spicy Tuna Roll", description="", restaurant=restaurant2)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Nepali Momo ", description="", restaurant=restaurant2)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Beef Noodle Soup", description="", restaurant=restaurant2)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Ramen", description="", restaurant=restaurant2)
session.add(item6)
session.commit()

# add 3rd restaurant: Panda Garden
restaurant3 = Restaurant(user_id=1, name="Panda Garden")
session.add(restaurant3)
session.commit()


item1 = Item(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", restaurant=restaurant3)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", restaurant=restaurant3)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", restaurant=restaurant3)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.", restaurant=restaurant3)
session.add(item4)
session.commit()


# add the 4th restaurant: Thyme for That Vegetarian Cuisine
restaurant4 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")
session.add(restaurant4)
session.commit()


item1 = Item(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", restaurant=restaurant4)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto", restaurant=restaurant4)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", restaurant=restaurant4)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", restaurant=restaurant4)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", restaurant=restaurant4)
session.add(item5)
session.commit()


# add the 5th restaurant: Tony's Bistro
restaurant5 = Restaurant(user_id=1, name="Tony\'s Bistro ")
session.add(restaurant5)
session.commit()


item1 = Item(user_id=1, name="Shellfish Tower", description="", restaurant=restaurant5)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken and Rice", description="", restaurant=restaurant5)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Mom's Spaghetti", description="", restaurant=restaurant5)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description="", restaurant=restaurant5)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg", restaurant=restaurant5)
session.add(item5)
session.commit()


# add the 5th restaurant: Andala's
restaurant6 = Restaurant(user_id=1, name="Andala\'s")
session.add(restaurant6)
session.commit()


item1 = Item(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.", restaurant=restaurant6)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms", restaurant=restaurant6)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.", restaurant=restaurant6)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!", description="", restaurant=restaurant6)
session.add(item4)
session.commit()


# add the 7th restaurant: Auntie Ann's
restaurant7 = Restaurant(user_id=1, name="Auntie Ann\'s Diner ")
session.add(restaurant7)
session.commit()

item0 = Item(user_id=1, name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy", restaurant=restaurant7)
session.add(item0)
session.commit()



item1 = Item(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness", restaurant=restaurant7)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast", restaurant=restaurant7)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices", restaurant=restaurant7)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.", restaurant=restaurant7)
session.add(item4)
session.commit()


# add the 8th restaurant:  Cocina Y Amor
restaurant8 = Restaurant(user_id=1, name="Cocina Y Amor ")

session.add(restaurant8)
session.commit()


item1 = Item(user_id=1, name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", restaurant=restaurant8)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Cachapa", description="Golden brown, corn-based venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ", restaurant=restaurant8)
session.add(item2)
session.commit()

print "added menu items!"

