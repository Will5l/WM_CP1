# WM 2nd Crew Shares

# Inputs
print("A captain comes to port after an outing, but doesn't have time to divy up the money, so he gives each crew memeber $500 before they leave, and then sits down to divy it with his first mate.")
money_made = float(input("How much money was made on the outing: "))
crew_num = int(input("How many crew memebers are there: "))

total_share_count = crew_num+10
share_value = (float(round(money_made/total_share_count, 2)))
captain_amount = round(share_value*7, 2)
first_mate_amount = round(share_value*3, 2)
crew_amount = round(share_value-500, 2)
print(f"The captain gets ${captain_amount:,}, the first mate gets ${first_mate_amount:,}, and each crewmate needs ${crew_amount:,} more.")