# World of Tanks - API (PC Europe)

### 1. Description
This package will extract data from the Wargaming World of Tanks API.      
Currently, this works only for the PC version on EU region with the rest of the regions and platforms to be implemented at a later date.

The package will require the following from the official [World of Tanks Developer API](https://developers.wargaming.net/) page.
* application id
* account id
* access token

All data extracted will be written to a local sqlite database ready to be accessed.

### 2. Install

```
pip install worldoftanks
```

### 3. Usage

```
from worldoftanks import WotAPI

wot = WotAPI(application_id='############',
             account_id='##########',
             token='#########')

# Create the local database
wot.db_init()

# Extract Account Data
wot.player_personal()
wot.player_vehicles()
wot.player_achievements()

# Extract Tankopedia Data
wot.tankopedia_vehicles(load_once=True)
wot.tankopedia_achievements(load_once=True)
wot.tankopedia_information(load_once=True)
wot.tankopedia_maps(load_once=True)
```

The data can be accessed from the ```wot``` objects for further development processed

### 4. Left ToDo

- Accounts   
	- [✓] player_personal_data
	- [✓] player_vehicles
	- [✓] player_achievements (no token required)

- Tankopedia
	- [✓] vehicles (no token required)
	- [✓] achivements (no token required)
	- [✓] tankopedia_information (no token required)
	- [✓] maps (no token required)
	- badges (no token required)

- Vehicles Statistics
	- vehicle_statistics
	- vehicle_achievements