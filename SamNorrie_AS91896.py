import math
# Index of drivers names, team and base elo


driver_index = {
    "lando norris": {
        "team": "Mclaren",
        "elo": 2675,
    },
    "oscar piastri": {
        "team": "Mclaren",
        "elo": 2530,
    },
    "charles leclerc": { 
        "team": "Ferrari", 
        "elo": 2665,
    },
    "lewis hamilton": {
        "team": "Ferrari",
        "elo": 2485,
    }, 
    "max verstappen": {
        "team": "Red Bull",
        "elo": 2780,
    },
    "yuki tsunoda": {
        "team": "Red Bull",
        "elo": 1955,
    },
    "george russell": {
        "team": "Mercedes",
        "elo": 2505,
    },
    "kimi antonelli": {
        "team": "Mercedes",
        "elo": 1715,
    },
    "fernando alonso": {
        "team": "Aston Martin",
        "elo": 2350,
    },
    "lance stroll": {
        "team": "Aston Martin",
        "elo": 2200,
    },
    "pierre gasly": {
        "team": "Alpine",
        "elo": 2280,
    },
    "franco colapinto": {
        "team": "Alpine",
        "elo": 2095,
    },
    "esteban ocon": {
        "team": "Haas",
        "elo": 2465,
    },
    "oliver bearman": {
        "team": "Haas",
        "elo": 2315,
    },
    "liam lawson": {
        "team": "Racing Bulls",
        "elo": 1945,
    },
    "isack hadjar": {
        "team": "Racing Bulls",
        "elo": 1970,
    },
    "carlos sainz": {
        "team": "Williams",
        "elo": 2360,
    },
    "alexander albon": {
        "team": "Williams",
        "elo": 2155,
    },
    "nico hulkenberg": {
        "team": "Kick Sauber",
        "elo": 2620,
    },
    "gabriel bortoleto": {
        "team": "Kick Sauber",
        "elo": 1980,
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
    # Update Elo Function
    elif reason_of_run == "update elo":
        try:
            player_input = False
            # Loop until all teams have an rvp 
            while player_input == False:
                # Mclaren
                mclaren_performance_percent = float(input("Enter Mclaren's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if mclaren_performance_percent > 107: 
                    print("This is an incorrect value")
                elif  mclaren_performance_percent < 100: 
                    print("This is an incorrect value")
                else:
                    mclaren_away_from_fast_team = mclaren_performance_percent - 100
                    mclaren_rvp = 100 - mclaren_away_from_fast_team 
                    print("Mclaren's RVP (performance compared to fastest team) is: {:.2f}%".format(mclaren_rvp))
                    print("")
                    player_input = True

                # Ferrari
                ferrari_performance_percent = float(input("Enter Ferrari's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if ferrari_performance_percent > 107:
                    print("This is an incorrect value")
                elif ferrari_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    ferrari_away_from_fast_team = ferrari_performance_percent - 100
                    ferrari_rvp = 100 - ferrari_away_from_fast_team 
                    print("Ferrari's RVP (performance compared to fastest team) is: {:.2f}%".format(ferrari_rvp))
                    print("")
                    player_input = True 

                # Red Bull     
                redbull_performance_percent = float(input("Enter Red Bull's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if redbull_performance_percent > 107: 
                    print("This is an incorrect value")
                elif redbull_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    redbull_away_from_fast_team = redbull_performance_percent - 100
                    redbull_rvp = 100 - redbull_away_from_fast_team 
                    print("Red Bull's RVP (performance compared to fastest team) is: {:.2f}%".format(redbull_rvp))
                    print("")
                    player_input = True

                # Mercedes
                mercedes_performance_percent = float(input("Enter Mercedes's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if mercedes_performance_percent > 107:
                    print("This is an incorrect value")
                elif mercedes_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    mercedes_away_from_fast_team = mercedes_performance_percent - 100
                    mercedes_rvp = 100 - mercedes_away_from_fast_team 
                    print("Mercedes's RVP (performance compared to fastest team) is: {:.2f}%".format(mercedes_rvp))
                    print("")
                    player_input = True 


                # Aston Martin
                astonmartin_performance_percent = float(input("Enter Aston Martin's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if astonmartin_performance_percent > 107:
                     print("This is an incorrect value")
                elif astonmartin_performance_percent < 100: 
                     print("This is an incorrect value")
                else:   
                    astonmartin_away_from_fast_team = astonmartin_performance_percent - 100
                    astonmartin_rvp = 100 - astonmartin_away_from_fast_team 
                    print("Aston Martin's RVP (performance compared to fastest team) is: {:.2f}%".format(astonmartin_rvp))
                    print("")
                    player_input = True

                # Alpine
                alpine_performance_percent = float(input("Enter Alpine's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if alpine_performance_percent > 107:
                    print("This is an incorrect value")
                elif alpine_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    alpine_away_from_fast_team = alpine_performance_percent - 100
                    alpine_rvp = 100 - alpine_away_from_fast_team 
                    print("Alpine's RVP (performance compared to fastest team) is: {:.2f}%".format(alpine_rvp))
                    print("")
                    player_input = True 

                # Haas
                haas_performance_percent = float(input("Enter Haas's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if haas_performance_percent > 107:
                     print("This is an incorrect value")
                elif haas_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    haas_away_from_fast_team = haas_performance_percent - 100
                    haas_rvp = 100 - haas_away_from_fast_team 
                    print("Haas's RVP (performance compared to fastest team) is: {:.2f}%".format(haas_rvp))
                    print("")
                    player_input = True 

                # Racing Bulls
                racingbulls_performance_percent = float(input("Enter Racing Bulls's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if racingbulls_performance_percent > 107:
                     print("This is an incorrect value")
                elif racingbulls_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    racingbulls_away_from_fast_team = racingbulls_performance_percent - 100
                    racingbulls_rvp = 100 - racingbulls_away_from_fast_team
                    print("Racing Bulls's RVP (performance compared to fastest team) is: {:.2f}%".format(racingbulls_rvp))
                    print("")
                    player_input = True 

                # Williams
                williams_performance_percent = float(input("Enter Williams's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximumn due to F1 regulations is 107): "))
                if williams_performance_percent > 107: 
                     print("This is an incorrect value")
                elif racingbulls_performance_percent < 100: 
                     print("This is an incorrect value")
                else:
                    williams_away_from_fast_team = williams_performance_percent - 100
                    williams_rvp = 100 - williams_away_from_fast_team 
                    print("Williams's RVP (performance compared to fastest team) is: {:.2f}%".format(williams_rvp))
                    print("")
                    player_input = True

                # Kick Sauber
                kicksauber_performance_percent = float(input("Enter Kick Sauber's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximumn due to F1 regulations is 107): "))
                if kicksauber_performance_percent > 107:
                     print("This is an incorrect value")
                elif kicksauber_performance_percent < 100:
                     print("This is an incorrect value")
                else: 
                    kicksauber_away_from_fast_team = kicksauber_performance_percent - 100
                    kicksauber_rvp = 100 - kicksauber_away_from_fast_team
                    print("Kick Sauber's RVP (performance compared to fastest team) is: {:.2f}%".format(kicksauber_rvp))
                    print("")
                    player_input = True
            # Stores RVPs
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
            driver_race_elos = []
            for driver, info in driver_index.items():
                team = info["team"]
                rvp = team_rvps.get(team, 100)
                driver_elo = info["elo"]
             #Makes driver race elo which is a combination of the cars performance and the drivers skill 
                driver_race_elo = driver_elo * ((rvp/100) ** 60)
             #Sorts the driver elo from highest to lowest     
                driver_race_elos.append((driver.title(), driver_race_elo))
            driver_race_elos.sort(key=lambda x: x[1], reverse=True)
            
            # Prints all dirver elos in order 
            print("\nExpected Race Results based on Race Elo\n")

            # Assign expected finishing positions
            driver_race_results = []
            for i, (driver, elo) in enumerate(driver_race_elos, start=1):
                print("P{}: {} ({:.0f})".format(i, driver, elo))
                driver_race_results.append({
                "name": driver,
                "race_elo": elo,
                "expected_position": i
                })
            print("")
            # Gets user to input actual driver results 
            p1 = input("Who got P1")
            p2 = input("Who got P2")
            p3 = input("Who got P3")
            p4 = input("Who got P4")
            p5 = input("Who got P5")
            p6 = input("Who got P6")
            p7 = input("Who got P7")
            p8 = input("Who got P8")
            p9 = input("Who got P9")
            p10 = input("Who got P10")
            p11 = input("Who got P11")
            p12 = input("Who got P12")
            p13 = input("Who got P13")
            p14 = input("Who got P14")
            p15 = input("Who got P15")
            p16 = input("Who got P16")
            p17 = input("Who got P17")
            p18 = input("Who got P18")
            p19 = input("Who got P19")
            p20 = input("Who got P20")

            # K Factor (Elo Change Intensity)
            k_factor = 5 
            # Map actual positions
            actual_results = [
            p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
            p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
            ]
            actual_position_map = {name.lower(): pos + 1 for pos, name in enumerate(actual_results)}
            # Update driver ELOs
            for driver_result in driver_race_results:
                driver_name = driver_result["name"].lower()
                expected_position = driver_result["expected_position"]
                actual_position = actual_position_map.get(driver_name)

                if actual_position is None:
                    print(f"Warning: {driver_name} not found in actual results.")
                    continue
                # Calculations for the change of the ELO 
                postion_difference = expected_position - actual_position
                elo_change = postion_difference * k_factor

                # Update in driver_index
                old_elo = driver_index[driver_name]['elo']
                new_elo = old_elo + elo_change
                driver_index[driver_name]['elo'] = round(new_elo)
                # Output of new ElO 
                print("{}: Expected P{}, Actual P{}, ELO change: {:+.1f}, New ELO: {}".format(driver_name.title(), expected_position, actual_position, elo_change, round(new_elo)))




        # Stops code if there is a wrong value
        except ValueError:
            print("Please enter a valid number (e.g. 101).")

    # gets RVP and applys it to every driver, orders them for a 'simulated race result'   
    elif reason_of_run == "simulate race":
        # Get RVP for each team which will be used to find the race elo of each driver based on their teams RVP
        try:
            player_input = False
            
            while player_input == False:
                # Mclaren
                mclaren_performance_percent = float(input("Enter Mclaren's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if mclaren_performance_percent > 107: 
                    print("This is an incorrect value")
                elif  mclaren_performance_percent < 100: 
                    print("This is an incorrect value")
                else:
                    mclaren_away_from_fast_team = mclaren_performance_percent - 100
                    mclaren_rvp = 100 - mclaren_away_from_fast_team 
                    print("Mclaren's RVP (performance compared to fastest team) is: {:.2f}%".format(mclaren_rvp))
                    print("")
                    player_input = True

                # Ferrari
                ferrari_performance_percent = float(input("Enter Ferrari's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if ferrari_performance_percent > 107:
                    print("This is an incorrect value")
                elif ferrari_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    ferrari_away_from_fast_team = ferrari_performance_percent - 100
                    ferrari_rvp = 100 - ferrari_away_from_fast_team 
                    print("Ferrari's RVP (performance compared to fastest team) is: {:.2f}%".format(ferrari_rvp))
                    print("")
                    player_input = True 

                # Red Bull     
                redbull_performance_percent = float(input("Enter Red Bull's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if redbull_performance_percent > 107: 
                    print("This is an incorrect value")
                elif redbull_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    redbull_away_from_fast_team = redbull_performance_percent - 100
                    redbull_rvp = 100 - redbull_away_from_fast_team 
                    print("Red Bull's RVP (performance compared to fastest team) is: {:.2f}%".format(redbull_rvp))
                    print("")
                    player_input = True

                # Mercedes
                mercedes_performance_percent = float(input("Enter Mercedes's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if mercedes_performance_percent > 107:
                    print("This is an incorrect value")
                elif mercedes_performance_percent < 100:
                    print("This is an incorrect value")
                else:
                    mercedes_away_from_fast_team = mercedes_performance_percent - 100
                    mercedes_rvp = 100 - mercedes_away_from_fast_team 
                    print("Mercedes's RVP (performance compared to fastest team) is: {:.2f}%".format(mercedes_rvp))
                    print("")
                    player_input = True 


                # Aston Martin
                astonmartin_performance_percent = float(input("Enter Aston Martin's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if astonmartin_performance_percent > 107:
                     print("This is an incorrect value")
                elif astonmartin_performance_percent < 100: 
                     print("This is an incorrect value")
                else:   
                    astonmartin_away_from_fast_team = astonmartin_performance_percent - 100
                    astonmartin_rvp = 100 - astonmartin_away_from_fast_team 
                    print("Aston Martin's RVP (performance compared to fastest team) is: {:.2f}%".format(astonmartin_rvp))
                    print("")
                    player_input = True

                # Alpine
                alpine_performance_percent = float(input("Enter Alpine's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if alpine_performance_percent > 107:
                    print("This is an incorrect value")
                elif alpine_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    alpine_away_from_fast_team = alpine_performance_percent - 100
                    alpine_rvp = 100 - alpine_away_from_fast_team 
                    print("Alpine's RVP (performance compared to fastest team) is: {:.2f}%".format(alpine_rvp))
                    print("")
                    player_input = True 

                # Haas
                haas_performance_percent = float(input("Enter Haas's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if haas_performance_percent > 107:
                     print("This is an incorrect value")
                elif haas_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    haas_away_from_fast_team = haas_performance_percent - 100
                    haas_rvp = 100 - haas_away_from_fast_team 
                    print("Haas's RVP (performance compared to fastest team) is: {:.2f}%".format(haas_rvp))
                    print("")
                    player_input = True 

                # Racing Bulls
                racingbulls_performance_percent = float(input("Enter Racing Bulls's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximum due to F1 regulations is 107): "))
                if racingbulls_performance_percent > 107:
                     print("This is an incorrect value")
                elif racingbulls_performance_percent < 100:
                     print("This is an incorrect value")
                else:
                    racingbulls_away_from_fast_team = racingbulls_performance_percent - 100
                    racingbulls_rvp = 100 - racingbulls_away_from_fast_team
                    print("Racing Bulls's RVP (performance compared to fastest team) is: {:.2f}%".format(racingbulls_rvp))
                    print("")
                    player_input = True 

                # Williams
                williams_performance_percent = float(input("Enter Williams's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximumn due to F1 regulations is 107): "))
                if williams_performance_percent > 107: 
                     print("This is an incorrect value")
                elif racingbulls_performance_percent < 100: 
                     print("This is an incorrect value")
                else:
                    williams_away_from_fast_team = williams_performance_percent - 100
                    williams_rvp = 100 - williams_away_from_fast_team 
                    print("Williams's RVP (performance compared to fastest team) is: {:.2f}%".format(williams_rvp))
                    print("")
                    player_input = True

                # Kick Sauber
                kicksauber_performance_percent = float(input("Enter Kick Sauber's performance as a percentage of the fastest team (suggested values are from over 100 to 102, maximumn due to F1 regulations is 107): "))
                if kicksauber_performance_percent > 107:
                     print("This is an incorrect value")
                elif kicksauber_performance_percent < 100:
                     print("This is an incorrect value")
                else: 
                    kicksauber_away_from_fast_team = kicksauber_performance_percent - 100
                    kicksauber_rvp = 100 - kicksauber_away_from_fast_team
                    print("Kick Sauber's RVP (performance compared to fastest team) is: {:.2f}%".format(kicksauber_rvp))
                    print("")
                    player_input = True
            # Stores RVPs
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
            driver_race_elos = []
            for driver, info in driver_index.items():
                team = info["team"]
                rvp = team_rvps.get(team, 100)
                driver_elo = info["elo"]
             #Makes driver race elo which is a combination of the cars performance and the drivers skill 
                driver_race_elo = driver_elo * ((rvp/100) ** 60)
             #Sorts the driver elo from highest to lowest     
                driver_race_elos.append((driver.title(), driver_race_elo))
            driver_race_elos.sort(key=lambda x: x[1], reverse=True)
             # Prints all dirver elos in order 
            print("\nExpected Race Results based on Race Elo\n")

            # Assign simulated finishing positions
            for i, (driver, elo) in enumerate(driver_race_elos, start=1):
                print("P{}: {} ({:.0f})".format(i, driver, elo))
        # Stops code if there is a wrong value
        except ValueError:
            print("Please enter a valid number (e.g. 101).")
    # Quit function 
    elif reason_of_run == "quit":
        print("Thank you for using this program!")
        break
    #For cases that do not algin with any of the options 
    else:
        print("Invalid option. Please try again.")
    