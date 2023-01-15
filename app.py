import random
import uuid
from functools import reduce

from flask import Flask

app = Flask(__name__)

# Game Main Objects
# - Players
# - Worlds
# - Fleets or Keys

# Each player starts with a home world and 5 fleets. The home world starts with Population 50, max population 100,
# Industry 30, Metal 30 and Mines 2, I-Ships = 1 and P-Ships = 1

# There are 6 Player types:
# - The Empire Builder
# - The Merchant
# - The Pirate
# - The Artifact Collector
# - The Berserker
# - The Apostle

# A Fleet has the following attributes:
# - id : oid
# - owner : Player
# - location: World
# - ships: [Ship]
# - cargo: [Resource]
# - destination: World
# - Artifacts: [Artifact]
# - PlanetBusterBomb: int

# A Ship has the following attributes:
# - fleet: Fleet
# - cargo: [Resource]
# - fired: bool

# A World has the following attributes:
# - id : oid
# - owner : Player
# - location: World
# - connections: [World]
# - i-ships: int
# - p-ships: int
# - population: int
# - max-population: int
# - industry: int
# - metal: int
# - mines: int
# - artifacts: [Artifact]

# A Resource has the following attributes:
# - type: str
# - amount: int

# An Artifact has the following attributes:
# - type: str
# - owner: Player
# - location: World or Fleet
# - points: int

# A Player has the following attributes:
# - id : oid
# - name: str
# - type: str
# - home-world: World
# - fleets: [Fleet]
# - artifacts: [Artifact]
# - points: int
# - allies: {Player: 'allied' or 'neutral' or 'hostile'}

"""
BUILDING. You may build at any world where you have at least 1 industry, 1 population, and 1 metal. The amount you can
build is equal to the SMALLEST of these three numbers (and the metal are used up when you build).
If there is an enemy fleet "not at peace" at your world, for each shot he has which outnumbers your defending ships, 
one industry will not build (your population is hiding inside bomb shelters). This is automatic, and is shown on your
printout. If you have 30 industry, but only 25 are allowed to build because of enemy presence (or any other reason), 
your industry will be listed on your printout as 30/25. For this purpose only, I_SHIPS are counted as double. That is, 
if you have 4 I_SHIPS at the world, and the enemy has 10 ships, only 2 of your industry will be unable to build because
of enemy presence. Also any ships present belonging to a player who has declared you "ally" will be counted as defending
your industry.
"METAL" on your printout is how many raw materials you have stockpiled on that world. This is how many you can use to 
build this turn. You cannot use the ones which are going to be produced, nor can you use the ones that are being 
unloaded.
"MINES" tells you how many metal are going to be produced for NEXT turn. Note that all building must be done at the 
world where the industry is. You cannot build ships onto a fleet that is located somewhere else. Building comes before 
loading, movement, or firing. You cannot load the metal that is going to be used by the industry this turn. You can 
build onto a fleet that is moving away or firing, and the new ships count in the number of shots you get to fire.

Each industry can build 1 ship. Each 5 industry (4 for empire builders) can build 1 more industry using 5 metal and 5 
population. Each 5 industry (4 for empire builders) can increase the population limit of the planet they are on by 1. 
Each industry can build 2 robots (but ONLY if the population of that world is already robots. Non-berserkers cannot 
build robots & berserkers cannot build robots at worlds populated by people.) Remember, in each case you must have 1 
population to run each industry, and you use up one metal per industry. If a world does not have enough population to 
run BOTH the industry AND produce the metal from its mines, it will alternate. Example: if a world has 5 industry and 
5 mines, but only 5 population, then one turn it will create METAL, and the next turn the industry will turn those 5 
metal into ships or whatever.

You may also use your industry to move some of your population to an adjacent world. This is the only way to increase 
population at a world other than by normal growth. One industry, using 1 metal, moves 1 population to an adjacent 
world (which must be connected to that world by a gate). When you use this option, you are building a short- run colony 
ship which expends itself by moving to the next system. This is called Migrating Population. Robots are migrated using 
the same order as normal population. If you want to migrate CONVERTS, you must specify them with a special order. If 
you migrate population, you do NOT gain control of the adjacent system or even a report on that world. All you do is 
decrease the normal population of your world, and increase of population of the neighboring world. If you migrate 
CONVERTS or ROBOTS, however, you DO get a report on the world, and you can capture the world if you meet the capture
requirements. (Assuming of course that they are YOUR converts. If you migrate someone else's converts, then HE gets 
the report on the new world.) If a berserker migrates robots to a world populated by people, he DOES get points for 
killing those people.

You can only migrate to ONE world from any given world on a single turn, and you cannot give away the world or fire 
with its P_SHIPS or I_SHIPS on the turn that you migrate. (You can migrate TO a world from all of its adjacent worlds, 
but you can only migrate FROM a world in one direction at a time.)
POPULATION. Each world has a population and a population limit. The population of an owned world will grow approximately 
10% per turn until it reaches the limit, and then it will stop growing. If the world is owned by an Apostle, the new
 population will be all converts. You cannot have more population than the population limit of the world. If you put
extra people there (by migration), they will die. (However, they will have one turn in which to build before they die.
This is an expensive way of increasing the population limit of a world whose limit is less than 5, and unless you
are a Berserker, it is the only way. Berserker robots, of course, ignore the population limits.) Robots do not
"grow". (They must be built.)

If your population is less than your MINES, you will not produce the full number of metal per turn. If you have 4 mines,
but only 3 population, you will only produce 3 metal per turn. In addition, if you have an industry at that world, and
you build something with that industry, it takes one population, so the next turn only TWO metal will be produced.
Please remember that - people often call us and ask why their world with 2 industry and 2 mines and 3 population
only produced 1 metal last turn.

If someone fires at population, or if robots are attacking a world, you will notice:

DEATHS=N

with "N" being the number of population killed that turn. Every Berserker (or Apostle on a Jihad) who killed population
at that world, that turn, will receive 2 points for each, and every non-Berserker who fired at population at that world
that turn will lose 1 point for each. Worlds which have no population will be neutral, and will not be controlled by 
anyone.

"""


def allied(player1, player2):
    if player1.allies[player2] == 'allied':
        return True
    else:
        return False


def generate_name():
    return 'Player' + str(random.randint(0, 1000000))


def generate_player_type():
    return random.choice(['Convert', 'Berserker', 'Empire Builder', 'Apostle', 'Artifact Collector', 'Merchant'])


worlds = []


def generate_home_world(player):
    world = World(player)
    world.owner = player
    player.home_world = world
    world.population = 1
    world.population_limit = 1
    world.industry = 1
    world.mines = 1
    world.metal = 1
    world.name = 'Home World'
    worlds.append(world)
    return world


class Player:
    def __init__(self, name, type):
        self.id = uuid.uuid1()
        self.name = generate_name()
        self.type = generate_player_type()
        self.home_world = generate_home_world(self)
        self.fleets = []
        self.artifacts = []
        self.points = 0
        self.allies = {}

    def ally(self, player):
        self.allies[player] = 'allied'

    def hostile(self, player):
        self.allies[player] = 'hostile'

    def neutral(self, player):
        self.allies[player] = 'neutral'


class World:
    def __init__(self, id, owner, location, connections, i_ships, p_ships, population, max_population, industry, metal,
                 mines, artifacts):
        self.id = id
        self.owner = owner
        self.location = location
        self.connections = connections
        self.i_ships = i_ships
        self.p_ships = p_ships
        self.population = population
        self.max_population = max_population
        self.industry = industry
        self.metal = metal
        self.mines = mines
        self.artifacts = artifacts

    def effective_population(self, fleets: []):
        fleet_list = [f for f in fleets if f.location == self and not allied(f.owner, self.owner)]
        total_ships = reduce(lambda x, y: x + y, [f.ships for f in fleet_list])
        effective_population = self.population - total_ships + self.p_ships * 2
        return effective_population if effective_population < 0 else 0


# TODO: implement this method
def create_worlds(num_worlds):
    worlds = []
    max_population = random.randint(1, 10)
    population = random.randint(1, 10)
    population = population if population < max_population else max_population
    i_ships = random.randint(0, 10)
    i_ships = i_ships if i_ships < population else population
    p_ships = random.randint(0, 10)
    p_ships = p_ships if p_ships < population else population
    industry = random.randint(0, 10)
    industry = industry if industry < population else population
    metal = random.randint(0, 10)
    mines = random.randint(0, 10)
    mines = mines if mines < population else population
    artifacts = ['artifact1', 'artifact2']

    for i in range(0, num_worlds):
        worlds.append(World(i, None, None, [], i_ships, p_ships, population, max_population,
                            industry, metal, mines, artifacts))
    return worlds


class Fleet:
    def __init__(self, owner, location, ships, cargo, destination, artifacts, planet_buster_bomb):
        self.owner = owner
        self.location = location
        self.ships = ships
        self.cargo = cargo
        self.destination = destination
        self.artifacts = artifacts
        self.planet_buster_bomb = planet_buster_bomb

    def move(self, destination):
        if self.location == destination:
            return "You are already at this location"
        if destination in self.location.connections:
            self.destination = destination
            return "You are moving to " + destination
        else:
            return "You cannot move to this location"

    def attack_fleet(self, fleet):
        if fleet.location == self.location:
            if fleet.owner == self.owner:
                return "You cannot attack your own fleet"
            else:
                return "You are attacking " + fleet.owner
        else:
            return "You cannot attack a fleet that is not at your location"

    def attack_world(self, world):
        if world.location == self.location:
            if world.owner == self.owner:
                return "You cannot attack your own world"
            else:
                return "You are attacking " + world.owner
        else:
            return "You cannot attack a world that is not at your location"


# CONTROL OF A WORLD. You capture a world if you are the only player there with ships that are not at peace. Of course,
# there are exceptions. You will not capture a world from a player whom you have declared an "ally". If you are a
# Pirate and you have captured an enemy fleet this turn, the computer will NOT consider you the only player there this
# turn. If the world is populated by robots, you cannot capture it unless you are a Berserker. If the world is populated
# entirely by converts, you cannot capture it until you un-convert some of the population. A fleet belonging to the
# owner of the world, or to a player who has declared the owner his ally, will prevent capture, even if the fleet is at
# peace. A world with zero population cannot be owned.
#
# Apostles can also capture a world by converting all of its population to their religion. Berserkers can also capture
# worlds by making a robot attack and destroying all the population (leaving at least one robot).
#
# If you own a world, it remains yours until some other player meets the capture requirements, or until some other
# player forces it neutral by destroying all the I-SHIPS and P-SHIPS and firing at least two more shots than are
# necessary to destroy all the home fleets. You do not have to have any ships at a world to retain control, but if
# another player shows up and you do not have any ships there, you lose the world. If you show up at an unowned world
# which already has some I-SHIPS or P-SHIPS, you will not capture that world until you destroy the home fleets.


@app.route('/empire_builder')
def empire_builder():
    return 'Empire Builder'


@app.route('/merchant')
def merchant():
    return 'Merchant'


@app.route('/pirate')
def pirate():
    return 'Pirate'


@app.route('/artifact_collector')
def artifact_collector():
    return 'Artifact Collector'


@app.route('/berserker')
def berserker():
    return 'Berserker'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
