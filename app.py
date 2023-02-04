import logging
import re
from enum import IntEnum, unique

from flask import Flask

app = Flask(__name__)


oid = 0


class Ships:
    """
    A class that represents a number of ships on a fleet.
    """

    def __init__(self, ships: int, cargo: int):
        self.ships = ships if ships <= 255 else 255
        self.cargo = cargo if cargo <= 255 else 255

    def effective_firepower(self):
        return self.ships - self.cargo if self.ships > self.cargo else 0

    def update(self, ships: int, cargo: int = None):
        self.ships = ships if ships <= 255 else 255
        self.cargo = cargo if cargo <= 255 else 255

    def increase(self, ships: int):
        self.ships += ships
        self.ships = self.ships if self.ships <= 255 else 255

    def decrease(self, ships: int):
        self.ships -= ships
        self.ships = self.ships if self.ships >= 0 else 0

    def load(self, cargo: int):
        self.cargo += cargo
        self.cargo = self.cargo if self.cargo <= 255 else 255

    def unload(self, cargo: int):
        self.cargo -= cargo
        self.cargo = self.cargo if self.cargo >= 0 else 0

    def __str__(self):
        return str(self.ships) + " ships, " + str(self.cargo) + " cargo"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.ships == other.ships and self.cargo == other.cargo

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.ships >= other.ships and self.cargo >= other.cargo

    def __gt__(self, other):
        return self.ships > other.ships and self.cargo > other.cargo

    def __le__(self, other):
        return self.ships <= other.ships and self.cargo <= other.cargo

    def __lt__(self, other):
        return self.ships < other.ships and self.cargo < other.cargo


class WorldShips:
    """
    A class that represents a number of ships on a world. Either Iships or Pships.
    """

    def __init__(self, ships: int, location=None):
        self.location = location
        self.ships = ships if ships <= 255 else 255

    def __str__(self):
        return str(self.ships) + " ships"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.ships == other.ships

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.ships >= other.ships

    def __gt__(self, other):
        return self.ships > other.ships

    def __le__(self, other):
        return self.ships <= other.ships

    def __lt__(self, other):
        return self.ships < other.ships


class IShips(WorldShips):
    """
    A class that represents a number of ships on a world. Iships.
    """

    def __init__(self, ships: int):
        super().__init__(ships)

    def increase(self, ships: int):
        self.ships += ships
        self.ships = self.ships if self.ships <= 255 else 255

    def decrease(self, ships: int):
        self.ships -= ships
        self.ships = self.ships if self.ships >= 0 else 0


class PShips(WorldShips):
    """
    A class that represents a number of ships on a world. Pships.
    """

    def __init__(self, ships: int):
        super().__init__(ships)

    def increase(self, ships: int):
        self.ships += ships
        self.ships = self.ships if self.ships <= 255 else 255

    def decrease(self, ships: int):
        self.ships -= ships
        self.ships = self.ships if self.ships >= 0 else 0


class Industries:
    """
    A class that represents a number of industries on a world.
    """

    def __init__(self, industries: int, location=None):
        self.industries = industries if industries <= 255 else 255
        self.location = location

    def __str__(self):
        return str(self.industries) + " industries"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.industries == other.industries and self.location == other.location

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.industries >= other.industries

    def __gt__(self, other):
        return self.industries > other.industries

    def __le__(self, other):
        return self.industries <= other.industries

    def __lt__(self, other):
        return self.industries < other.industries

    def increase(self, industries: int):
        self.industries += industries
        self.industries = self.industries if self.industries <= 255 else 255

    def decrease(self, industries: int):
        self.industries -= industries
        self.industries = self.industries if self.industries >= 0 else 0


class Mines:
    """
    A class that represents a number of mines on a world.
    """

    def __init__(self, mines: int, location=None):
        self.mines = mines if mines <= 255 else 255
        self.location = location

    def __str__(self):
        return str(self.mines) + " mines"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.mines == other.mines and self.location == other.location

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.mines >= other.mines

    def __gt__(self, other):
        return self.mines > other.mines

    def __le__(self, other):
        return self.mines <= other.mines

    def __lt__(self, other):
        return self.mines < other.mines

    def increase(self, mines: int):
        self.mines += mines
        self.mines = self.mines if self.mines <= 255 else 255

    def decrease(self, mines: int):
        self.mines -= mines
        self.mines = self.mines if self.mines >= 0 else 0


@unique
class PopulationType(IntEnum):
    """
    A enum that tells what type of population a world has: normal, convert, robot, or none.
    """
    Normal = 0
    Convert = 1
    Robot = 2


class Population:
    """
    A class that represents a number of population on a world.
    """

    def __init__(self, population: int, location=None, population_type: PopulationType = PopulationType.Normal):
        self.population = [0, 0, 0]
        self.population[population_type] = population if population <= 255 else 255
        self.location = location
        self.population_type: PopulationType = population_type

    def __str__(self):
        return str([str(self.population[PopulationType.Normal]), str(self.population[PopulationType.Convert]),
                    str(self.population[PopulationType.Robot])]) + " population"

    def converts(self):
        return self.population[PopulationType.Convert]

    def robots(self):
        return self.population[PopulationType.Robot]

    def normal(self):
        return self.population[PopulationType.Normal]

    def effective(self, fleets: []):
        suppression_ships_in_orbit = 0
        for fleet in fleets:
            if not fleet.at_peace and fleet.location == self.location and fleet.owner != self.location.owner:
                suppression_ships_in_orbit += fleet.ships.effective_firepower()
        return self.population[PopulationType.Normal] - suppression_ships_in_orbit \
            if self.population[PopulationType.Normal] - suppression_ships_in_orbit >= 0 else 0


@unique
class OrderType(IntEnum):
    LOAD = 1
    UNLOAD = 2
    BUILD = 3
    MOVE = 4
    FIRE = 5
    GIFT = 6
    ALLIE = 7
    HOSTILE = 8
    NEUTRAL = 9
    CAPTURE = 10
    SCRAP = 11
    MOVE_ARTIFACT = 12
    MOVE_MUSEUM = 13
    MOVE_MINE = 14
    MOVE_INDUSTRY = 15


class Order:
    oid: int = 0
    orders = {OrderType.LOAD: [], OrderType.UNLOAD: [], OrderType.BUILD: [], OrderType.MOVE: [], OrderType.FIRE: [],
              OrderType.GIFT: [], OrderType.ALLIE: [], OrderType.HOSTILE: [], OrderType.NEUTRAL: [],
              OrderType.CAPTURE: [], OrderType.SCRAP: [], OrderType.MOVE_ARTIFACT: [], OrderType.MOVE_MUSEUM: [],
              OrderType.MOVE_MINE: [], OrderType.MOVE_INDUSTRY: []}

    @classmethod
    def _generate_next_oid(cls):
        cls.oid += 1
        return cls.oid

    def __init__(self, owner, name: str, command: str):
        self.oid = Order._generate_next_oid()
        self.owner = owner
        self.name = name
        self.command = command
        self.type = "Unknown"
        Order.orders[self.type].append(self)

    def __str__(self):
        return self.name + " (" + str(self.oid) + ")" + " - " + self.command

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.oid == other.oid


class ClassType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def pship_cost(self):
        return 10

    def iship_cost(self):
        return 20

    def pship_effectiveness(self):
        return 2

    def ship_effectiveness(self):
        return 1

    def ship_effective_cargo(self):
        return 1


class Merchant(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Merchant", "blue")

    def pship_cost(self):
        return 8

    def iship_cost(self):
        return 16

    def pship_effectiveness(self):
        return 3

    def ship_effective_cargo(self):
        return 2


class Pirate(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Pirate", "red")

    def pship_cost(self):
        return 12

    def iship_cost(self):
        return 24

    def pship_effectiveness(self):
        return 1

    def ship_effectiveness(self):
        return 2

    def ship_effective_cargo(self):
        return 1


class ArtifactCollector(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Artifact Collector", "green")


class Berserker(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Berserker", "yellow")


class Apostle(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Apostle", "purple")


class EmpireBuilder(ClassType):
    def __init__(self):
        ClassType.__init__(self, "Empire Builder", "black")


class Player:
    players = []

    def __init__(self, name, class_type: ClassType):
        self.name = name
        self.class_type = class_type
        self.home_world = None
        self.ambush = True
        self.artifacts = []
        self.martyrs = []
        self.jihad = False
        self.jihad_enemy = None
        self.jihad_turns = 0
        self.score = 0
        Player.players.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def pship_effectiveness(self) -> int:
        return self.class_type.pship_effectiveness()

    def calculate_fleet_suppression(self, world, fleets):
        suppression = 0
        for fleet in fleets:
            if fleet.location == world and fleet.owner != self:
                suppression += fleet.ship_effectiveness() * fleet.ships
        return suppression

    def iship_effectiveness(self):
        return self.class_type.ship_effectiveness()


Neutral_Player = Player("Neutral", EmpireBuilder())


class CharacterType:
    """
    Character types are the different types of players that can be in the game. Each character type has a different
    starting fleet, and a different set of abilities.
    """

    def __init__(self, name, description, greatest_treasure):
        self.name = name
        self.description = description
        # The greatest treasure is the artifact that the player
        # will be most likely to collect in the game.
        self.greatest_treasure = greatest_treasure

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Piece:
    """
    A piece is a fleet, world, or artifact. It has a name, location, and owner.
    The pid is a unique identifier for each piece and will be used to create a unique name for each piece.
    """
    next_pid: int = 100

    @classmethod
    def _generate_next_pid(cls):
        cls.next_pid += 1
        return cls.next_pid

    def __init__(self, piece_type: str = 'X', location=None, owner=None):
        self.piece_type = piece_type  # fleet name = "F", world name = "W", or artifact name = "A"
        self.pid = Piece._generate_next_pid()
        self.location = location  # world or fleet location
        self.owner = owner

    def __str__(self):
        return self.piece_type + str(self.pid)

    def __repr__(self):
        return '[' + self.piece_type + str(self.pid) + ']'

    def __eq__(self, other):
        return self.piece_type == other.piece_type and self.pid == other.pid and \
            self.location == other.location and self.owner == other.owner


class World(Piece):
    """
    The location of the world is the world itself. NB: this is different from the location of a fleet, which is a world.
    """
    worlds = []

    def __init__(self, owner, neighbors: [], population: int, pships: int, industry: int,
                 iships: int, metal: int, mines: int):
        super().__init__("W", owner=owner)
        self.neighbors = neighbors
        self.population = population
        self.PSHIPS = pships
        self.industry = industry
        self.iships = iships
        self.metal = metal
        self.mines = mines
        self.artifacts = []
        self.ambush = True
        # location of world is the world itself NB: can't do this in Piece constructor because
        # World is not defined yet
        self.location = self
        World.worlds.append(self)
        self.next_turn = {}

    def calculate_effective_population(self, fleets: []):
        """
        :param fleets:
        :return: effective population of world, including fleets with ships at this world and not "at peace"
        """
        current_effective_population = self.population + self.PSHIPS * self.owner.pship_effectiveness()
        fleet_suppression = self.owner.calculate_fleet_suppression(self, fleets)
        return max(current_effective_population - fleet_suppression, 0)

    def calculate_effective_industry(self, fleets: []):
        """

        :param fleets:
        :return: effective industry of world, including fleets with ships at this world and not "at peace"
        """
        current_effective_industry = self.industry + self.iships * self.owner.iship_effectiveness()
        fleet_suppression = calculate_fleet_suppression(self, fleets)
        return max(current_effective_industry - fleet_suppression, 0)

    def is_neighbor(self, world):
        return world in self.neighbors

    def is_within_range(self, world, hops: int, max_hops: int = 3):
        """
        This is a recursive function that goes through the neighbors of the world and checks if the world is within
        hops of self. If hops is 0, then the world must be self. If hops is 1, then the world must be in the neighbor
        of self.
        :param world:
        :param hops:
        :param max_hops:
        :return: true if world is within hops of self
        """
        if hops == 0:
            return self == world
        elif hops == 1:
            return self.is_neighbor(world)
        elif hops > max_hops:
            return False
        else:
            for neighbor in self.neighbors:
                if neighbor.is_within_range(world, hops - 1):
                    return True
            return False

    def update_industry(self, fleets, artifacts):
        """
        Update the industry of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["industry"] = self.industry * 1.10

        self.industry = self.calculate_effective_industry(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.industry += artifact.owner.artifact_effectiveness()

    def update_metal(self, fleets, artifacts):
        """
        Update the metal of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["metal"] = self.metal * 1.10

        self.metal += self.calculate_metal_production(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.metal += artifact.owner.artifact_effectiveness()

    def update_mines(self, fleets, artifacts):
        """
        Update the mines of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["mines"] = self.mines * 1.10

        self.mines = self.calculate_effective_mines(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.mines += artifact.owner.artifact_effectiveness()

    def update_pships(self, fleets, artifacts):
        """
        Update the pships of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["pships"] = self.pships * 1.10

        self.pships = self.calculate_effective_pships(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.pships += artifact.owner.artifact_effectiveness()

    def update_iships(self, fleets, artifacts):
        """
        Update the iships of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["iships"] = self.calculate_effective_iships(fleets)

        self.iships = self.calculate_effective_iships(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.iships += artifact.owner.artifact_effectiveness()

    def update_ambush(self, fleets, artifacts):
        """
        Update the ambush of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["ambush"] = self.ambush * 1.10

        self.ambush = self.calculate_effective_ambush(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.ambush += artifact.owner.artifact_effectiveness()

    def update_artifacts(self, fleets, artifacts):
        """
        Update the artifacts of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["artifacts"] = self.artifacts * 1.10

        self.artifacts = self.calculate_effective_artifacts(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.artifacts += artifact.owner.artifact_effectiveness()

    def update_population(self, fleets, artifacts):
        """
        Update the population of the world
        :param fleets:
        :param artifacts:
        :return:
        """
        self.next_turn["population"] = self.population * 1.10

        self.population = self.calculate_effective_population(fleets)
        for artifact in artifacts:
            if artifact.location == self:
                self.population += artifact.owner.artifact_effectiveness()


class Fleet(Piece):
    fleets = []

    def __init__(self, location: World, owner: Player, ships: int, cargo: int, pbb: bool, artifacts: []):
        super().__init__("F", location, owner)
        self.ships = ships
        self.cargo = cargo
        self.ppb = pbb
        self.artifacts = artifacts
        self.at_peace = False
        Fleet.fleets.append(self)

    def move_to(self, world):  # move fleet to world
        if world in self.location.neighbors:
            self.location = world


class Artifact(Piece):
    artifacts = []

    def __init__(self, location, owner, primary_name, secondary_name):
        super().__init__("A", location, owner)
        self.primary_name = primary_name
        self.secondary_name = secondary_name
        Artifact.artifacts.append(self)


def calculate_fleet_suppression(world, fleets):
    fleet_suppression = 0
    for fleet in fleets:
        if fleet.location == world and not fleet.at_peace and fleet.owner != world.owner:
            fleet_suppression += fleet.ships * fleet.class_type.ship_effectiveness()
        elif fleet.location == world and fleet.owner == world.owner:
            fleet_suppression -= fleet.ships * fleet.class_type.ship_effectiveness()

    return fleet_suppression


"""
FnnnTqqqFmmm = transfers qqq ships from fleet nnn to fleet mmm
FnnnTqqqI or FnnnTqqqP = transfers qqq ships from fleet nnn to ISHIPS or PSHIPS
InnnTqqqFmmm = transfers qqq ships from ISHIPS at world nnn to fleet mmm
PnnnTqqqFmmm = transfers qqq ships from PSHIPS at world nnn to fleet mmm
PnnnTqqqI or InnnTqqqP = transfers qqq ships from PSHIPS to ISHIPS or vice versa
"""

transfer_n_ships_from_fleet_to_fleet = re.compile("F\d+T\d+F\d+")
transfer_n_ships_from_fleet_to_iships = re.compile("F\d+T\d+I")
transfer_n_ships_from_fleet_to_PSHIPS = re.compile("F\d+T\d+P")
transfer_n_iships_from_world_to_fleet = re.compile("I\d+T\d+F\d+")
transfer_n_PSHIPS_from_world_to_fleet = re.compile("P\d+T\d+F\d+")
transfer_n_PSHIPS_from_world_to_iships = re.compile("P\d+T\d+I")
transfer_n_iships_from_world_to_PSHIPS = re.compile("I\d+T\d+P")

transfer_orders = [transfer_n_ships_from_fleet_to_fleet, transfer_n_ships_from_fleet_to_iships,
                   transfer_n_ships_from_fleet_to_PSHIPS, transfer_n_iships_from_world_to_fleet,
                   transfer_n_PSHIPS_from_world_to_fleet, transfer_n_PSHIPS_from_world_to_iships,
                   transfer_n_iships_from_world_to_PSHIPS]

"""
create an html/jinja2 template for inputting transfer orders
<html>
    <head>
        <title>Transfer Orders</title>
    </head>
    <body>
        <form action="/transfer_orders" method="post">
            <input type="text" name="transfer_orders" />
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>

"""


def transfer_ships_from_fleet_to_fleet(order: str, fleets: []) -> bool:
    """
    Transfers ships from one fleet to another fleet (not a world)
    :param order:
    :param fleets:
    :return:
    """
    fleet1 = int(order[1:4])
    n = int(order[5:8])
    fleet2 = int(order[9:12])
    if fleets[fleet1].ships < n:
        logging.warning("Not enough ships in fleet {} to transfer {} ships to fleet {}".format(fleet1, n, fleet2))
        return False

    fleets[fleet1].ships -= n
    fleets[fleet2].ships += n

    return True


def transfer_ships_from_fleet_to_iships(order: str, fleets: [], worlds: []) -> bool:
    """
    Transfers ships from a fleet to ISHIPS at a world
    :param order:
    :param fleets:
    :param worlds:
    :return:
    """
    fleet = int(order[1:4])
    n = int(order[5:8])
    if fleets[fleet].ships < n:
        logging.warning("Not enough ships in fleet {} to transfer {} ships to iships".format(fleet, n))
        return False
    world = int(order[9:12])
    fleets[fleet].ships -= n
    worlds[world].iships += n

    return True


def transfer_ships_from_fleet_to_pships(order: str, fleets: [], worlds: []) -> bool:
    """
    Transfers ships from a fleet to PSHIPS at a world
    :param order:
    :param fleets:
    :param worlds:
    :return:
    """
    fleet = int(order[1:4])
    n = int(order[5:8])
    if fleets[fleet].ships < n:
        logging.warning("Not enough ships in fleet {} to transfer {} ships to PSHIPS".format(fleet, n))
        return False

    world = int(order[9:12])
    fleets[fleet].ships -= n
    worlds[world].PSHIPS += n

    return True


def transfer_iships_from_world_to_fleet(order, fleets, worlds) -> bool:
    """"
    Transfers ISHIPS from a world to a fleet
    :param order:
    :param fleets:
    :param worlds:
    :return:
    """
    world = int(order[1:4])
    n = int(order[5:8])
    if worlds[world].iships < n:
        logging.warning("Not enough iships at world {} to transfer {} ships to fleet".format(world, n))
        return False

    fleet = int(order[9:12])
    fleets[fleet].ships += n
    worlds[world].iships -= n

    return True


"""
WnnnBqqqI = build qqq ISHIPS at world nnn. (This order is actually not necessary as all industry not otherwise ordered 
will automatically build ISHIPS.)
WnnnBqqqP = build qqq PSHIPS at world nnn
WnnnBqqqFmmm = build qqq ships and attach them to fleet mmm (fleet mmm must be at world nnn)
WnnnIqqqI = build qqq new industry (needs 5 metal and 5 industry for each one)
WnnnIqqqL = increase the population limit of world nnn by qqq (uses 5 industry and 5 metal).
WnnnBqqqR = build robots with qqq industry (makes twice that many robots). This order may only be given if the world is 
already populated with robots.
"""

build_n_iships_at_world = re.compile("W\d+B\d+I")
build_n_PSHIPS_at_world = re.compile("W\d+B\d+P")
build_n_ships_and_attach_to_fleet = re.compile("W\d+B\d+F\d+")
build_n_industry_at_world = re.compile("W\d+I\d+I")
build_n_population_limit_at_world = re.compile("W\d+I\d+L")
build_n_robots_at_world = re.compile("W\d+B\d+R")

build_orders = [build_n_iships_at_world, build_n_PSHIPS_at_world, build_n_ships_and_attach_to_fleet,
                build_n_industry_at_world, build_n_population_limit_at_world, build_n_robots_at_world]


def effective_industry(world, fleets) -> int:
    """
    Returns the effective industry of a world or fleet
    :param world:
    :param fleets:
    :return:
    """
    if world.fleet is None:
        return world.industry
    else:
        hostile_ships_in_orbit = 0
        for fleet in fleets:
            if fleet.owner != world.owner and fleet.world == world.fleet and fleet.at_peace is False:
                hostile_ships_in_orbit += fleet.ships
        return (world.industry + world.owner.effecitve_iships * world.iships) - hostile_ships_in_orbit


def effective_population(world, fleets) -> int:
    """
    Returns the effective population of a world
    :param world:
    :param fleets:
    :return:
    """
    if world.fleet is None:
        return world.population
    else:
        hostile_ships_in_orbit = 0
        for fleet in fleets:
            if fleet.owner != world.owner and fleet.world == world.fleet and fleet.at_peace is False:
                hostile_ships_in_orbit += fleet.ships
        return (world.population + world.owner.effecitve_PSHIPS * world.PSHIPS) - hostile_ships_in_orbit


def build_iships_at_world(order: str, worlds: [], fleets: []) -> bool:
    """
    Builds ISHIPS at a world
    :param fleets:
    :param order:
    :param worlds:
    :return:
    """
    world = int(order[1:4])
    n = int(order[5:8])
    if effective_industry(worlds[world], fleets) < n:
        logging.warning("Not enough industry at world {} to build {} iships".format(world, n))
        return False

    if worlds[world].metal < n:
        logging.warning("Not enough metal at world {} to build {} iships".format(world, n))
        return False

    if effective_population(worlds[world], fleets) < n:
        logging.warning("Not enough population {} to build {} iships".format(world, n))
        return False

    worlds[world].iships += n
    worlds[world].industry -= n

    return True


"""
PnnnMqqqWmmm = moves qqq people or robots from world nnn to world mmm. Uses qqq industry and metal.
CnnnMqqqWmmm = moves qqq converts from world nnn to world mmm. Uses qqq industry and metal.
"""

migrate_n_people_from_world_to_world = re.compile("P\d+M\d+W\d+")
migrate_n_converts_from_world_to_world = re.compile("C\d+M\d+W\d+")

migrate_orders = [migrate_n_people_from_world_to_world, migrate_n_converts_from_world_to_world]


def migrate_n_people_from_world_to_world(order: str, worlds: [], fleets: []) -> bool:
    """
    Migrates people from one world to another
    :param order:
    :param worlds:
    :param fleets:
    :return:
    """
    world = int(order[1:4])
    n = int(order[5:8])
    if effective_population(worlds[world], fleets) < n:
        logging.warning("Not enough population at world {} to migrate {} people".format(world, n))
        return False

    if effective_industry(worlds[world], fleets) < n:
        logging.warning("Not enough industry at world {} to migrate {} people".format(world, n))
        return False

    if effective_population(worlds[world], fleets) < n:
        logging.warning("Not enough population at world {} to migrate {} people".format(world, n))
        return False

    world2 = int(order[9:12])
    worlds[world].population -= n
    worlds[world2].population += n

    return True


def migrate_n_converts_from_world_to_world(order: str, worlds: [], fleets: []) -> bool:
    """
    Migrates converts from one world to another
    :param order:
    :param worlds:
    :param fleets:
    :return:
    """
    world = int(order[1:4])
    n = int(order[5:8])
    if effective_population(worlds[world], fleets) < n:
        logging.warning("Not enough population at world {} to migrate {} converts".format(world, n))
        return False

    if effective_industry(worlds[world], fleets) < n:
        logging.warning("Not enough industry at world {} to migrate {} converts".format(world, n))
        return False

    if effective_population(worlds[world], fleets) < n:
        logging.warning("Not enough population at world {} to migrate {} converts".format(world, n))
        return False

    world2 = int(order[9:12])
    worlds[world].population -= n
    worlds[world2].population += n

    return True


"""
FnnnWmmm = move fleet nnn to world mmm.
FnnnWmmmWooo = move fleet nnn through world mmm to world ooo.
FnnnWmmmWoooWppp = move fleet nnn through worlds nnn and ooo to world ppp
"""

move_fleet_to_world = re.compile("F\d+W\d+")
move_fleet_through_worlds = re.compile("F\d+W\d+W\d+")
move_fleet_through_worlds = re.compile("F\d+W\d+W\d+W\d+")

fleet_move_orders = [move_fleet_to_world, move_fleet_through_worlds, move_fleet_through_worlds]


def move_fleet_to_world(order: str, worlds: [], fleets: []) -> bool:
    """
    Moves a fleet to a world
    :param order:
    :param worlds:
    :param fleets:
    :return:
    """
    fleet = int(order[1:4])
    world = int(order[5:8])
    if fleets[fleet].location == world:
        logging.warning("Fleet {} is already at world {}".format(fleet, world))
        return False

    if fleets[fleet].location != worlds[world].fleet:
        logging.warning("Fleet {} is not orbiting world {}".format(fleet, world))
        return False

    if fleets[fleet].location != worlds[world].fleet:
        logging.warning("Fleet {} is not orbiting world {}".format(fleet, world))
        return False

    if world not in world:
        logging.warning("World {} does not exist".format(world))
        return False

    fleets[fleet].world = world

    return True


"""
FnnnPmmm = uses 1 ship from fleet nnn to probe world mmm (happens before movement and fleet nnn can then move that turn)
InnnPmmm = uses an ISHIP at world nnn to probe world mmm
PnnnPmmm = uses a PSHIP at world nnn to probe world mmm
"""

probe_world_with_fleet = re.compile("F\d+P\d+")
probe_world_with_iship = re.compile("I\d+P\d+")
probe_world_with_pship = re.compile("P\d+P\d+")

probe_orders = [probe_world_with_fleet, probe_world_with_iship, probe_world_with_pship]

"""
FnnnU = unloads all the metal from fleet nnn onto the world where fleet nnn starts that turn.
FnnnUqqq = unload only qqq of the metal fleet nnn is carrying.
FnnnJ = jettisons (destroys) all the cargo that Fnnn is carrying.
FnnnJqqq = jettisons qqq cargo from fleet nnn.
FnnnN = unloads all the metal that fleet nnn is carrying as consumer goods.
FnnnNqqq = unload qqq metal as consumer goods
FnnnL = fleet nnn will pick up as much metal as it can carry.
FnnnLqqq = fleet nnn will pick up qqq metal.
"""
unload_all_metal_from_fleet = re.compile("F\d+U")
unload_n_metal_from_fleet = re.compile("F\d+U\d+")
jettison_all_cargo_from_fleet = re.compile("F\d+J")
jettison_n_cargo_from_fleet = re.compile("F\d+J\d+")
unload_all_metal_as_consumer_goods = re.compile("F\d+N")
unload_n_metal_as_consumer_goods = re.compile("F\d+N\d+")
fleet_loads_metal = re.compile("F\d+L")
fleet_loads_n_metal = re.compile("F\d+L\d+")

unload_orders = [unload_all_metal_from_fleet, unload_n_metal_from_fleet, jettison_all_cargo_from_fleet,
                 jettison_n_cargo_from_fleet, unload_all_metal_as_consumer_goods, unload_n_metal_as_consumer_goods,
                 fleet_loads_metal, fleet_loads_n_metal]

"""
VnnnFmmm = attach artifact nnn to fleet mmm. (The fleet must either be owned by you, or by an artifact collector. 
The artifact must be on the world the fleet is currently located or, if Fmmm is owned by a collector, it can also be 
on a fleet at the world where Fmmm is located.)
VnnnW = drop the artifact nnn from the fleet carrying it, wherever it may be at the moment. Note that only one order 
per turn can be given for each artifact.
"""
artifact_attach_to_fleet = re.compile("V\d+F\d+")
artifact_drop_from_fleet = re.compile("V\d+W")

artifact_orders = [artifact_attach_to_fleet, artifact_drop_from_fleet]

"""
FnnnAFmmm = fleet nnn fires at fleet mmm.
InnnAFmmm = ISHIPS at world nnn fire at fleet mmm.
PnnnAFmmm = PSHIPS at world mmm fire at fleet mmm.
FnnnAI = fleet nnn fires at ISHIPS, and then industry.
FnnnAP = fleet nnn fires at PSHIPS, and then population.
FnnnAH = fleet nnn fires at ISHIPS and PSHIPS, then tries to make the world go neutral.
InnnAC = ISHIPS at world nnn fire at converts.
PnnnAC = PSHIPS at world nnn fire at converts.
"""
fire_at_fleet = re.compile("F\d+A[FIPHC]")
iships_fire_at_fleet = re.compile("I\d+A[FIPHC]")
PSHIPS_fire_at_fleet = re.compile("P\d+A[FIPHC]")
fire_at_iships_then_industry = re.compile("F\d+AI")
fire_at_PSHIPS_then_population = re.compile("F\d+AP")
fire_at_iships_and_PSHIPS_then_try_to_make_world_neutral = re.compile("F\d+AH")
iships_fire_at_converts = re.compile("I\d+AC")
PSHIPS_fire_at_converts = re.compile("P\d+AC")

fire_orders = [fire_at_fleet, iships_fire_at_fleet, PSHIPS_fire_at_fleet, fire_at_iships_then_industry,
               fire_at_PSHIPS_then_population, fire_at_iships_and_PSHIPS_then_try_to_make_world_neutral,
               iships_fire_at_converts, PSHIPS_fire_at_converts]

"""
FnnnCFmmm = fleet nnn fires at fleet mmm only if the owner of fleet mmm fires at you this turn at this world
"""
conditional_fleet_fire = re.compile("F\d+CF\d+")

"""
Z = don't ambush anyone this turn anywhere (must be given every turn if you want it to stay in effect).
Znnn = don't ambush anyone this turn at world nnn.
"""
ambush_no_one = re.compile("Z$")

"""
A=xxxxxx = you are declaring player xxxxxx your ally.
N=xxxxxx = you are declaring player xxxxxx "not" your ally.
L=xxxxxx = you are declaring player xxxxxx a loader (he is allowed to pick up metal).
X=xxxxxx = you are declaring player xxxxxx "not" a loader.
J=xxxxxx = you are an Apostle declaring a jihad against player xxxxxx.
FnnnG=xxxxxx = you are giving fleet nnn to player xxxxxx.
WnnnG=xxxxxx = you are giving world nnn to player xxxxxx.
"""
declare_ally = re.compile("A=\w+")
declare_not_ally = re.compile("N=\w+")
declare_loader = re.compile("L=\w+")
declare_not_loader = re.compile("X=\w+")
declare_jihad = re.compile("J=\w+")
give_fleet = re.compile("F\d+G=\w+")
give_world = re.compile("W\d+G=\w+")
diplomacy_orders = [declare_ally, declare_not_ally, declare_loader, declare_not_loader, declare_jihad, give_fleet,
                    give_world]

"""
WnnnX = you are plundering world nnn.
FnnnQ = you are putting fleet nnn "at peace".
FnnnX = you are putting fleet nnn "not at peace".
FnnnB = you are building a planet buster bomb with fleet nnn.
FnnnD = fleet nnn is dropping a PBB on the world below.
FnnnRqqq = you are a berserker converting qqq ships from fleet nnn into robots (1 ship = 2 robots) and they are landing 
on the world below. (Happens after the firing for that turn is finished.)
"""

plunder_world = re.compile("W\d+X")
fleet_at_peace = re.compile("F\d+Q")
fleet_not_at_peace = re.compile("F\d+X")
build_pbb = re.compile("F\d+B")
drop_pbb = re.compile("F\d+D")
convert_ships_to_robots = re.compile("F\d+R\d+")

misc_orders = [plunder_world, fleet_at_peace, fleet_not_at_peace, build_pbb, drop_pbb, convert_ships_to_robots]

build_iships_at_world = re.compile(r'I(\d+)B(\d+)')
build_PSHIPS_at_world = re.compile(r'P(\d+)B(\d+)')


def process_orders(worlds, fleets, artifacts):
    """
    Go through all orders for each game piece and process them.
    :param worlds:
    :param fleets:
    :param artifacts:
    :return:
    """
    for world in worlds:
        world.process_orders(worlds, fleets)
    for fleet in fleets:
        fleet.process_orders(worlds, fleets)
    for artifact in artifacts:
        artifact.process_orders(worlds, fleets)


def resolve_conflicts(worlds, fleets, artifacts):
    """
    Resolve all conflicts between fleets and worlds.
    :param worlds:
    :param fleets:
    :param artifacts:
    :return:
    """
    for world in worlds:
        world.resolve_conflicts(worlds, fleets, artifacts)
    for fleet in fleets:
        fleet.resolve_conflicts(worlds, fleets, artifacts)
    for artifact in artifacts:
        artifact.resolve_conflicts(worlds, fleets, artifacts)


def process_turn(worlds, fleets, artifacts):
    """
    Process all orders and then resolve all conflicts.
    :param worlds:
    :param fleets:
    :param artifacts:
    :return:
    """
    process_orders(worlds, fleets, artifacts)
    resolve_conflicts(worlds, fleets, artifacts)


def update_population(worlds, fleets, artifacts):
    """
    Update the population of all worlds.
    :param worlds:
    :param fleets:
    :param artifacts:
    :return:
    """
    for world in worlds:
        world.update_population(worlds, fleets, artifacts)


def process_orders(worlds, fleets, artifacts):
    """
    Go through all orders for each game piece and process them.
    :param worlds:
    :param fleets:
    :param artifacts:
    :return:
    """
    for world in worlds:
        world.process_orders(worlds, fleets)
    for fleet in fleets:
        fleet.process_orders(worlds, fleets)
    for artifact in artifacts:
        artifact.process_orders(worlds, fleets)


"""
Define some html/jinja2 templates for the game.
Need to define a template for the game board, 
a template for the game status,
a template for the game history.
Need to define a template for player order entry
Need to define a template for player turn results
"""

"""
<html>
<head>
<title>Game Board</title>
</head>
<body>
<h1>Game Board</h1>
<table>
<tr>
<td>World</td>
<td>Owner</td>
<td>Industry</td>
<td>Population</td>
<td>Ships</td>
<td>Artifacts</td>
</tr>
{% for world in worlds %}
<tr>
<td>{{ world.name }}</td>
<td>{{ world.owner }}</td>
<td>{{ world.industry }}</td>
<td>{{ world.population }}</td>
<td>{{ world.ships }}</td>
<td>{{ world.artifacts }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

"""
<html>
<head>
<title>Game Status</title>
</head>
<body>
<h1>Game Status</h1>
<table>
<tr>
<td>Player</td>
<td>Score</td>
<td>Industry</td>
<td>Population</td>
<td>Ships</td>
<td>Artifacts</td>
</tr>
{% for player in players %}
<tr>
<td>{{ player.name }}</td>
<td>{{ player.score }}</td>
<td>{{ player.industry }}</td>
<td>{{ player.population }}</td>
<td>{{ player.ships }}</td>
<td>{{ player.artifacts }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>

"""

"""
<html>
<head>
<title>Game History</title>
</head>
<body>
<h1>Game History</h1>
<table>
<tr>
<td>Turn</td>
<td>Player</td>
<td>Order</td>
</tr>
{% for turn in turns %}
<tr>
<td>{{ turn.turn }}</td>
<td>{{ turn.player }}</td>
<td>{{ turn.order }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>

"""

"""
<html>
<head>
<title>Player Order Entry</title>
</head>
<body>
<h1>Player Order Entry</h1>
<form action="/player_order_entry" method="post">
<table>
<tr>
<td>World</td>
<td>Order</td>
</tr>
{% for world in worlds %}
<tr>
<td>{{ world.name }}</td>
<td><input type="text" name="{{ world.name }}" /></td>
</tr>
{% endfor %}
</table>
<input type="submit" value="Submit" />
</form>
</body>
</html>

"""

"""
<html>
<head>
<title>Player Turn Results</title>
</head>
<body>
<h1>Player Turn Results</h1>
<table>
<tr>
<td>World</td>
<td>Order</td>
</tr>
{% for world in worlds %}
<tr>
<td>{{ world.name }}</td>
<td>{{ world.order }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>

"""
