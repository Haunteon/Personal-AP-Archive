# Movement
## High Jump (Need one)
- Triple Jump
- Back Flip
- Side Flip
- Ground Pound and Ground Pound Jump
## Momentum (Need one)
- Long Jump
- Roll
- Dive
## Cap Vault (Need Both)
- Dive
- Cap Jump
# NPC
## Tourist (Steps must be done in order)
- Begin: Defeat Knucklotec
- Metro: Complete Festival
- Cascade:
- Luncheon: Defeat Cookatiel
- Moon: Defeat Bowser
- Mushroom:
- Sand: 
## Princess Peach (Steps must be done in order)
- Begin: Talk with Toad in Mushroom Kingdom (Story pillar of light)
- Moon: Speak with Peach in all previous Kingdoms
- Mushroom: Speak with Peach in Moon Kingdom
# Sand Kingdom
## Pyramid Skip (Need one)
- Bullet Bill
- **Cap Vault** and (Long Jump or Triple Jump)
# Lake Kingdom
## Into the Lake (Need one)
- Zipper and Swim
- **Cap Vault** and (High Jump or Long Jump or (Triple Jump and Wall Jump))
- Cap Jump and Triple Jump and Wall Jump and Goomba
## Above the Lake (Need one)
- Cheep Cheep
- Swim
- **Cap Vault**
# Wooded Kingdom
## Maze Skip (Need one)
- Uproot
- **Cap Vault**
## To the Wall (Need one)
- Hold/Throw
- **Cap Vault** and **High Jump**
- Uproot and Dive
## Sherm Wall (Need one and To the Wall)
- Sherm
- Goomba and Wall Jump and Dive
# Lost Kingdom
## View of Lost (Need Both)
- Ground Pound
- Wall Jump
# Snow Kingdom
## After Gusty Barrier
-
  },
  {
    "name": "Get to Cheese",
	"region": "Luncheon Kingdom Post Spewart",
    "requires": "{OptAll(|Lava Bubble| or (|Dive| and (|Triple Jump| or |Cap Jump| or (|Ground Pound| and |Ground Pound Jump|))))}",
    "visible": false
  },
  {
    "name": "Get to Meat",
	"region": "Luncheon Kingdom Post Cheese",
    "requires": "{OptAll(|Volbonan| or ((|High Jump| or |Spin|) and (|Wall Jump| and |Dive|)) or (|High Jump| and (|Cap Jump| or (|Cap Jump| and |Dive|))))}",
    "visible": false
  },
  {
    "name": "Enter the Courtyard",
	"region": "Bowser Kingdom 1st Visit",
    "requires": "{OptAll(|Pokio| or (|Dive| and (|Back Flip| or |Wall Jump| or (|Ground Pound Jump| and |Ground Pound|))))}",
    "visible": false
  },
  {
    "name": "Over the Moat",
	"region": "Bowser Kingdom Courtyards",
    "requires": "{OptAll(|Pokio| or (|High Jump| and |Dive| and |Cap Jump|) or ({YamlEnabled(easy_trick_jumps)} and |Dive| and |Cap Jump|))}",
    "visible": false
  },
  {
    "name": "Parabones Skip",
	"region": "Moon Kingdom 1st Visit",
    "requires": "{OptAll(|Parabones| or (|Dive| and |Cap Jump| and (|Long Jump| or |Triple Jump|)))}",
    "visible": false
  },
  {
    "name": "Moon Cave Gauntlet",
	"region": "Moon Kingdom 1st Visit",
    "requires": "{OptAll(|Parabones Skip| and |Banzai Bill| and |Spark Pylon|)}",
    "visible": false
  },
  {
    "name": "Moon Cave Skip",
	"region": "Moon Kingdom 1st Visit",
    "requires": "{YamlEnabled(moon_cave_skip)} and {OptAll(|Cap Jump| and |Wall Jump| and (|Back Flip| or (|Ground Pound| and |Ground Pound Jump|)))}",
    "visible": false
  },
  {
	"name": "Tourist 1",
	"copy_location": "A Tourist in the Metro Kingdom!",
    "visible": false
  },
  {
	"name": "Tourist 2",
	"copy_location": "A Tourist in the Cascade Kingdom!",
    "visible": false
  },
  {
	"name": "Tourist 3",
	"copy_location": "A Tourist in the Luncheon Kingdom!",
    "visible": false
  },
  {
	"name": "Tourist 4",
	"copy_location": "A Tourist in the Moon Kingdom!",
    "visible": false
  },
  {
	"name": "Tourist 5",
	"copy_location": "A Tourist in the Mushroom Kingdom!",
    "visible": false
  },
  {
	"name": "Peach Cap",
	"copy_location": "Peach in the Cap Kingdom",
    "visible": false
  },
  {
	"name": "Peach Cascade",
	"copy_location": "Peach in the Cascade Kingdom",
    "visible": false
  },
  {
	"name": "Peach Sand",
	"copy_location": "Peach in the Sand Kingdom",
    "visible": false
  },
  {
	"name": "Peach Lake",
	"copy_location": "Peach in the Lake Kingdom",
    "visible": false
  },
  {
	"name": "Peach Wooded",
	"copy_location": "Peach in the Wooded Kingdom",
    "visible": false
  },
  {
	"name": "Peach Cloud",
	"copy_location": "Peach in the Cloud Kingdom",
    "visible": false
  },
  {
	"name": "Peach Lost",
	"copy_location": "Peach in the Lost Kingdom",
    "visible": false
  },
  {
	"name": "Peach Metro",
	"copy_location": "Peach in the Metro Kingdom",
    "visible": false
  },
  {
	"name": "Peach Snow",
	"copy_location": "Peach in the Snow Kingdom",
    "visible": false
  },
  {
	"name": "Peach Seaside",
	"copy_location": "Peach in the Seaside Kingdom",
    "visible": false
  },
  {
	"name": "Peach Luncheon",
	"copy_location": "Peach in the Luncheon Kingdom",
    "visible": false
  },
  {
	"name": "Peach Ruined",
	"copy_location": "Peach in the Ruined Kingdom",
    "visible": false
  },{
	"name": "Peach Bowser",
	"copy_location": "Peach in Bowser's Kingdom",
    "visible": false
  },
  {
	"name": "Peach Moon",
	"requires": "|Peach Cap| and |Peach Cascade| and |Peach Sand| and |Peach Lake| and |Peach Wooded| and |Peach Cloud| and |Peach Lost| and |Peach Metro| and |Peach Snow| and |Peach Seaside| and |Peach Luncheon| and |Peach Ruined| and |Peach Bowser|",
    "visible": false
  },
  {
	"name": "Peach Mushroom",
	"requires": "|Peach Moon|",
    "visible": false
  },
  {
	"name" : "Goal 1",
	"copy_location": "A Traditional Festival!",
	"visible": false
  },
  {
	"name" : "Goal 2",
	"copy_location": "Rescue Princess Peach",
	"visible": false
  },
  {
	"name" : "Goal 3",
	"copy_location": "Achieve World Peace",
	"visible": false
  },
  {
	"name" : "Goal 4",
	"copy_location": "Long Journey's End",
	"visible": false
  },
  {
	"name": "Post Game",
	"copy_location": "Rescue Princess Peach",
    "visible": false# Sand Kingdom

# Moon Kingdom
## Parabones Skip
- Parabones
- Dive and Cap Jump and (Long Jump or Triple Jump)
## Moon Cave Gauntlet
- Parabones Skip
- Banzai Bill
- Spark Pylon (Starting Inv)
## Moon Cave Skip
- Back Flip or Ground Pound Jump (+ Ground Pound)
- Cap Jump
- Wall Jump
