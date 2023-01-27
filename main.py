import time
import threading


class Castle:

    @staticmethod
    def draw():
        castle_art = [
            "   /\\      /\\   ",
            "  /  \\    /  \\  ",
            " /    \\  /    \\ ",
            "/      \\/      \\",
            "---------------",
            "  |          |",
            "  |          |",
            "  |          |",
            "  |          |",
            "  |          |",
            "---------------",
        ]

        for line in castle_art:
            print(line)

    def sign(self):
        print(f"It's a {self.__class__.__name__}!")
        print()
        time.sleep(3)


class WonderfulHall(Castle):

    @staticmethod
    def crystal_walls(material):
        walls_art = [
            " |---------|"" |---------|",
            " |  ***    |"" |   ***   |",
            " |   ***   |"" |  ***    |",
            " |   ***   |"" |   ***   |",
            " | ***     |"" | ***     |",
            " |   ***   |"" |   ***   |",
            " |   ***   |"" |   ***   |",
            " |     *** |"" |     *** |",
            " |---------|"" |---------|",
        ]

        for line in walls_art:
            print(line)

        print(f"The castle walls are made of {material}")
        print()
        time.sleep(3)

    def inside(self, *name):
        names = " and ".join([n.__class__.__name__ for n in name])
        print()
        print(f"{names} entered the {self.__class__.__name__}!")
        print()
        time.sleep(3)


class Furniture(WonderfulHall):
    def __init__(self, quality):
        self._quality = quality

    def luxurious_furniture(self, material):
        furniture_art = [
            "  __________",
            " |          |",
            " |__  __  __|",
            "",
            "        ____",
            "       |    |",
            "       |____|",
            "  ____       ",
            " |    |      ",
            " |____|      ",
        ]

        for line in furniture_art:
            print(line)

        print(f"This {self.__class__.__name__} is made of {material}")
        print()
        time.sleep(4)

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value

    @staticmethod
    def large_table():
        table_art = [
            " _______________",
            "|               |",
        ]

        for line in table_art:
            print(line)

        print()
        time.sleep(3)


class Kitchen(Castle):
    def __init__(self):
        self.output_lock = threading.Lock()

    def start_cook(self, name, tool):
        name = name.__class__.__name__
        with self.output_lock:
            print()
            print(f"Food is cooking by {name} using {tool}...")
        time.sleep(1)

    def cook_food(self):
        symbols = ["/", "|", "\\", "-", "/", "|", "\\", "-", "/", "|", "\\", "-", "/", "|", "\\", "-"]
        time.sleep(4)
        print()
        for symbol in symbols:
            with self.output_lock:
                print(f"\b{symbol}", end="", flush=True)
            time.sleep(0.5)

    def cut_fruits(self):
        with self.output_lock:
            print()
            print("Cutting fruits...")
        time.sleep(3)
        with self.output_lock:
            print("Fruits are cut.")

    def crush_almonds(self):
        with self.output_lock:
            print("Crushing almonds in a mortar...")
        time.sleep(3)
        with self.output_lock:
            print("Almonds are crushed.")

    def grate_roots(self):
        with self.output_lock:
            print("Grating roots...")
            print()
        time.sleep(3)
        with self.output_lock:
            print("Roots are grated.")

    def run_concurrently(self):
        threads = [threading.Thread(target=self.start_cook(princesses, princesses.little_white_hands())),
                   threading.Thread(target=self.cut_fruits), threading.Thread(target=self.crush_almonds),
                   threading.Thread(target=self.grate_roots),
                   threading.Thread(target=self.cook_food)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        with self.output_lock:
            print("A great lunch is ready")
            print()
            time.sleep(3)
        threading.Thread(target=self.cook_food)


class AllDishes(Kitchen):
    def __init__(self, quality):
        super().__init__()
        self._quality = quality

    @staticmethod
    def tableware(material):
        tableware_art = [
            "\\_/""   __",
            "   ""  |  |",
            "|__|""  ‾‾",
        ]

        for line in tableware_art:
            print(line)

        print(f"This tableware is made of {material}")
        print()
        time.sleep(3)

    @staticmethod
    def cutlery(material):
        cutlery_art = [
            " Ш""  o""  (|",
            " |""  |""   |",
        ]

        for line in cutlery_art:
            print(line)

        print(f"This cutlery is made of {material}")
        print()
        time.sleep(3)

    @staticmethod
    def golden_mortar():
        golden_mortar_art = [
            "  /",
            " o ",
            "\\_/",
        ]

        for line in golden_mortar_art:
            print(line)

        print()
        time.sleep(3)

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value


class Character:
    def sign(self):
        print("The name of the character...")
        print(f"It's {self.__class__.__name__}!")
        print()
        time.sleep(3)

    def walk(self):
        symbols = ["/", "\\", "/", "\\", "/", "\\"]
        for symbol in symbols:
            print(f"\b  {symbol}", end="", flush=True)
            time.sleep(0.5)

        print(f"{self.__class__.__name__} moves...")

    def inspect(self):
        print(f"{self.__class__.__name__} looks around...")
        eyes = [
            " o o ",
            "оо   ",
            " o o ",
            "   оo",
            " o o ",
            "оо   ",
            " o o ",
            "     ",
        ]
        for eye in eyes:
            print(f"\r{eye}", end="")
            time.sleep(0.5)

        print()

    def talk(self, name, words):
        name = name.__class__.__name__
        print(f"The character is talking... to {name}")
        print(f"{self.__class__.__name__}: {words}")
        print()

    def admiration(self, action, name):
        print("( ˘ ³˘)❤")
        action = action.__name__
        name = name.__class__.__name__
        print(f"{self.__class__.__name__} likes the {action} of {name}")
        print()
        time.sleep(3)

    def escort(self, place, *name):
        place = place.__class__.__name__
        names = " and ".join([n.__class__.__name__ for n in name])
        print(f"The {self.__class__.__name__} accompany {names} to the {place}!")
        print()
        time.sleep(1)

    def seat(self, place, *name):
        place = place.__name__
        names = " and ".join([n.__class__.__name__ for n in name])
        print(f"The {self.__class__.__name__} have seated {names} at the {place}!")
        print()

    def gift(self, name, gift):
        name = name.__class__.__name__
        gift = gift.__name__
        print(f"The {self.__class__.__name__} gave {name} a {gift}!")
        print()


class Nutcracker(Character):

    @staticmethod
    def draw():
        nutcracker_art = [
            "    _.-O-._",
            "   o_o_o_o_o",
            "   \\_`___`_/",
            "   } /. .\\ {",
            "  } | _c_ | {",
            " __}_\\www/_{__",
            "((((  { }  ))))",
        ]

        for line in nutcracker_art:
            print(line)


class Marie(Character):

    @staticmethod
    def draw():
        marie_art = [
            "  (((  '  )))",
            " (((  o o  )))",
            "((((   u   ))))",
            "((((\\  -  /))))",
            "   ___,H,___",
        ]

        for line in marie_art:
            print(line)


class Princesses(Character):

    @staticmethod
    def draw():
        princess_art = [
            "  /\\/\\  " "  /\\/\\  " "  /\\/\\  ",
            " /    \\ "  " /    \\ "  " /    \\ ",
            "(/    \\)"  "(/    \\)"  "(/    \\)",
            " \\    / "  " \\    / "  " \\    / ",
            "  \\/\\/  " "  \\/\\/  " "  \\/\\/  ",
        ]

        for line in princess_art:
            print(line)

    def talk(self, name, words):
        name = name.__class__.__name__
        print(f"The character is talking... to {name}")
        print(f"The youngest of the {self.__class__.__name__}: {words}")
        print()
        time.sleep(5)

    def little_white_hands(self):
        return self.little_white_hands.__name__


character = Character
nutcracker = Nutcracker()
marie = Marie()
princesses = Princesses()

castle = Castle()
wonderful_hall = WonderfulHall()
furniture = Furniture("pretty, small")
kitchen = Kitchen()
all_dishes = AllDishes("thinnest, cleanest")

nutcracker.draw()
nutcracker.sign()
marie.draw()
marie.sign()
castle.draw()
castle.sign()
princesses.draw()
princesses.sign()

princesses.escort(castle, nutcracker, marie)
nutcracker.walk()
marie.walk()

wonderful_hall.inside(nutcracker, marie, princesses)
marie.inspect()
wonderful_hall.crystal_walls("shiny multicolored crystals")
marie.inspect()
furniture.luxurious_furniture("cedar and Brazilian wood")
print(furniture.quality)
print()

princesses.seat(furniture.large_table, nutcracker, marie)
furniture.large_table()
marie.inspect()
all_dishes.tableware("Japanese porcelain")
all_dishes.cutlery("gold and silver")
print(all_dishes.quality)
print()

marie.inspect()
kitchen.run_concurrently()

marie.admiration(kitchen.cook_food, princesses)
princesses.gift(marie, all_dishes.golden_mortar)
all_dishes.golden_mortar()
princesses.talk(marie, "«— Вот возьми, милая спасительница нашего брата, и потолки эти карамельки».")

print("THE END")
time.sleep(1)
