from worldoftanks import WotAPI

wot = WotAPI(application_id='e910e3cc48a27aa6879313c637b41f8c',
             account_id='1004400332',
             realm='com')
wot.player_personal()
wot.player_vehicles()
wot.player_achievements()

# Extract Tankopedia Data
wot.tankopedia_vehicles(load_once=True)
wot.tankopedia_achievements(load_once=True)
wot.tankopedia_information(load_once=True)
wot.tankopedia_maps(load_once=True)
wot.tankopedia_badges(load_once=True)

# Extract Player Vehicles Data
wot.vehicle_achievements()
