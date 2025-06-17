import math
# Index of drivers names, team and base elo
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
# Acts as a loop so that the user can do multiple functions, has a quit option for easy acess
while True:
    print("\nWould you like to:")
    print("- Look at ELO")
    print("- Update ELO")
    print("- Simulate race")
    print("- Quit")
    # Finds reason of run to apply to if statement 
    reason_of_run = input("Answer: ").strip().lower()
    #Outputs all base elos of the drivers 
    if reason_of_run == "look at elo":
        print("\nCurrent ELO ratings for all F1 drivers:\n")
        for driver, info in driver_index.items():
            print("{}: {}".format(driver.title(), info['elo']))
    
    elif reason_of_run == "update elo":
        print("\nFeature coming soon: Update ELO.")
    # gets RVP and applys it to every driver, orders them for a 'simulated race result'   
    elif reason_of_run == "simulate race":
        # Get RVP for each team which will be used to find the race elo of each driver based on their teams RVP
        try:
            # Mclaren
            mclaren_performance_percent = float(input("Enter Mclaren's performance as a percentage of the fastest team (e.g. 102): "))
            mclaren_away_from_fast_team = mclaren_performance_percent - 100
            mclaren_rvp = 100 - mclaren_away_from_fast_team 
            print("Mclaren's RVP (performance compared to fastest team) is: {:.2f}%".format(mclaren_rvp))

            # Ferrari
            ferrari_performance_percent = float(input("Enter Ferrari's performance as a percentage of the fastest team (e.g. 102): "))
            ferrari_away_from_fast_team = ferrari_performance_percent - 100
            ferrari_rvp = 100 - ferrari_away_from_fast_team 
            print("Ferrari's RVP (performance compared to fastest team) is: {:.2f}%".format(ferrari_rvp))

            # Red Bull
            redbull_performance_percent = float(input("Enter Red Bull's performance as a percentage of the fastest team (e.g. 102): "))
            redbull_away_from_fast_team = redbull_performance_percent - 100
            redbull_rvp = 100 - redbull_away_from_fast_team 
            print("Red Bull's RVP (performance compared to fastest team) is: {:.2f}%".format(redbull_rvp))

            # Mercedes
            mercedes_performance_percent = float(input("Enter Mercedes's performance as a percentage of the fastest team (e.g. 102): "))
            mercedes_away_from_fast_team = mercedes_performance_percent - 100
            mercedes_rvp = 100 - mercedes_away_from_fast_team 
            print("Mercedes's RVP (performance compared to fastest team) is: {:.2f}%".format(mercedes_rvp))

            # Aston Martin
            astonmartin_performance_percent = float(input("Enter Aston Martin's performance as a percentage of the fastest team (e.g. 102): "))
            astonmartin_away_from_fast_team = astonmartin_performance_percent - 100
            astonmartin_rvp = 100 - astonmartin_away_from_fast_team 
            print("Aston Martin's RVP (performance compared to fastest team) is: {:.2f}%".format(astonmartin_rvp))

            # Alpine
            alpine_performance_percent = float(input("Enter Alpine's performance as a percentage of the fastest team (e.g. 102): "))
            alpine_away_from_fast_team = alpine_performance_percent - 100
            alpine_rvp = 100 - alpine_away_from_fast_team 
            print("Alpine's RVP (performance compared to fastest team) is: {:.2f}%".format(alpine_rvp))

            # Haas
            haas_performance_percent = float(input("Enter Haas's performance as a percentage of the fastest team (e.g. 102): "))
            haas_away_from_fast_team = haas_performance_percent - 100
            haas_rvp = 100 - haas_away_from_fast_team 
            print("Haas's RVP (performance compared to fastest team) is: {:.2f}%".format(haas_rvp))

            # Racing Bulls
            racingbulls_performance_percent = float(input("Enter Racing Bulls's performance as a percentage of the fastest team (e.g. 102): "))
            racingbulls_away_from_fast_team = racingbulls_performance_percent - 100
            racingbulls_rvp = 100 - racingbulls_away_from_fast_team
            print("Racing Bulls's RVP (performance compared to fastest team) is: {:.2f}%".format(racingbulls_rvp))

            # Williams
            williams_performance_percent = float(input("Enter Williams's performance as a percentage of the fastest team (e.g. 102): "))
            williams_away_from_fast_team = williams_performance_percent - 100
            williams_rvp = 100 - williams_away_from_fast_team 
            print("Williams's RVP (performance compared to fastest team) is: {:.2f}%".format(williams_rvp))

            # Kick Sauber
            kicksauber_performance_percent = float(input("Enter Kick Sauber's performance as a percentage of the fastest team (e.g. 102): "))
            kicksauber_away_from_fast_team = kicksauber_performance_percent - 100
            kicksauber_rvp = 100 - kicksauber_away_from_fast_team
            print("Kick Sauber's RVP (performance compared to fastest team) is: {:.2f}%".format(kicksauber_rvp))

            team_rvps = {
                "Mclaren": mclaren_rvp,
                "Ferrari": ferrari_rvp,
                "Red Bull": redbull_rvp,
                "Mercedes": mercedes_rvp,
                "Aston Martin": astonmartin_rvp,
                "Alpine": alpine_rvp,
                "Haas": haas_rvp,
                "Racing Bulls": racingbulls_rvp,
                "Williams": williams_rvp,
                "Kick Sauber": kicksauber_rvp,
            }
            #Update the drivers base elo for their ELO in the race that is simulated 
            for driver, info in driver_index.items():
                team = info["team"]
                rvp = team_rvps.get(team, 100)
                driver_elo = info["elo"]
                
                driver_race_elo = driver_elo * ((rvp/100) ** 60)
                print(driver.title(), driver_race_elo)
        except ValueError:
            print("Please enter a valid number (e.g. 96.5).")
    elif reason_of_run == "quit":
        print("Thank you for using this program!")
        break

    else:
        print("Invalid option. Please try again.")
    