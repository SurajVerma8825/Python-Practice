traffic_colours = input("Enter the traffic colour:- ")

match traffic_colours:
    case  "Green":
           print("Go 🏃‍♂️‍➡️🚘")
    case "Yellow":
           print("Go Slowly 🟡")
    case "Red":
           print("Go 🏃‍♂️‍➡️🚘")
    case _ :
            print("Choose the correct colours")

