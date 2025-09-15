# WM 2nd Crew Shares

# Inputs
print("A captain comes to port after and outing, but doesn't have time to divy up the money, so he gives each crew memeber $500 before they leave, and then sits down to divy it with his first mate.")
money_made = float(input("How much money was made on the outing: "))
crew_num = int(input("How many crew memebers are there: "))

total_share_count = crew_num+10
share_value = (float(round(money_made/total_share_count, 2)))
captain_amount = share_value*7
first_mate_amount = share_value*3
crew_amount = share_value-500
print(f"The captain gets ${captain_amount:.2f}, the first mate gets ${first_mate_amount:.2f}, and each crewmate needs ${crew_amount:.2f} more.")