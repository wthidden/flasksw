from flask import Flask

app = Flask(__name__)

"""

StarWeb Rules

7th edition Copyright 1976, 1977, 1978, 1981, 1988 by Flying Buffalo Inc
"Starweb" is a registered trademark of Flying Buffalo Inc and is not to be used without permission.

This game was specifically designed to be moderated/refereed by Flying Buffalo Inc, and these rules are provided only 
to assist players in games run by Flying Buffalo Inc. The right to run this game for others is reserved for Flying 
Buffalo Inc and no one else may do so without written permission from the publisher.

CONTENTS

Historical Background
Introduction
How to Play the Game (Including a brief order of events)
The Character Types
The Empire Builder
The Merchant
The Pirate
The Artifact Collector
The Berserker
The Apostle
Details on Playing the Game
Ships
Keys
Control of a World
Building
Population
Moving
Probes
Cargo
Artifacts
Firing
Ambush
Allies
Gifts
Plundering
At Peace
PBBs (Planet Buster Bombs)
Robots
Metal Production (Mines) & the Turns Owned Number
Loose Keys
Black Holes
Signs and Diplomatic Messages
The Printout
The Turn Sheet
TRANSFER SHIPS FROM PLACE TO PLACE
MAKE NEW INDUSTRY OUT OF SHIPS
BUILDING
MIGRATING POPULATION
MOVE A FLEET ONE, TWO, OR THREE WORLDS
PROBE AN ADJACENT WORLD
TRANSFER CARGO
HOOK AND UNHOOK ARTIFACTS FROM FLEETS
TO FIRE SHOTS FROM FLEETS, ISHPS, OR PSHIPS
CONDITIONAL FIRE ORDERS
AMBUSH CONTROL
ALLIANCES, JIHADS, AND GIFTS
MISCELLANEOUS
Mutually Exclusive Orders
Victory Point Totals
Miscellaneous
Appendix -- Summary of Character Types
1. HISTORICAL BACKGROUND

You are the sole ruler of a planet of beings who have just started to explore space. The first landing on your nearest 
planetary neighbor has recently stirred up tremendous excitement. The exploration team discovered definite and 
extensive evidence of an ancient civilization. One area appears to have been a large spaceport, operated by a 
self-repairing computer.

After considerable effort, your scientists manage to communicate with the computer. It is determined that the space 
port is part of a large transportation network (called "The Web") which connects 255 star systems by means of an 
almost instantaneous transfer system. (Note: it has been determined that there is rarely more than one usable world 
in a star system. Therefore, for the rest of this description, "star system", "world", and "planet" should be 
considered interchangeable words.)

Within this space port, your scientists have found five devices, called "keys", which make transportation possible. 
When attached to a fleet of your multi-purpose spaceships, a key allows the whole fleet to travel through the "gate" 
to another star system. Unfortunately, the part of the computer which contained the map of the "Web" has been removed. 
The only star systems you know of are those which are directly connected to yours. In order to find out how to get to 
the other stars, you will have to send exploration fleets through the gates. You have noted that both the keys and the 
gates are indestructible, and that the race of beings which built the system has been gone for thousands of years.

 Table of Contents

2. INTRODUCTION

Don't let the length of these rules scare you. Most of the final parts of the rules are devoted to finer points of 
strategy, which can be ignored for the time being. As a beginner, first concentrate on Section 3, "How to Play the Game"
, and Section 4, "The Character Types". Also, please don't be intimidated by all the codes which must be given in order 
to explain your moves to the computer. These are merely abbreviations to make it easier and quicker to explain EXACTLY 
what you wish to do. (W=World, F=Fleet, U=Unload, A=Attack, S=Scrap, and so on.)

The object of StarWeb is to accumulate the most "victory points" during the game. Each player will get victory points 
for different things, as described in Section 4, "The Character Types".

 Table of Contents

3. HOW TO PLAY THE GAME

When you receive your first turn, you should find a copy of the latest "House Rules" (about two pages long) describing 
the latest procedures for making address changes, asking questions, paying for your game turns, and so forth. Please 
keep a copy of the House Rules with your game files, and if you receive one with a later date, read the new one and 
replace the old. We have thousands of turns coming in every two weeks, and we want to process them all with as few 
errors as possible. Therefore, it is very important that people follow the instructions. You should also find in your 
first turn a blank turn sheet and a short computer printout.

The first line of the computer printout will read: "ACCOUNT #9999". Your Flying Buffalo account number will appear 
within this space. Please mention this number in ALL transactions with us (payment to account, address changes, 
questions, resignations, errors, etc). You will also find the date the turn is due back to us stamped on the first line.

The next line on your printout will say: "Game SW-555". That means you are in game 555. Please mention the game number 
if you have any specific questions or problems with this game. You can be in more than one game if you wish, and we 
have many games going simultaneously. Your account number is always the same, but each different StarWeb game that 
you join will have a different game number.

The third line of your printout might say something like: [TERRAN]=Empire Builder. This means that your code name is 
TERRAN (and all the worlds and fleets that you own will be identified by the name TERRAN), that your character type is 
EMPIRE BUILDER (more about this later).

The next section will total up your current score, and all your assets (worlds, keys, ships, etc). This will be very 
useful later in the game.

The next line (or group of lines) might look something like this:

W75 (5,12,86) [TERRAN] (Industry=30, Metal=30, Mines=2, Population=50, Limit=100, Turns=1, I-Ships=1, P-Ships=1)

F3[TERRAN]=0
F70[TERRAN]=0
F102[TERRAN]=0
F119[TERRAN]=0
F133[TERRAN]=0
This all means that your homeworld is world number 75, that the three worlds directly adjacent to your homeworld are 
worlds #5, #12, and #86; that this world belongs to TERRAN (you); that you have 30 industry, 30 metal stockpiled, 
your mines produce 2 metal per turn, your current population is 50 and your maximum population is 100; the 
"Turns Owned Number" is one (more about this later); you have one I-SHIP and one P-SHIP guarding your planet; 
and that your five keys are numbered 3, 70, 102, 119, and 133. (There are two hundred and fifty five keys per game; 
each has a unique number from 1 to 255.)

The first thing you will want to do is build with your industry. The first part of a world's description is the number 
of industry on the world. Most worlds will have little or no industry. Each industry can build something every turn as 
long as there is a metal stockpiled and a population available to operate the industry. Notice that you have 30 
industry, 30 metal, and 50 population. You always build with the SMALLEST of these three numbers. You cannot build 
with metal that is not already stockpiled. Later on in the game you will see worlds with TWO industry numbers such 
as: "Industry=30/2". This means that although the world has 30 industry, only two of them can build this turn. 
(Usually because there is not enough metal.) On Turn 1, you can build with all 30 industry. Let's say you want to 
put ten ships on Fleet 3, ten on Fleet 70, eight on Fleet 102, and one each on Fleet 119 and Fleet 133. Your orders 
would be as follows:

W75B10F3
W75B10F70
W75B8F102
W75B1F119
W75B1F133
Now, you want to move your three large fleets to the three worlds adjacent to your homeworld. You would give the 
following orders:
F3W5
F70W12
F102W86
On Turn 2, your printout will tell you what is at these three worlds, and what worlds are adjacent to them. World 5 
might look like this:
W5 (18,75,66,103) [TERRAN] (Captured, Metal=5, Mines=5, Population=10, Limit=20, Turns=1)

F3[TERRAN]=10 (Moved)
F17[TERRAN]=0 (Captured)
This means that from World 5 you can move to worlds 18, 75, 66, or 103. The owner is TERRAN (you), the world has no 
industry (since none was listed), has 5 metal available and produces 5 per turn, has a population of 10 and a max 
population of 20, and a turns owned number of 1. F17 is a new key that you can use because you just captured it, and 
at the moment it has zero ships.
Now you have two choices. You can have the keys explore two new worlds, or you can have one key carry the 5 metal back 
to your homeworld, and the other one explore a new world. It is probably better to explore (and most likely capture) 
two new worlds, but we'll also show you how to carry metal back to your home world. You will also notice that this 
turn at your home world you still have 30 industry, and now you have 55 population, but you only have 2 metal. 
(You produced them from your mines this turn.) Since you can build with the SMALLEST of the three numbers, 
you can only build 2 ships this turn. You would probably build two more ships onto one of the keys still at home: 
W75B2F119, and have that fleet go on to one of the unexplored worlds: F119W5W18. (This means that Fleet 119 is moving 
through World 5 to get to World 18.) Any fleet can move up to three worlds in one turn.

Now for the ships at World 5. First, you probably want to leave a ship behind to guard World 5 for you. The world 
belongs to you until someone else takes it away from you. If you do not leave a ship behind, all someone else has 
to do is show up on the world and he or she will capture it. If you leave a ship there, the other player must first 
destroy the ship, which takes an additional turn. You can leave a ship on the ground guarding population 
(called a PSHIP), or guarding industry (called an ISHIP). Since there is no industry on W5, you probably want to make 
a PSHIP. The order you should give is: F3T1P.

This means that Fleet 3 is transferring one ship to become a PSHIP. Since a key with no ships cannot move (and can 
also be captured by any other player who shows up), you should also transfer some ships to the new key with this 
order: F3T4F17.

You have caused Fleet 3 to transfer 4 ships to Fleet 17.

IMPORTANT: Keys belong to someone. Ships do not. If you transfer ships to someone else's key, you are giving ships to 
that player. Make sure that a key or world is ALREADY listed as belonging to YOU before you transfer any ships to it. 
Transferring ships does NOT capture it. If a key's owner is listed as [ ], that means NO ONE owns it, and if you 
transfer any ships to it, you will create a NEUTRAL fleet. This is a common mistake made by beginners. If the key 
is not ALREADY listed as yours on your printout NOW, do not transfer ships to it until NEXT turn.

To put the 5 metal from World 5 onto Fleet 3 and move back home with them, you would order: F3L and F3W75. The first 
order causes fleet 3 to pick up all the metal it can carry. Each ship can carry 1 metal 
(or two if you were a merchant). You could also have ordered: F3L5 which orders fleet 3 to pick up 5 metal. 
You cannot order a fleet to pick up more metal than it can carry, but you can order it to pick up less. The second 
order sends Fleet 3 back to your homeworld.

You could not order Fleet 3 to unload its cargo yet, because all unloading comes BEFORE movement. Please notice that 
the order in which you write your instructions makes NO difference. The computer will execute all load and unload 
orders before it executes any move orders, even though you might have written the load orders at the end of your 
turnsheet.

Now, you want the new fleet to explore a new world, so you order: F17W66.

You have already sent Fleet 119 to explore World 18, and World 75 is yours. Also, you will probably want to 
explore W103 as soon as possible. It is generally a good idea to explore as many worlds as possible, as soon 
as possible.

On Turn 3, you can have Fleet 3 unload the 5 metal it is carrying, by ordering: F3U5 or F3U. The second order 
tells F3 to unload all its cargo. You only need to tell the fleet how many cargo to unload if you have some 
reason for not wanting to unload it all. These metal will be unloaded at the beginning of the turn, before 
anything else happens. However, you cannot build with them until next turn, when they will be part of your 
Metal Stockpile.

Now you know how to build, move, and carry metal around. If an enemy fleet (for example, Fleet 98) waits at a 
world, and you want your Fleet 70 to fire at it, the order is: F70AF98. This orders Fleet 70 to attack Fleet 98. If 
you want to fire at Fleet 98 only if the owner of that fleet fires at you, you would order a conditional fire like 
this: F70CF98.

 Table of Contents

BRIEF ORDER OF EVENTS: This is a short description of the order in which most major events happen:

Unloading metal (you can't build with it this turn).
Transfers of ships.
Building
Loading
Combat
Movement and ambushing
Special combat (PBBs and robots)
World and key capturing
Pirate Fleet capture.
Gifts.
 Table of Contents
IV. THE CHARACTER TYPES

You are one of six possible types of beings. Each character type (being) gets points for doing different things, as 
described below.

A. THE EMPIRE BUILDER. Your people believe in manifest destiny. It is your goal to control as much of the universe as 
possible. You get one point per turn for each 10 population you control (except for converts - see Apostle). You get 1 
point per turn for each industry you control (it makes no difference if the industry is able to build - if you own it, 
you get a point for it), and 1 point per turn for each MINE you control. In other words, a planet with 4 industry with 
6 mines and a population of 10 will gain you 11 points per turn. SPECIAL POWER: Other players can build an industry by 
using 5 other industry , or by scrapping 6 ISHPS. You can build a new industry using only 4 other industry, or 
scrapping 4 ISHPS.

 Table of Contents

B. THE MERCHANT. You are interested only in trade. You get 8 points for each metal which you unload on a planet owned 
by another player. (The other player can keep and use the metal which you unloaded.) You only get these points if 
there is INDUSTRY at the planet, and only up to twice the number of industry that is there. In other words, if you are 
unloading at another player's homeworld, where he or she has 30 industry, you can unload 60 metal per turn and get 
points for them. But at an outpost world where that player only has 1 industry, you can only get points for unloading 
2 metal per turn. This is to keep you from dumping excess raw materials on worthless worlds. If you UNLOAD and LOAD 
metal at the same world on the same turn, you only get points for the NET amount that was UNLOADED. If you unload 10 
metal, and load 6 metal back up on the same or different fleet, you only get points for 4 of them. Note that you do 
NOT get points for unloading onto a NEUTRAL world, or a world that you own either at the BEGINNING or at the END of 
the turn.

Merchants also get points for unloading CONSUMER GOODS on worlds. (Consumer goods are created merely by unloading metal
 and declaring that it is Consumer goods. They disappear when unloaded and cannot be used again.) The first time CGs 
 are unloaded on a world, you get 10 points. You get 8 points the second time, 5 points the third time, 3 the fourth 
 time, and after that you get 1 point each time. You get the points for unloading 1 CG. If you unload more than 1 CG 
 on the same world at the same time, you do not get any extra points.

SPECIAL POWER: As a Merchant, you can carry twice as many metal as other players. Other players' ships can carry 1 
metal each; your ships can carry 2 metal each. (However, ships carrying 2 metal cannot fire shots. or rather, they 
can fire shots but won't get any hits.)

 Table of Contents

C. THE PIRATE. You are interested in plunder, and you get points for plundering worlds. To plunder a world, you must 
own it and declare that you are plundering it. The first time you plunder a particular world, you get 50 points. 
(Then 40, 30, 20, and thereafter 10.) A world can only be plundered once every four turns. During the three turns 
after a world has been plundered, it will produce no metal, it will not increase in population and the industry on 
that world (if any) will not be able to build. The "turns owned" number won't increase, either. If a player other 
than a Pirate plunders a world (for instance, to make it less valuable to an enemy), he or she loses 5 points.

Pirates also get 3 points per turn for each KEY that they own. SPECIAL POWER: If a Pirate is at a world where his or 
her ships on fleets NOT at peace, outnumber all other ships on all keys by MORE THAN THREE TO ONE, then the pirate 
captures all enemy fleets without firing a shot. This capture is automatic, and it happens at the END of the turn. 
When you get your printout from the computer, all captured fleets will be listed as belonging to you (along with a 
"captured from" notation). Note that although you do not capture fleets belonging to your allies (see "Allies"), 
you must outnumber their ships by more than 3 to 1 also in order to capture any enemy fleets in the area. You do 
not have to outnumber ISHPS or PSHPS, and you cannot capture those.

The computer checks for Pirate capture AFTER it checks to see if someone captures a world or an empty key 
(see "Control of a World). So if you captured an enemy fleet at a world, you are not the "only person there" and you 
can't capture the world on the same turn. You will have to wait until the next turn to capture the world. Any ships 
that are GIFTED to a pirate will count AGAINST him for capture, since the gift comes AFTER pirate capture. However, 
ships TRANSFERRED to a pirate's fleet will be included as his, since pirate capture comes AFTER transfers and movement.

 Table of Contents

D. THE ARTIFACT COLLECTOR. As the richest person on a rich world, your jaded tastes are excited by the idea of owning 
unique things. On many of the worlds in the system, there are various indestructible artifacts left behind by that 
ancient race of beings. You get points for each of these artifacts that you own. (See "Artifacts".) You also get a 
bonus of 500 points at the end of the game for each world that you own which has 10 or more artifacts on it 
(including plastics); you have created a "museum". (The artifacts must be on the WORLD, not on a fleet.)

SPECIAL POWER: You are the only player who does not lose points for owning Plastic Artifacts. Also, you may transfer an 
artifact from one fleet to another (other players must unload the artifact onto a world on one turn, and then put it on 
another fleet on the next turn). And, other players may attach artifacts onto your fleets from their fleets or worlds. 
(A player may not put an artifact onto another player's fleet unless the receiving player is an artifact collector.)

 Table of Contents

E. THE BERSERKER. You are a computer in charge of a race of robots. Your prime directive is to kill all life wherever 
you find it. (You have no idea who gave you that directive, or why, but you never question it.) You are allowed to make 
temporary alliances with living beings (people who help Berserkers are called "Goodlife") if it will further your prime 
directive (i.e. allow you to kill even more living beings). However, your robots and people cannot exist on the same 
world at the same time. They kill each other off - 1 robot kills 4 people, and 4 people kill 1 robot. Fractions of 
robots lost are rounded up. Thus, 1 person kills 1 robot, 4 people kill one robot, 5 people kill 2 robots, etc.

You may control worlds with living beings on them, but other players (except other Berserkers) cannot control your 
robots. They can drive a robot-populated world NEUTRAL, but a non-berserker can not control it until all the robots 
are destroyed. Your robots may ignore the population limits described later in the rules (you don't care how many 
people a world can support, since your robots are not people).

You get two points for each population you kill (normal or converted, but not robots) by shooting, by unloading robots 
on the world, or by destroying the world! You get 5 points per turn for each world you own that is populated by robots. 
If you destroy a fleet of ships, you get two points for each ship destroyed. (If you only damage a fleet, you don't get 
any points.) If you destroy an entire world (!) by dropping a Planet Buster Bomb (PBB) on it, you get 200 points for 
the bomb, plus the points for the population. (You can only PBB a particular world once for points.) If any other 
player drops a PBB (except an Apostle on a Jihad - see Apostle), he loses 50 points. If any other character type kills 
population (except for an Apostle on a Jihad), he loses 1 point for each population he kills. Note that if 2 or more 
players both fire at the population of the same world, each gains or loses the proper number of points for the TOTAL 
population that died there that turn.

SPECIAL POWER: A Berserker can convert some of his ships on keys to robots, and they immediately drop to the world 
below (robot attack). If a Berserker drops robots on a world, killing all the population, and leaves at least 1 robot 
on the world, he or she captures the world, including any PSHPS or ISHPS which are there. If two Berserkers make a 
robot attack at the same time, one or the other of them will capture the world and all the robots - the odds of a 
player being the winner are proportional to the number of robots that player used in the attack.

The Berserker character is adapted from stories written and copyrighted by Fred Saberhagen, and the name is used with 
his permission.

 Table of Contents

F. THE APOSTLE. You are a religious fanatic (or political fanatic, if you prefer). Your purpose is to convert the entire
 galaxy to your particular point of view. Each of your converts on a world has a 10% chance of converting one normal 
 population to a convert, each turn. If you have a fleet of ships "not at peace" at a world, each of those ships has a 
 10% chance of converting one normal population to a convert, each turn. (This does Not mean that if you have 10 ships 
 at a world, you will always convert exactly one population. You could convert none, and you could conceivably convert 
 as many as 10.)

The conversion takes place at the beginning of the turn, so if a fleet is moving, it will create converts at the world 
it just left. Other players may get rid of your converts by killing them, but you'll get one point for each one killed 
(they're Martyrs) and of course any non-berserker who shoots at population will lose 1 point for each one killed. Or, 
other players may get rid of your converts by converting them back to normal by unloading consumer goods on them 
(bribing them with material goods). Each CG unloaded on a world has a 50% chance of converting one convert back to 
"normal".

You WILL convert population at worlds belonging to your allies, but any of your ships "at peace" will not convert 
anyone (see "At Peace"). If you have any converts at a world, you will get a probe of that world as long as the 
converts survive.

Apostles get 5 points per turn for each world they control, and 1 point per turn for each 10 of their converts in the 
universe. They also get an additional 5 points per turn for each world they own which is completely populated by their 
converts. As an Apostle, you LOSE one point for each shot you fire - you are a pacifist. (For this purpose, ambushes 
are not "shots".)

Only one Apostle can have converts on a particular world at a time. If two Apostles try to convert at the same world, 
the computer will award all the converts to one or the other. The odds of being the winner will be proportional to the 
number of converts or ships the player has at that world.

At any time during the game you may declare a JIHAD (holy war) against any one player. You no longer get any points for 
martyrs (no matter who kills them), but you don't lose points when you fire at that one player, and you get two points 
for each of his or her population you kill. If you declare a Jihad against a Berserker, you don't get any points for 
killing robots, but you would only get points for killing normal population controlled by the Berserker. You cannot 
cancel the Jihad once it is declared, but you may change it to a different enemy (every turn, if you like). If you 
fire at population, you get the Jihad points if the world is controlled by your enemy either at the beginning, or 
the end of the turn, or both. (In other words, you CAN get points by giving the world to your Jihad victim on the 
turn you shoot at the world.) However you do NOT get points for killing your own converts, even if they are on a 
world controlled by your enemy. (You lose points for them.)

SPECIAL POWER: If you completely convert the entire population of a world, you gain control of that world, overriding 
the rules about control of a world listed elsewhere in these rules. Also, if you give away a world that has been 
completely converted, it will come right back to you on the next turn.

 Table of Contents

5. DETAILS ON PLAYING THE GAME

You now know how to get started. Read through this section briefly, but don't worry if you don't understand or remember
 it all the first time. Most of these details won't be important until the later turns of the game, after you have 
 become familiar with the general details.

 Table of Contents

6. SHIPS. Ships must either be attached to a key, or be on a world. There can only be a maximum of 255 ships on any one 
key. If the ships are on a world, they must either defend industry (ISHPS) or defend population (PSHPS). ISHPS and 
PSHPS collectively are known as "Home Fleets". Note that ISHP and PSHP refer only to the position of the ship. All 
ships are identical.

ISHPS and PSHPS cannot fire at each other, or at industry or population. They CAN fire at converts on their world.

The only possible cargo of a ship is metal. Each ship can carry one metal (except merchants, who can carry two). Ships 
can be freely moved from fleet to fleet (at the same world) or to ISHPS or PSHPS and back at the beginning of the turn 
(before movement or firing or loading metal, but after unloading metal). This is called a "transfer" and is not 
considered movement. If you transfer from fleet to fleet, only SHIPS will transfer (not metal or artifacts). If 
you try to transfer loaded ships, the ships will transfer but the metal will disappear.

Six ISHPS which are at a world (as ISHPS) at the beginning of a turn may be scrapped and turned into one industry (4 
ISHPS for Empire Builders). (If the ships are on a fleet, it will take two turns to create industry: one to transfer 
them to ISHPS and one more to scrap them.) This is the ONLY way to get industry at a world which does not already have 
industry.

 Table of Contents

7. KEYS. Each player starts with five keys. "Fleet" and "Key" are the same thing; each of your fleets is a key. If your 
code name is TERRAN, then one of your fleets will look like this on your printout:

F85[TERRAN]=5 (Moved,Cargo=2)

That means your Fleet # 85 has 5 ships, is carrying 2 metal, and moved this turn. (If a fleet belongs to another player,
 you will NOT be told how many metal it is carrying.) Each key has a unique number, so there is only one Fleet #85 in 
 your game. If your printout says:

F85[ ]=0

That means F85 is an UNOWNED or NEUTRAL key. You do NOT own it, so do not transfer ships to it. Please note that if you 
leave an empty key (one with no ships on it) at a world where there are no other ships (no other fleets, and no ISHPS 
or PSHPS), then the key will be listed as UNOWNED and if you BUILD a ship onto it on the next turn, you will NOT 
capture it. (See "Loose Keys"). A common error for beginners is to put all their ships onto some of their keys, 
moving all the ships away, and leaving one or more keys behind with NO ships. Then NEXT turn while these keys are 
NEUTRAL, the beginner builds ships onto the neutral keys and creates a NEUTRAL fleet at his homeworld, which cannot 
be used. NEVER leave keys around with no ships on them unless you are trying to let another player capture them!

 Table of Contents

8. CONTROL OF A WORLD. You capture a world if you are the only player there with ships that are not at peace. Of course,
 there are exceptions. You will not capture a world from a player whom you have declared an "ally". If you are a Pirate 
 and you have captured an enemy fleet this turn, the computer will NOT consider you the only player there this turn. If 
 the world is populated by robots, you cannot capture it unless you are a Berserker. If the world is populated entirely 
 by converts, you cannot capture it until you un-convert some of the population. A fleet belonging to the owner of the 
 world, or to a player who has declared the owner his ally, will prevent capture, even if the fleet is at peace. A 
 world with zero population cannot be owned.

Apostles can also capture a world by converting all of its population to their religion. Berserkers can also capture 
worlds by making a robot attack and destroying all the population (leaving at least one robot).

If you own a world, it remains yours until some other player meets the capture requirements, or until some other player 
forces it neutral by destroying all the ISHPS and PSHPS and firing at least two more shots than are necessary to destroy 
all the home fleets. You do not have to have any ships at a world to retain control, but if another player shows up and
 you do not have any ships there, you lose the world. If you show up at an unowned world which already has some ISHPS 
 or PSHPS, you will not capture that world until you destroy the home fleets.

 Table of Contents

9. BUILDING. You may build at any world where you have at least 1 industry, 1 population, and 1 metal. The amount you 
can build is equal to the SMALLEST of these three numbers (and the metal are used up when you build).

If there is an enemy fleet "not at peace" at your world, for each shot he has which outnumbers your defending ships, 
one industry will not build (your population is hiding inside bomb shelters). This is automatic, and is shown on your 
printout. If you have 30 industry, but only 25 are allowed to build because of enemy presence (or any other reason), 
your industry will be listed on your printout as 30/25. For this purpose only, ISHPS are counted as double. That is, if 
you have 4 ISHPS at the world, and the enemy has 10 ships, only 2 of your industry will be unable to build because of 
enemy presence. Also any ships present belonging to a player who has declared you "ally" will be counted as defending 
your industry.

"METAL" on your printout is how many raw materials you have stockpiled on that world. This is how many you can use to 
build this turn. You cannot use the ones which are going to be produced, nor can you use the ones that are being 
unloaded.

"MINES" tells you how many metal are going to be produced for NEXT turn. Note that all building must be done at the 
world where the industry is. You cannot build ships onto a fleet that is located somewhere else. Building comes 
before loading, movement, or firing. You cannot load the metal that is going to be used by the industry this turn. 
You can build onto a fleet that is moving away or firing, and the new ships count in the number of shots you get to 
fire.

Each industry can build 1 ship. Each 5 industry (4 for empire builders) can build 1 more industry using 5 metal and 5 
population. Each 5 industry (4 for empire builders) can increase the population limit of the planet they are on by 1. 
Each industry can build 2 robots (but ONLY if the population of that world is already robots. Non-berserkers cannot 
build robots & berserkers cannot build robots at worlds populated by people.) Remember, in each case you must have 1 
population to run each industry, and you use up one metal per industry. If a world does not have enough population to 
run BOTH the industry AND produce the metal from its mines, it will alternate. Example: if a world has 5 industry and 
5 mines, but only 5 population, then one turn it will create METAL, and the next turn the industry will turn those 
5 metal into ships or whatever.

You may also use your industry to move some of your population to an adjacent world. This is the only way to increase 
population at a world other than by normal growth. One industry, using 1 metal, moves 1 population to an adjacent world 
(which must be connected to that world by a gate). When you use this option, you are building a short- run colony ship 
which expends itself by moving to the next system. This is called Migrating Population. Robots are migrated using the 
same order as normal population. If you want to migrate CONVERTS, you must specify them with a special order. If you 
migrate population, you do NOT gain control of the adjacent system or even a report on that world. All you do is 
decrease the normal population of your world, and increase of population of the neighboring world. If you migrate 
CONVERTS or ROBOTS, however, you DO get a report on the world, and you can capture the world if you meet the capture 
requirements. (Assuming of course that they are YOUR converts. If you migrate someone else's converts, then HE gets 
the report on the new world.) If a berserker migrates robots to a world populated by people, he DOES get points for 
killing those people.

You can only migrate to ONE world from any given world on a single turn, and you cannot give away the world or fire 
with its PSHPS or ISHPS on the turn that you migrate. (You can migrate TO a world from all of its adjacent worlds, but 
you can only migrate FROM a world in one direction at a time.)

 Table of Contents

10. POPULATION. Each world has a population and a population limit. The population of an owned world will grow 
approximately 10% per turn until it reaches the limit, and then it will stop growing. If the world is owned by an 
Apostle, the new population will be all converts. You cannot have more population than the population limit of the 
world. If you put extra people there (by migration), they will die. (However, they will have one turn in which to 
build before they die. This is an expensive way of increasing the population limit of a world whose limit is less 
than 5, and unless you are a Berserker, it is the only way. Berserker robots, of course, ignore the population limits.) 
Robots do not "grow". (They must be built.)

If your population is less than your MINES, you will not produce the full number of metal per turn. If you have 4 mines, 
but only 3 population, you will only produce 3 metal per turn. In addition, if you have an industry at that world, and y
ou build something with that industry, it takes one population, so the next turn only TWO metal will be produced. Please
 remember that - people often call us and ask why their world with 2 industry and 2 mines and 3 population only produced 
 1 metal last turn.

If someone fires at population, or if robots are attacking a world, you will notice:

DEATHS=N

with "N" being the number of population killed that turn. Every Berserker (or Apostle on a Jihad) who killed population 
at that world, that turn, will receive 2 points for each, and every non-Berserker who fired at population at that world 
that turn will lose 1 point for each. Worlds which have no population will be neutral, and will not be controlled by 
anyone.

 Table of Contents

11. MOVING. Each fleet may move up to three worlds per turn (with one single order). For all official purposes, you are 
only "on" the world you started on or the one you ended up on. You may be ambushed at any of the intervening worlds, 
and you will get reports of them, but you may not do anything at those worlds. Any player who ambushes you as you try 
to move gets double hits on you. If you make a move that is partly illegal, the fleet will NOT move AT ALL. (Example, 
if you are at world 1, which is adjacent to world 13, and you order a move "W2W31" instead of "W2W13", you fleet will 
NOT move to world 2 and stop. It will not move at all.)

Note that loading and unloading of fleets, and all transfers, come BEFORE movement. This means that you can NOT move and
 then transfer, nor can you move and then unload. It makes no difference in what order you write your instructions on 
 the turn sheet. If you tell Fleet #1 to move from World 34 to World 46, and then you tell Fleet #1 to unload its 3 
 metal and its one artifact, it will unload them ON WORLD 34.

You may load and move. You may unload and move. You may transfer and move, or probe and move. You may NOT fire and move,
 or ambush and move, or move a fleet the turn you give it away.

 Table of Contents

12. PROBES. You may send a probe to an adjacent world. This uses up one ship (which does not require a key), and tells 
you what is on that world and what its adjacent worlds are (as though you were there). You have sent a ship through a 
gate without a key - it gets through long enough to send back a report, and then burns up. It is not seen by any other 
player, and it cannot "carry" an artifact to that world. You cannot probe a world if you own it or have fleets or 
converts there, nor can you probe a world more than once per turn.

Probes are sent from the world you begin the turn at. You cannot probe with a ship on the turn it is built, or the turn 
you transfer it from one fleet to another. (There is no reason to transfer it if you are going to probe with it, but 
someone always makes that mistake.)

The world that you begin the game with is considered your "home world". You will always receive a report or probe of 
this world, even if you lose control of it. (There is no particular penalty for losing control of you "home" world.) 
You will get a report on every world where you have a fleet, where you have converts, where you own the world, where 
you had a fleet at the beginning of the turn, and where you passed through on the way to another world.

 Table of Contents

13. CARGO. Each ship (except for those owned by Merchants) may carry ONE metal as cargo. If a fleet is carrying metal, 
it may unload them on a world, jettison them (destroy them), unload them as consumer goods (as a Merchant to get 
points, or as any player to get rid of converts). You may pick up metal from any world you own with any fleet at that 
world. If the world is not yours, then the player who owns the world must have declared you a "loader" (either this 
turn or on a previous turn). Once you have been declared a "loader" by a player, you remain that way until he changes 
his mind and gives a "non-loader" order for you. You will not be told by the computer that you are a "loader". You'll 
know if you succeed in picking up metal from his world.

You can specify a number of metal to pick up, or you can just say "load" and your fleet will pick up as many metal as 
it can find and carry. You cannot overload your ship, nor can you pick up metal that is going to be used for building 
that turn. If two players load at the same world, and there is not enough metal for both of them, the owner of the 
world gets preference. (His ship is filled before the other player gets any). If two or more players (both loaders) 
are at a world neither of them owns, and both try to load, the one with the smallest NUMBERED fleet will get 
preference. (i.e. fleet #1 gets loaded before fleet #5). (In certain variant games it will be a random numbered fleet).

If a Pirate captures a Merchant fleet which is carrying more than 1 metal per ship, the excess metal disappears (ditto 
if the merchant gives away the fleet). Jettisoning and unloading cargo come BEFORE firing, so you can avoid taking the 
extra damage caused by being loaded with cargo. (See"Firing"). Transferring from fleet to fleet and building new ships 
comes after unloading and before loading. Artifacts are NOT considered cargo. Remember that transferring loaded ships 
automatically jettisons the cargo. You can load metal that someone else is unloading that turn.

 Table of Contents

14. ARTIFACTS. Any fleet may carry any number of artifacts. The artifacts are attached to the KEY and not the ships. 
If the fleet carrying the artifacts is destroyed, the artifacts remains neutral until there is only one player at that 
world with ships not at peace (in other words, until some player captures the key it is attached to). There are 90 
standard artifacts, and 10 special artifacts. The standard artifacts will consist of two words. The first word can 
be any of these: Platinum, Ancient, Vegan, Blessed, Arcturian, Silver, Titanium, Gold, Radiant, Plastic. The second 
word can be any of these: Lodestar, Pyramid, Stardust, Shekel, Crown, Sword, Moonstone, Sepulchre, Sphinx.

Thus an artifact would be known as the SILVER SWORD, or the BLESSED STARDUST, or the PLASTIC CROWN. Each type of 
character would like to collect two distinct types of artifacts. Empire Builders, for instance, would like all 
PLATINUM items and all CROWNS. The PLATINUM CROWN is their "Greatest Treasure". Here is a chart of what each
 player wants:

  Empire Builder............Platinum, Crown
  Merchant.....................Gold, Shekel
  Pirate ..................Silver, Lodestar
  Apostle ...............Blessed, Sepulchre
  Berserker.................Titanium, Sword
  Artifact Collector.......Ancient, Pyramid
Note that there is some conflict here, as both the Empire Builder and the Merchant will want the "GOLDEN CROWN" and of 
course the Artifact Collector will want everything.
The special artifacts are the TREASURE OF POLARIS, the SLIPPERS OF VENUS, the RADIOACTIVE ISOTOPE, the LESSER OF TWO
 EVILS, the NEBULA SCROLLS (Volumes 1-5), and the BLACK BOX.

Players gain (or lose) points for holding certain artifacts. Character types other than Artifact Collectors are awarded 
points according to the following schedule:

For holding a standard artifact from one of your categories (Note: the Plastic item is not considered part of your 
category) ... 5 pts/turn
For holding a standard artifact not from your category ... 0 pts/turn
For holding your "Greatest Treasure" ... 15 pts/turn
For holding any Plastic item ... lose 10 pts/turn
For holding the Treasure of Polaris ... 20 pts/turn
For holding the Slippers of Venus ... 10 pts/turn
For holding the Radioactive Isotope ... lose 30 pts/turn
For holding the Lesser of Two Evils ... lose 15 pts/turn
For holding all 5 Nebula Scrolls at the end of the game ... 1000 pts
For holding all the standard Artifacts in either of your two categories at the end of the game ... 500 pts
For holding the Black Box ... 0 pts/turn
The Artifact Collector gets more points for each item, as follows:
For holding any Ancient item or Pyramid (Note: the Plastic Pyramid is not considered part of your category ... 
30 pts/turn
For holding the Ancient Pyramid ... 90 per/turn
For holding any other standard artifact (non-plastic) ... 15 pts/turn
For holding any Plastic item ... 0 pts/turn
For holding the Treasure, the Slippers, the Isotope, or the Lesser ... 30 pts/turn
For holding all 9 Ancient items, or all 9 Pyramids at the end of the game ... 1000 pts
For holding all 5 Nebula Scrolls at the end of the game ... 1500 pts
For holding the Black Box ... 30 pts/turn
For each museum held at the end of the game (10 artifacts on a world) ... 500 pts.
The Black Box is special. If you own it, this artifact may do something to you or for you. Each game, the Black Box
 will do something different. We will decide when the game starts what that particular Black Box will do, and you will
  not be told what it is. If you find the Black Box, you will have to determine what it is doing (if anything). It may 
  do something every turn (like produce one extra metal each turn) or it may do something every once in a while (like 
  double the number of mines of the world it is on every 8th turn) or it may go in some kind of cycle (produces an 
  industry every turn except on the 10th turn it blows up the world it is on!). The effect may be good, or bad, or 
  mixed, or it may be nothing at all. The Black Box MAY tell you something (thus, it is illegal to sign the Black 
  Box's name to a diplomatic message), but the Black Box will never answer questions, so please do not address 
  questions to it.
Each artifact has a number which will appear with the artifact on your printout. (The "V" is NOT part of the number, 
and is just there to remind you that all artifact orders start with a "V").

An artifact may be hooked onto one of your fleets, unhooked from your fleet onto the world your fleet is located, or 
hooked onto the fleet of an Artifact Collector. You may NOT hook it onto a fleet of a player who is not an artifact 
collector, and you may NOT transfer it directly from one fleet to another fleet unless you are a collector, or the 
fleet you are transferring it to belongs to a collector. You are only allowed to give ONE order per artifact per 
turn. An artifact is attached to a fleet if it appears after that fleet on the printout. An artifact belongs to the 
player who owns the world or fleet it is on.

If you have a bad artifact you want to dispose of, you can unhook (unload) it on a world that does not belong to you, 
give it to an artifact collector, or attach it onto a fleet and fly the fleet into a black hole (see "Black Holes"). 
If you do not own the world that an artifact is on, you cannot hook that artifact onto a fleet.

 Table of Contents

15. FIRING. Each ship gets one shot per turn (1 shot = 1 hit) except ISHPS, PSHPS, and overloaded merchant ships. ISHPS 
and PSHPS get 1/2 shot each (odd ship rounded up). Merchants can carry double cargo on their fleets, but each ship 
carrying a double cargo cannot fire. (If you have 5 ships carrying 6 metal, only 4 of the ships can fire.) Each 
fleet must fire all of its shots at one target. If the ISHPS fire, they must all fire at the same target; ditto for 
PSHPS. (That is, if you have 1 fleet, plus ISHPS and PSHPS at the same world, they can fire at 3 different targets, 
but not 4 different targets.)

Fleets may fire at another fleet at the world, or may fire at industry, population, or home fleets (ISHPS and PSHPS are 
known collectively as home fleets; this has nothing in particular to do with your home world). ISHPS and PSHPS can fire 
at fleets or at converts (and nothing else). Fleets can fire at population; if there are converts in the population, 
some of the casualties will be converts, but the fleet cannot specify that it is shooting only at converts. In order 
to fire at robots, you just fire at "population".

You must always specify which fleet you are firing at. If you destroy all ships attached to a key, that key becomes 
neutral until there is only one player at that world with ships not at peace. Each 2 shots destroys 1 unloaded ship 
or 2 loaded ships. (You cannot merely damage a ship. One shot will not harm an unloaded ship.) If the enemy fleet is 
leaving instead of firing back at you, you only get half as many hits. If you destroy all the ships on a fleet that is 
trying to move away, the key stays where you are. If a fleet moves, it cannot fire that turn. (You can NOT move to a 
world and fire at it on the same turn. If you write an order to move and an order to fire for the same fleet, whichever 
one we happen to type first will be executed, and the other one will be ignored.)

If you fire at industry, first you must destroy all ISHPS at 2 hits apiece. The remaining shots destroy industry at 2 
hits for 1 industry. If you fire at population, you must first destroy the PSHPS at 2 hits apiece; the remaining shots 
will destroy population at 2 hits per 1 population.

If you fire at home fleets, you first destroy the ISHPS, then the PSHPS. Any remaining shots fired at home fleets do not
 destroy anything, but if there are at least 2 extra shots fired at a home fleet, the world becomes neutral until there
  is only one player there with ships not at peace. (Even if the owner of the world has fleets there. And if a world
   has no home fleets, you must fire at least 2 shots at it to force it neutral.) This is how you take a world away 
   from your enemy when you are unable to capture it for yourself.

It is NOT necessary to force a world neutral if you are able to capture it. If you just want to destroy all the enemy 
ships guarding a world, but not the population or industry, you fire at home fleets. If you fire at converts
 (ISHPS and PSHPS only), each shot destroys one convert.

Each attack must be either conditional or unconditional. An unconditional attack fires, no matter what. A conditional 
attack means you fire at the specified target IF AND ONLY IF the owner of the target fires at YOU this turn AT THAT 
WORLD. If both players give only conditional fire orders, then neither will fire. An ambush will NOT trigger a 
conditional fire order, but a robot attack WILL trigger conditional fire. A conditional fire order IS AN ATTACK 
ORDER, and you cannot move or ambush or give away a fleet if you give a conditional fire order. (The conditional 
fire order is effective only for the turn you give it. It does not remain in effect on the next turn.)

When shooting at ships, hits are first taken by unloaded ships, then by loaded ships. You may only fire at a target 
which STARTS the turn at the same world as the firing unit.

 Table of Contents

16. AMBUSH. Unless you specify not to ambush at all this turn, or not to ambush at this world this turn, any 
fleets that have not moved or fired, and all unfired home fleets will ambush any fleet (not belonging to an ally) 
which tries to move THROUGH that world. This only applies if that fleet moves through the world without stopping.

For example, Player A has F85 at World 1, and wants to move through Worlds 2 and 3 to get to World 4. He orders 
"F85W2W3W4". He can be ambushed by any player at World 2 or World 3. He can NOT be ambushed at World 1 or World 
4 (Nor can a fleet at W4 fire at F85 until NEXT turn.)

This ambush order confuses a lot of players. They want to ambush anyone who appears at their world, and it is 
NOT possible. The ambush order exists to guard your inner circle of worlds by putting ambush ships on the outer 
fringes of your empire. An enemy must either stop and fire at your outer ships, or fly past them and let you ambush 
him. Note that any enemy ships which have not moved or fired will ambush you even if they are at one of your worlds. 
Fleets do not have to be at their own worlds to ambush.

When you are ambushing, ISHPS and PSHPS are not halved as they are when firing, AND all ships are doubled when 
ambushing. Thus, a fleet of 2 ships or 2 ISHPS will destroy two enemy ships (or four, if they are loaded with metal). 
Home fleets won't ambush if their world does a migration or is being given away.

If you only destroyed some of the ships, the remainder of the fleet will continue on to where it was headed. If you 
destroy all the ships, the empty key will remain at the world where it was ambushed. A ship ambushing will shoot at 
every enemy fleet that moves through. This is the only case where a ship may fire more than once per turn.

You will not ambush fleets belonging to players you have declared ALLY. A fleet will not ambush if it has given an a 
conditional fire order, or if it is making a robot attack or dropping a PBB. Fleets "At Peace" do ambush. Gifts do not 
ambush.

 Table of Contents

17. ALLIES. You start the game with no allies. After you have met another player, you may declare him or her an ally, 
if you wish. That player will remain your ally until you subsequently declare him or her a non-ally. You will not 
ambush any allied ships, and you will not capture worlds belonging to your ally. (Your ships will help protect 
allied industry and even if they are "at peace" they will keep enemy fleets from capturing allied worlds.) If you are 
a Pirate, you will not capture your ally's ships. (But you do have to outnumber your ally's ships if they are at the 
same world where you are trying to capture enemy ships.) If you are an Apostle, you WILL convert an ally's population.

The word "Ally" has additional connotations which DO NOT APPLY in StarWeb. If YOU declare someone your ally, the only 
thing it means is that you will not ambush his fleets or capture his worlds. That player does not have to declare 
YOU an ally, and he or she can still ambush you and capture your worlds. You will not be told whether another player 
has declared you an ally or not. Being an ally has NOTHING to do with whether you can FIRE at another player. All it 
does is make sure you won't do any automatic nasties against the player who you think is your friend.

 Table of Contents

18. GIFTS. At any time after you have met another player in the game, you may give a fleet or world to that player - 
but neither of you can move the fleet or fire its shots the turn it is given away. If you have given away a world, 
you can neither fire with its ISHPS or PSHPS nor plunder it the turn you give it away. You may build with industry 
on the turn a world is given away, and you can load or unload metal or artifacts. You may only make TWO gift orders 
per turn, and only to players who you have met at some point in the game. (i.e. one of their worlds or fleets or 
converts or robots has appeared on your printout at least once so far in the game.) The player who receives a gift 
is told who gave it to him.

 Table of Contents

19. PLUNDERING. At any time you can plunder a world which you control. If the world is taken away from you that turn, 
or if you give it away, the plunder fails. While a world recovers from the plunder (the next 3 turns), it will not 
build with its industry, increase in population, or produce metal. You cannot plunder a world again while it is 
recovering from a previous plunder.

 Table of Contents

20. AT PEACE. You may at any time declare any fleet "at peace". It will subsequently appear on the printout with 
"At-Peace" after it, until you declare it "not at peace". (All keys and fleets start out "not at peace"). This ONLY 
means that this fleet will not capture loose keys or worlds, nor will it prevent other players from capturing them. 
(However, a fleet "at peace" at one of your OWN or an ALLY'S worlds will prevent another player from capturing 
that world.)

You should order a fleet to be "at peace" if you want to move to a world without capturing it, or if you want to 
allow another player to capture a loose key or world without requiring you to leave.

Apostle fleets "at peace" do not convert. A fleet "at peace" will not prevent industry from building. Being "at peace" 
does NOT prevent you from firing or ambushing; it merely means you don't want to capture anything. (Pirate fleets 
"at peace" will not capture enemy fleets, either.) Most of the time you will want your fleets to be "not at peace".

 Table of Contents

21. PLANET BUSTER BOMBS. Any time a fleet contains MORE than 25 ships, you can convert 25 of them into a PBB (Planet 
Buster Bomb). The fleet does not have to start the turn with the 25 ships -- you can be transferring them to the 
fleet on the turn you build the bomb. You may move or fire or drop a previously-built PBB on the turn that you build 
a PBB (but you can only have one PBB on a single fleet at a time). On any subsequent turn you may drop the bomb you 
just built (you cannot drop it the turn it is built).

Dropping a PBB is a FIRE order, and you cannot move on the turn you drop it. (See "Mutually Exclusive Orders") If 
you drop the bomb, and the fleet carrying it is not destroyed by some other player on the turn it attempts the drop, 
everything on that world (except artifacts) is destroyed. All population, industry, mines, metal, PSHPS, ISHPS, and 
robots are destroyed. The population limit is reduced to zero. Fleets are not affected. Attempting to drop a PBB DOES 
trigger "conditional fire".

You cannot fire with the fleet which is dropping the bomb. If the fleet is destroyed (or if you transfer all ships 
away from it), the PBB is destroyed. PBBs cannot be transferred from fleet to fleet, or jettisoned. The PBB will 
appear on the printout, and everyone who can see your fleet will know you have a PBB. Berserkers gain points for 
dropping PBBs, and everyone else loses 50 points (plus losing points for population killed) for dropping them, 
except an Apostle on a Jihad if he drops it on his Jihad victim.

 Table of Contents

22. ROBOTS. In most cases, robot populations will act the same as regular populations. However, there are certain 
exceptions. Robots will not be converted by Apostles. Robot populations can ignore population limits (and can survive 
on worlds previously "planet busted"). Also, robot populations will not increase 10% like regular population. If you 
want to give an order regarding robot population (fire at population, or migrate population) you just give the same 
order you would give if it were regular population.

A Berserker may convert some of his ships to robots (1 ship = 2 robots) and the robots immediately land on the world 
where the fleet is, and start killing people. (This is a "robot attack". The fleet making the robot attack cannot move 
or fire.) Shots fired at fleets making a robot attack will kill the robots first. Thus, if a Berserker orders F7R2 
(Fleet 7 convert 2 ships to robots) and at the same time an enemy fires 4 shots at F7 (enough to destroy 2 ships) 
then F7 will be noted on the printout as having made a robot attack, but no robots will get through to the planet 
below, and no damage will be done to population.

A berserker may make a robot attack on a world already populated with other robots. In this case, no population is 
killed; the new robots are just added to the previous ones. If the robots on the world are not owned by the player 
making the robot attack, one player or the other will randomly be chosen to own ALL the robots, with the odds being 
proportional to how many robots each player owns. (Example: A player makes a robot attack with 5 ships (10 robots) on 
a world populated by 90 neutral robots. The new population will be 100 robots, and the player has a 10% chance of 
capturing the world. There is a 90% chance that instead, all 100 robots will be neutral.)

A fleet may never convert ALL its ships to robots. At least one ship must be left behind on the key. If you make an 
error, the computer will automatically reduce your Robot Attack order enough to leave 1 ship behind. You can make a 
robot attack with ships which are being transferred to that fleet. A Berserker can move robots to an adjacent world 
using industry and metal (migrating), the same as other players can migrate population, and he will get a probe of the 
world and credit for killing any population. A berserker can capture a world this way. A robot attack WILL trigger a 
conditional fire order.

 Table of Contents

23. METAL PRODUCTION (MINES) AND THE TURNS NUMBER. Each mine produces one metal per turn. It is stockpiled on the world 
unless picked up by a fleet. The maximum MINES for a world is 31. You can stockpile up to 255 metal at any one world. 
You must have population at the world not building with industry in order for the mine to produce its metal.

For example, if you have a world with 6 industry, 6 mines, and 10 population, and you build with all 6 industry, only 4 
of the mines will produce metal for the next turn. (However, you can not voluntarily avoid building with the industry 
if there is enough metal at the world. A world with industry, metal, and population WILL build.)

Another example would be if you had a world with 5 mines, a population of 2, and a population limit of 3. That world 
will only produce 2 metal per turn until you put another population there by migration (or until the population 
increases, which might happen in about 5 turns). It will never produce more than 3 metal per turn unless you are a 
Berserker and you put 5 robots on the world. (Or if you increase the population limit by the expensive method 
mentioned earlier.)

There is only one way the MINES on a world can increase. Each world which already has at LEAST one mine, has a "Turns" 
number (Number of turns the world has been owned by its current owner). That number starts at 1 when you capture a 
world, and increases by 1 each turn unless interrupted by a plunder or capture of the world. The turn after the Turns 
number reaches 7, it goes back to 1, and the MINES on the world go up by 1. That means two things: First, a world which 
has no mines does not have a Turns number and will never have any mines. Second, if you own a world with mines for 7 
consecutive turns, your MINES increase. If you plunder a world, the Turns number stops where it is until the world 
recovers from the plunder, and then continues. If a Berserker robotizes a world which he already owned, the Turns 
number starts over at 1, just as if he had captured it from another player.

 Table of Contents

24. LOOSE KEYS. Any fleet with no ships on it is a loose key. Any loose key is captured by the only player there with 
ships not at peace. Home fleets are NEVER at peace. Keys are never destroyed. If you leave keys with no ships attached 
to them around on your worlds, those keys will belong to you as long as you are the only player there with ships. If 
another player shows up, the key will not be owned by anyone. (And note that if you don't have any ships at that world, 
you won't own the key either.) It is advisable, therefore, to attach at least one ship to every key you own.

To attach a ship to a key, transfer a ship from another fleet to that key, or build a ship onto the key with your 
industry which is at the same world. REMEMBER: If you do not ALREADY own the key, and you attach a ship to it, you 
STILL do not own the key. You have created a neutral fleet. Beginners do this often. If the name after the fleet number 
is your name, then you own the key. If the name after the fleet number is [ ], then no one owns the key. Players do not 
own SHIPS; they own KEYS and all the ships attached.

 Table of Contents

25. BLACK HOLES. A few of the worlds on the map are black holes. If you move into or through a black hole, all the ships
 which move in are destroyed. The key will reappear at some random place in the galaxy, along with any artifacts which 
 were carried. If you probe a black hole, you will discover what it is. However, there are only a few black holes in 
 each game, so don't be paranoid.

 Table of Contents

26. DIPLOMATIC MESSAGES and SIGNS - CONTACTING OTHER PLAYERS.

A SIGN is a short message (up to 2 lines of up to 78 characters each) that is posted on all of your worlds and fleets. 
When another player meets you for the first time, the text of your sign will appear on his printout. If you change to 
contents of your sign, anyone who has ever seen you will be given the text of your new sign. To add or change your sign,
 write the word SIGN below the orders on your turn sheet, and then 1 or 2 lines of text of up to 78 characters each. 
 You can change your sign every turn if you like.

Once you have met another player (his name has appeared on your printout) or another player has introduced you to him, 
you may send him messages. Messages must be addressed to him by player name, and must be signed with your player name, 
or Anonymous. A diplomatic message should be written on a 3x5 card, or written on a piece of paper and folded to 3x5 
size with the address (From and To) written on the OUTSIDE. Do NOT send messages SMALLER than 3x5 as they can easily 
get lost or delivered to the wrong player.

You may exchange addresses and/or phone numbers in diplomatic messages in order to contact each other directly. Please
 note that Flying Buffalo will NOT give you the name, address, or phone number of another player. If he wants you to 
 have it, he will have to give it to you himself.

You may tell each other about other players you have met. Once you have been told about a player, you may send messages 
to him. However you cannot make GIFTS to another player until you actually see his name on your printout.

Cross-game alliances, threats, vendettas, and agreements cannot be totally prevented, but are frowned upon and are 
considered unethical. Each game should be played separately for itself alone. Note that Diplomatic Messages will be 
delivered the following turn after they are received. (They will NOT be delivered between turns.) They should be 
included with your turn.

DO NOT try to sign some other player's name or code name to a diplomatic message. This is considered CHEATING, and if 
you are caught you will be thrown out of ALL your games.

 Table of Contents

27. THE PRINTOUT

Each turn you will get a computer printout of what you know currently in the game. The following is what will appear on 
the printouts (items marked with an asterisk may or may not appear on any given turn).

World Number
List of Connections
Owner of this world, [ ] if no owner
* Owner of converts: C[NAME]
The number of industry, metal, mines, population, population limit, Iships, and Pships at the world. (If industry is two
 numbers with a "/", then the first number is actual industry, and the second number is the amount of industry usable 
 this turn. If population is 25/5C for instance, that means that there are 25 population, of which 5 are converts. 
 If population is followed by an "R", that means they are robots.)
* If a PBB has been dropped at this world during the game so far, "BUSTED" will appear. If population (not robots) has 
died, "DEATHS=xx" will appear. If "Deaths" has two numbers, the one after the "/" is how many converts died. "Turns=" 
is the Turns number. If the world has been plundered so far this game, the word "Plunder=x" will appear with "x" being 
the number of times it has been plundered. If there are two numbers, the one after the "/" is how many turns before the 
world recovers from the plunder. "CG-Unloaded=x" tells you how many times Consumer Goods have been unloaded on this 
world. If the world was captured this turn, you are told who lost it and who captured it.
* You are told what artifacts are on the world (they belong to the owner of the world.)
* Next is a list of the fleets here. You are told the fleet number, who own it, how many ships are in the fleet, (how
 much cargo, if it is YOUR fleet), whether it is carrying a PBB, what artifacts it is carrying (an artifact that appears
  after a fleet number is being carried by the fleet and belongs to the player who owns that fleet), whether it dropped
   a PBB, made a robot attack, moved, unloaded consumer goods, or fired (and the target, if it fired).
* Lastly you are given a list of fleets that left here this turn, or passed through here this turn. You are told the 
fleet number and the owner, and the immediate destination (where it went from this world, not necessarily its final 
destination). You are not told how many ships or cargo it had. If you see the same fleet with two different 
destinations, that means it left here, came back again, and left in a different direction all in the same turn. 
This is a cheap way to get a probe of an extra world, as long as you don't get ambushed along the way!
In the example below, World 2 is adjacent to Worlds 24, 37, and 161. TERRAN owns the world and it has 1 industry, 2 
mines, 2 metal, 7 population, 10 maximum population, in two or more turns the number of mines will increase, there 
is one ISHP guarding the world, and that player JOVIAN moved his fleet #6 consisting of 1 ship into this world this 
turn. Also, Fleet #47 went from here to W161 this turn.
W2 (24,37,161) [TERRAN] (Industry=1, Mines=2, Metal=2, Population=7, Limit=10, Turns=2, IShip=1)
F6[JOVIAN]=1,Moved
F47[TERRAN]->W161
Each turn you will get a report from every world which you own, where you have fleets or converts or robots, or 
where you have probed. You also get a report on a world the turn it is captured from you, or the turn you leave 
it. And you always get a report on the world you started with (your homeworld). You are also told which players 
you have as allies, which players are currently your loaders, which players you have met so far in the game, and 
which players you currently see on your printout. The current scores of the players you see THIS TURN will be 
listed on your printout, but not necessarily in the order that the players appear. (The scores will be listed in 
numerical order from lowest to highest. The player names will be listed in random order. You will have to try to 
figure out which player has which score, if you can see more than one player on a turn.)
 Table of Contents

28. THE TURN SHEET. There are six spaces at the top of every turn sheet which are very important. You should fill 
them in before you do anything else.

The first space is labelled, STARWEB GAME #. This is your game number, and is the single most important space on 
the turn sheet. We are running many games of StarWeb simultaneously (usually well over 100) and we MUST know which 
game your turn sheet is for. The game number is the one which begins with "SW". If you put your account number, or 
the turn number, or some other number in the game number space, you may MISS YOUR TURN, as we may not be able to 
determine which game it is for.

The second space is the "TURN #". Please write the number that appears on your latest printout here. DO NOT ADD 
ONE TO THE TURN NUMBER. If you have received a printout that is labeled "Turn 5" then you should write "Turn 5" 
on the orders you are submitting, NOT "Turn 6".

The third space is labelled, "CODE NAME". This is your player name, the name that appears on all of your fleets 
and planets.

The fourth space is labelled, "ACCOUNT NUMBER". This is where you put your personal account number, which is 
confidential - don't tell anyone else what it is. (You have only one account even if you are playing in more 
than one game.)

The fifth space is labelled "DATE DUE". Please write in the date that is stamped on your printout as the due 
date. It may be helpful.

The sixth space says, "SIGNATURE". Here we want your REAL name. This is to make sure it is really you. And 
please make it readable. If you have accidentally written down the wrong game number, we MIGHT be able to 
figure out which game it is for, if we can read your signature.

About once a month we receive a turn sheet that has all of these spaces blank. If that's the case, it is highly unlikely 
that we will be able to figure out whose turn it is, and you will miss the turn.

Your turn will consist of a list of instructions, in any order you care to write them. If you list two orders which 
cannot both happen on the same turn (see "mutually exclusive orders"), whichever one we happen to type first will occur 
and the other will be ignored. This is the ONLY time the order in which you write your instructions will make a 
difference. Remember, all unloading and loading comes BEFORE movement in the game.

In the examples below, nnn or mmm is a world or fleet number, and qqq is a quantity. (To build 3 industry at world 205, 
order W205I3I.) Please note that if a number does not take up all three digits, DO NOT fill in the spaces with zeros. 
If you want fleet 5 to move to world 2, the order is F5W2, not F005W002 or F--5W--2.

TRANSFER SHIPS FROM PLACE TO PLACE

FnnnTqqqFmmm = transfers qqq ships from fleet nnn to fleet mmm
FnnnTqqqI or FnnnTqqqP = transfers qqq ships from fleet nnn to ISHPS or PSHIPS
InnnTqqqFmmm = transfers qqq ships from ISHIPS at world nnn to fleet mmm
PnnnTqqqFmmm = transfers qqq ships from PSHIPS at world nnn to fleet mmm
PnnnTqqqI or InnnTqqqP = transfers qqq ships from PSHIPS to ISHIPS or vice versa
MAKE NEW INDUSTRY OUT OF SHIPS
(This is the only way to get industry at a world which does not already have 5 industry, or 4 industry for an 
empire builder.)

WnnnSqqq = makes qqq new industry at world nnn by scrapping 6 ISHIPS each (or 4 ISHPS for an empire builder.)
BUILDING
WnnnBqqqI = build qqq ISHIPS at world nnn. (This order is actually not necessary as all industry not otherwise ordered 
will automatically build ISHPS.)
WnnnBqqqP = build qqq PSHIPS at world nnn
WnnnBqqqFmmm = build qqq ships and attach them to fleet mmm (fleet mmm must be at world nnn)
WnnnIqqqI = build qqq new industry (needs 5 metal and 5 industry for each one)
WnnnIqqqL = increase the population limit of world nnn by qqq (uses 5 industry and 5 metal).
WnnnBqqqR = build robots with qqq industry (makes twice that many robots). This order may only be given if the world is
 already populated with robots.
MIGRATING POPULATION
PnnnMqqqWmmm = moves qqq people or robots from world nnn to world mmm. Uses qqq industry and metal.
CnnnMqqqWmmm = moves qqq converts from world nnn to world mmm. Uses qqq industry and metal.
MOVE A FLEET ONE, TWO, OR THREE WORLDS
FnnnWmmm = move fleet nnn to world mmm.
FnnnWmmmWooo = move fleet nnn through world mmm to world ooo.
FnnnWmmmWoooWppp = move fleet nnn through worlds nnn and ooo to world ppp
TO PROBE AN ADJACENT WORLD
FnnnPmmm = uses 1 ship from fleet nnn to probe world mmm (happens before movement and fleet nnn can then move that turn)
InnnPmmm = uses an ISHIP at world nnn to probe world mmm
PnnnPmmm = uses a PSHIP at world nnn to probe world mmm
TRANSFER CARGO (qqq is how many metal)
FnnnU = unloads all the metal from fleet nnn onto the world where fleet nnn starts that turn.
FnnnUqqq = unload only qqq of the metal fleet nnn is carrying.
FnnnJ = jettisons (destroys) all the cargo that Fnnn is carrying.
FnnnJqqq = jettisons qqq cargo from fleet nnn.
FnnnN = unloads all the metal that fleet nnn is carrying as consumer goods.
FnnnNqqq = unload qqq metal as consumer goods
FnnnL = fleet nnn will pick up as much metal as it can carry.
FnnnLqqq = fleet nnn will pick up qqq metal.
TO HOOK AND UNHOOK ARTIFACTS FROM FLEETS
VnnnFmmm = attach artifact nnn to fleet mmm. (The fleet must either be owned by you, or by an artifact collector. 
The artifact must be on the world the fleet is currently located or, if Fmmm is owned by a collector, it can also be on 
a fleet at the world where Fmmm is located.)
VnnnW = drop the artifact nnn from the fleet carrying it, wherever it may be at the moment. Note that only one order 
per turn can be given for each artifact.
TO FIRE SHOTS FROM FLEETS, ISHPS, OR PSHIPS
FnnnAFmmm = fleet nnn fires at fleet mmm.
InnnAFmmm = ishps at world nnn fire at fleet mmm.
PnnnAFmmm = PSHPS at world mmm fire at fleet mmm.
FnnnAI = fleet nnn fires at ISHPS, and then industry.
FnnnAP = fleet nnn fires at PSHPS, and then population.
FnnnAH = fleet nnn fires at ISHPS and PSHPS, then tries to make the world go neutral.
InnnAC = ISHPS at world nnn fire at converts.
PnnnAC = PSHPS at world nnn fire at converts.
CONDITIONAL FIRE ORDERS
Exactly the same as fire orders, above, except replace the "A" in the above orders with a "C" for "conditional". 
Example:

FnnnCFmmm = fleet nnn fires at fleet mmm only of the owner of fleet mmm fires at you this turn at this world
AMBUSH CONTROL
Z = don't ambush anyone this turn anywhere (must be given every turn if you want it to stay in effect).
Znnn = don't ambush anyone this turn at world nnn.
ALLIANCES, JIHADS, AND GIFTS
A=xxxxxx = you are declaring player xxxxxx your ally.
N=xxxxxx = you are declaring player xxxxxx "not" your ally.
L=xxxxxx = you are declaring player xxxxxx a loader (he is allowed to pick up metal).
X=xxxxxx = you are declaring player xxxxxx "not" a loader.
J=xxxxxx = you are an Apostle declaring a jihad against player xxxxxx.
FnnnG=xxxxxx = you are giving fleet nnn to player xxxxxx.
WnnnG=xxxxxx = you are giving world nnn to player xxxxxx.
MISCELLANEOUS
WnnnX = you are plundering world nnn.
FnnnQ = you are putting fleet nnn "at peace".
FnnnX = you are putting fleet nnn "not at peace".
FnnnB = you are building a planet buster bomb with fleet nnn.
FnnnD = fleet nnn is dropping a PBB on the world below.
FnnnRqqq = you are a berserker converting qqq ships from fleet nnn into robots (1 ship = 2 robots) and they are landing 
on the world below. (Happens after the firing for that turn is finished.)
Please note that these are ALL the possible orders. Please do not write and ask us what the order is to do thus-and-so. 
If you cannot find it listed here, then it cannot be ordered.
 Table of Contents

29. MUTUALLY EXCLUSIVE ORDERS.

The following orders are mutually exclusive; a fleet given one of these orders cannot be given any of the other orders 
listed here on the same turn.

Firing
Moving
Making a robot attack
Ambushing
Being given away
Dropping a PBB
A conditional fire order IS a firing order, and is also mutually exclusive. Note that if you fire with the ISHPS or 
PSHPS of a world, you cannot give that world away or migrate population from that world.
 Table of Contents

30. VICTORY POINT TOTALS. On the first turn of your game, you should pick a number between 1000 and 10,000 (inclusive). 
Put it in the space at the bottom of the turn sheet marked "your choice for an ending score". We will take all the 
numbers given, and average them. We will not tell what this average is until the game is over. If you fail to give a 
number, we will not average in a "zero" for you, we just won't include you in the average.

As soon as at least one player has reached or exceeded this number, the game is over. At that time (after awarding 
bonuses for artifacts), the player with the most points wins. This way, you usually won't know for sure when the game 
is about to end. The average will probably be around 8,000 points or so, but you won't know for sure. You can tell 
other players what number you picked, or not, as you choose. (Or for that matter you can lie to them if you feel it 
necessary.)

Each turn you will be told your victory point total and the point total of all the players you can see this turn (you 
will not be told Which player has Which score. The final scores of each game and a rating system will be printed in our 
magazine, Flying Buffalo Quarterly, which comes out about four times a year. All players should either subscribe to 
this magazine or read a friend's copy, as it may have corrections, explanations, strategy notes, price increases, or 
procedure changes in it.

 Table of Contents

31. MISCELLANEOUS. The maximum # of mines for a world is 31. For all other quantities of items, the maximum is 255.

When filling out your turn sheet, be sure you PRINT your orders neatly. Do not use red ink, or a felt-tip pen, or a 
pencil when you write your orders. If we type in the wrong orders because we can't read your writing, we will not go 
back and correct it for you. Count the total number of orders that you have written and put that total in the 
"total orders" box on the turn sheet. This way, if we accidentally don't type one of you orders, we will notice it and 
go back and fix it before processing the game. If we make an error partly because you failed to include an order count, 
or you have an incorrect count, we won't fix the error later.


EMPIRE BUILDER

1 point/turn for each 10 population controlled.
1 point/turn for each MINE controlled.
1 point/turn for each Industry controlled.
Can build new industry with only 4 industry or scrapping 4 ISHPS.
MERCHANT
8 points/turn for each metal unloaded on world owned by another player. Points awarded only if Industry on world, and 
only up to twice the number of industry at that world. Not awarded for neutral worlds.
Points for unloading CGs on world (10 first time, 8 second time, 5 third time, 3 fourth time, 1 each time after that).
Ships can carry 2 metal each
PIRATE
Points for plundering a world (50 first time, 40 second time, 30 third time, 20 fourth time, 10 each time after that.
3 points for each key owned.
If a Pirate is at a world where he outnumbers all ships on all keys by more than 3 to 1, that Pirate captures all 
enemy fleets.
ARTIFACT COLLECTOR
Points for owning artifacts (see "Artifacts").
No points lost for owning Plastic Artifacts.
Other players can hook artifacts onto your fleets.
You (only) can transfer artifacts directly from one fleet to another.
500 points for each museum at the end of the game (world with 10 artifacts on it).
BERSERKER
2 points for each population you kill.
5 points/turn for each world owned that is populated by robots.
2 points/ship destroyed, if entire fleet destroyed.
200 points for dropping a PBB.
Berserker will capture a world if he drops robots on that world killing all population and leaving at least 1 robot.
1 robot kills 4 people; 4 people kill 1 robot. Fractions of robots lost are rounded up.
APOSTLE
One point per Martyr owned.
5 points/turn for each planet controlled.
Additional 5 points/turn for world populated entirely by converts.
1 point/turn for each 10 converts controlled.
Lose 1 point for each shot fired, unless on Jihad.
Each convert on world has 10% chance of converting one normal population each turn.
Each ship on fleet at world has 10% chance of converting one normal population each turn
An Apostle can declare Jihad. Under Jihad, no points are awarded for Martyrs, but no points are lost when firing at your 
Jihad enemy, and 2 points are awarded for each of his population you kill.
"""


class Owner:
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


class Merchant(Owner):
    def __init__(self):
        Owner.__init__(self, "Merchant", "blue")

    def pship_cost(self):
        return 8

    def iship_cost(self):
        return 16

    def pship_effectiveness(self):
        return 3

    def ship_effective_cargo(self):
        return 2


class Pirate(Owner):
    def __init__(self):
        Owner.__init__(self, "Pirate", "red")

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


class ArtifactCollector(Owner):
    def __init__(self):
        Owner.__init__(self, "Artifact Collector", "green")


class Berserker(Owner):
    def __init__(self):
        Owner.__init__(self, "Berserker", "yellow")


class Apostle(Owner):
    def __init__(self):
        Owner.__init__(self, "Apostle", "purple")


class EmpireBuilder(Owner):
    def __init__(self):
        Owner.__init__(self, "Empire Builder", "black")


class Player:
    def __init__(self, name, owner: Owner):
        self.name = name
        self.owner = owner
        self.home_world = None
        self.artifacts = []
        self.martyrs = []
        self.jihad = False
        self.jihad_enemy = None
        self.jihad_turns = 0
        self.score = 0


def parse_fleet_move(order, worlds, fleets):
    tokenize = order.split()
    if len(tokenize) != 4:
        raise ValueError("Invalid fleet move order")
    fleet_name = tokenize[0]
    world_name = tokenize[1]
    fleet = None
    for f in fleets:
        if f.name == fleet_name:
            fleet = f
            break
    if fleet is None:
        raise ValueError("Invalid fleet name")

    world = None
    for w in worlds:
        if w.name == world_name:
            world = w
            break
    if world is None:
        raise ValueError("Invalid world name")

    fleet.move_to(world)


class CharacterType:
    """
    Character types are the different types of players that can be in the game. Each character type has a different
    """

    def __init__(self, name, location, owner, description, greatest_treasure):
        self.name = name
        self.location = location
        self.owner = owner
        self.orders = []

    def move_to(self, world_of_fleet, worlds: [], fleets: []):
        if world_of_fleet in worlds:
            self.orders.append("M" + world_of_fleet.name)
        elif world_of_fleet in fleets:
            self.orders.append("M" + world_of_fleet.location.name)

    def process_orders(self, worlds: [], fleets: [], order_processing_dict=None):
        for order in self.orders:
            order_processing_dict[order[0]](order, worlds, fleets)


class Piece:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner


class Fleet(Piece):
    def __init__(self, name, location, owner, ships, cargo, ppb, artifacts, orders):
        super().__init__(name, location, owner)
        self.ships = ships
        self.cargo = cargo
        self.ppb = ppb
        self.artifacts = artifacts
        self.orders = orders


class World(Piece):
    def __init__(self, name, location, owner, neighbors, population, pships, industry, iships, metal, mines):
        super().__init__(name, location, owner)
        self.neighbors = neighbors
        self.population = population
        self.pships = pships
        self.industry = industry
        self.iships = iships
        self.metal = metal
        self.mines = mines

    def calculate_effective_population(self, fleets: []):
        """
        :param fleets:
        :return: effective population of world, including fleets with ships at this world and not "at peace"
        """
        effective_population = self.population + self.pships * self.owner.pship_effectiveness()
        fleet_suppression = calculate_fleet_suppression(self, fleets)
        return max(effective_population - fleet_suppression, 0)

    def calculate_effective_industry(self, fleets):
        """

        :param fleets:
        :return: effective industry of world, including fleets with ships at this world and not "at peace"
        """
        effective_industry = self.industry + self.iships * self.owner.iship_effectiveness()
        fleet_suppression = calculate_fleet_suppression(self, fleets)
        return max(effective_industry - fleet_suppression, 0)

    def is_neighbor(self, world):
        return world in self.neighbors

    def is_within_range(self, world, hops, max_hops=3):
        """

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


class Artifact(Piece):
    def __init__(self, name, location, owner, primary_name, secondary_name):
        super().__init__(name, location, owner)
        self.primary_name = primary_name
        self.secondary_name = secondary_name


def calculate_fleet_suppression(world, fleets):
    fleet_suppression = 0
    for fleet in fleets:
        if fleet.location == world and not fleet.at_peace and not fleet.owner == world.owner:
            fleet_suppression += fleet.ships * fleet.owner.ship_effectiveness()
        elif fleet.location == world and fleet.owner == world.owner:
            fleet_suppression -= fleet.ships * fleet.owner.ship_effectiveness()

    return fleet_suppression


import re

"""
FnnnTqqqFmmm = transfers qqq ships from fleet nnn to fleet mmm
FnnnTqqqI or FnnnTqqqP = transfers qqq ships from fleet nnn to ISHPS or PSHIPS
InnnTqqqFmmm = transfers qqq ships from ISHIPS at world nnn to fleet mmm
PnnnTqqqFmmm = transfers qqq ships from PSHIPS at world nnn to fleet mmm
PnnnTqqqI or InnnTqqqP = transfers qqq ships from PSHIPS to ISHIPS or vice versa
"""

transfer_n_ships_from_fleet_to_fleet = re.compile("F\d+T\d+F\d+")
transfer_n_ships_from_fleet_to_iships = re.compile("F\d+T\d+I")
transfer_n_ships_from_fleet_to_pships = re.compile("F\d+T\d+P")
transfer_n_iships_from_world_to_fleet = re.compile("I\d+T\d+F\d+")
transfer_n_pships_from_world_to_fleet = re.compile("P\d+T\d+F\d+")
transfer_n_pships_from_world_to_iships = re.compile("P\d+T\d+I")
transfer_n_iships_from_world_to_pships = re.compile("I\d+T\d+P")

transfer_orders = [transfer_n_ships_from_fleet_to_fleet, transfer_n_ships_from_fleet_to_iships,
                   transfer_n_ships_from_fleet_to_pships, transfer_n_iships_from_world_to_fleet,
                   transfer_n_pships_from_world_to_fleet, transfer_n_pships_from_world_to_iships,
                   transfer_n_iships_from_world_to_pships]

"""
WnnnBqqqI = build qqq ISHIPS at world nnn. (This order is actually not necessary as all industry not otherwise ordered will automatically build ISHPS.)
WnnnBqqqP = build qqq PSHIPS at world nnn
WnnnBqqqFmmm = build qqq ships and attach them to fleet mmm (fleet mmm must be at world nnn)
WnnnIqqqI = build qqq new industry (needs 5 metal and 5 industry for each one)
WnnnIqqqL = increase the population limit of world nnn by qqq (uses 5 industry and 5 metal).
WnnnBqqqR = build robots with qqq industry (makes twice that many robots). This order may only be given if the world is already populated with robots.
"""

build_n_iships_at_world = re.compile("W\d+B\d+I")
build_n_pships_at_world = re.compile("W\d+B\d+P")
build_n_ships_and_attach_to_fleet = re.compile("W\d+B\d+F\d+")
build_n_industry_at_world = re.compile("W\d+I\d+I")
build_n_population_limit_at_world = re.compile("W\d+I\d+L")
build_n_robots_at_world = re.compile("W\d+B\d+R")

build_orders = [build_n_iships_at_world, build_n_pships_at_world, build_n_ships_and_attach_to_fleet,
                build_n_industry_at_world, build_n_population_limit_at_world, build_n_robots_at_world]

"""
PnnnMqqqWmmm = moves qqq people or robots from world nnn to world mmm. Uses qqq industry and metal.
CnnnMqqqWmmm = moves qqq converts from world nnn to world mmm. Uses qqq industry and metal.
"""

move_n_people_from_world_to_world = re.compile("P\d+M\d+W\d+")
move_n_converts_from_world_to_world = re.compile("C\d+M\d+W\d+")

move_orders = [move_n_people_from_world_to_world, move_n_converts_from_world_to_world]

"""
FnnnWmmm = move fleet nnn to world mmm.
FnnnWmmmWooo = move fleet nnn through world mmm to world ooo.
FnnnWmmmWoooWppp = move fleet nnn through worlds nnn and ooo to world ppp
"""

move_fleet_to_world = re.compile("F\d+W\d+")
move_fleet_through_worlds = re.compile("F\d+W\d+W\d+")
move_fleet_through_worlds = re.compile("F\d+W\d+W\d+W\d+")

fleet_move_orders = [move_fleet_to_world, move_fleet_through_worlds, move_fleet_through_worlds]

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
VnnnFmmm = attach artifact nnn to fleet mmm. (The fleet must either be owned by you, or by an artifact collector. The artifact must be on the world the fleet is currently located or, if Fmmm is owned by a collector, it can also be on a fleet at the world where Fmmm is located.)
VnnnW = drop the artifact nnn from the fleet carrying it, wherever it may be at the moment. Note that only one order per turn can be given for each artifact.
"""
artifact_attach_to_fleet = re.compile("V\d+F\d+")
artifact_drop_from_fleet = re.compile("V\d+W")

artifact_orders = [artifact_attach_to_fleet, artifact_drop_from_fleet]

"""
FnnnAFmmm = fleet nnn fires at fleet mmm.
InnnAFmmm = ishps at world nnn fire at fleet mmm.
PnnnAFmmm = PSHPS at world mmm fire at fleet mmm.
FnnnAI = fleet nnn fires at ISHPS, and then industry.
FnnnAP = fleet nnn fires at PSHPS, and then population.
FnnnAH = fleet nnn fires at ISHPS and PSHPS, then tries to make the world go neutral.
InnnAC = ISHPS at world nnn fire at converts.
PnnnAC = PSHPS at world nnn fire at converts.
"""
fire_at_fleet = re.compile("F\d+A[FIPHC]")
iships_fire_at_fleet = re.compile("I\d+A[FIPHC]")
pships_fire_at_fleet = re.compile("P\d+A[FIPHC]")
fire_at_iships_then_industry = re.compile("F\d+AI")
fire_at_pships_then_population = re.compile("F\d+AP")
fire_at_iships_and_pships_then_try_to_make_world_neutral = re.compile("F\d+AH")
iships_fire_at_converts = re.compile("I\d+AC")
pships_fire_at_converts = re.compile("P\d+AC")

fire_orders = [fire_at_fleet, iships_fire_at_fleet, pships_fire_at_fleet, fire_at_iships_then_industry,
               fire_at_pships_then_population, fire_at_iships_and_pships_then_try_to_make_world_neutral,
               iships_fire_at_converts, pships_fire_at_converts]

"""
FnnnCFmmm = fleet nnn fires at fleet mmm only of the owner of fleet mmm fires at you this turn at this world
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
build_pships_at_world = re.compile(r'P(\d+)B(\d+)')


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
