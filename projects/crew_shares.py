# WM 2nd Crew Shares

# Inputs
money_made = float(input("How much money was made on the outing: "))
crew_num = int(input("How many crew memebers are there: "))

total_share_count = crew_num+10
share_value = (float(round(money_made/total_share_count)))
captain_amount = share_value*7
first_mate_amount = share_value*3
crew_amount = share_value-500
print(f"The captain get {captain_amount}, the first mate gets {first_mate_amount}, and each crewmate needs {crew_amount} more.1")