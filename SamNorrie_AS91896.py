driver_index = {
    "lando norris": {
        "team": "Mclaren",
        "elo": 2675,
    },
    "oscar piastri": {
        "team": "Mclaren",
        "elo": 2565,
    },
    "charles leclerc": { 
        "team": "Ferrari", 
        "elo": 2640,
    },
    "lewis hamilton": {
        "team": "Ferrari",
        "elo": 2480,
    }, 
    "max verstappen": {
        "team": "Red Bull",
        "elo": 2810,
    },
    "yuki tsundoa": {
        "team": "Red Bull",
        "elo": 2305,
    },
    "george russell": {
        "team": "Mercedes",
        "elo": 2525,
    },
    "kimi antonelli": {
        "team": "Mercedes",
        "elo": 1800,
    },
    "fernando alonso": {
        "team": "Aston Martin",
        "elo": 2420,
    },
    "lance stroll": {
        "team": "Aston Martin",
        "elo": 2270,
    },
    "pierre gasly": {
        "team": "Alpine",
        "elo": 2385,
    },
    "franco colapinto": {
        "team": "Alpine",
        "elo": 2060,
    },
    "esteban ocon": {
        "team": "Haas",
        "elo": 2235,
    },
    "oliver bearman": {
        "team": "Haas",
        "elo": 2095,
    },
    "liam lawson": {
        "team": "Racing Bulls",
        "elo": 1990,
    },
    "isack hadjar": {
        "team": "Racing Bulls",
        "elo": 1800,
    },
    "carlos sainz": {
        "team": "Williams",
        "elo": 2540,
    },
    "alexander albon": {
        "team": "Williams",
        "elo": 2165,
    },
    "nico hulkenberg": {
        "team": "Kick Sauber",
        "elo": 2350,
    },
    "gabriel bortoleto": {
        "team": "Kick Sauber",
        "elo": 1800,
    },
}




print("Hello, this is an F1 ELO system.\n")

while True:
    print("\nWould you like to:")
    print("- Look at ELO")
    print("- Update ELO")
    print("- Simulate race")
    print("- Quit")
    
    reason_of_run = input("Answer: ").strip().lower()

    if reason_of_run == "look at elo":
        print("\nCurrent ELO ratings for all F1 drivers:\n")
        for driver, info in driver_index.items():
            print("{}: {}".format(driver.title(), info['elo']))
    
    elif reason_of_run == "update elo":
        print("\nFeature coming soon: Update ELO.")
        mclaren_rvp = int(input("What is the RVP of Mclaren(The distance in seconds between them and the fastest lap of the slowest team)")+1)
    elif reason_of_run == "simulate race":
        print("\nFeature coming soon: Simulate race.")
    
    elif reason_of_run == "quit":
        print("Thank you for using this program!")
        break

    else:
        print("Invalid option. Please try again.")
    