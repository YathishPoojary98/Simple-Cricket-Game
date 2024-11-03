import random

# generate a random number between 1 and 100
number = random.randint(1, 6)

bat_total = 0
bowl_total = 0
bat_flag = 0
bowl_flag = 0


a = int(input("Choose 1 for Batting or 2 for Bowling: "))
if a > 2:
	print("Invalid choice")
else:
	if a == 1:
		while bowl_flag == 0:
			guess = int(input("Score the run between 1 and 6: "))
			if guess == 0 or guess > 6:
				print("Invalid run")
				break
			if number == guess:
				print(f"You are out, your score is {bat_total}")
				while bowl_flag == 0:
					if bowl_total>bat_total:
						print(f"Computer won the match, You lost the match")
						bowl_flag = 1
						break
					guess1 = int(input("Enter the number between 1 and 6: "))
					if guess1 == 0 or guess1 > 6:
						print("Invalid run")
						break
					if number == guess1:
						print(f"Computer is out, Computer score is {bowl_total}")
						if bat_total == bowl_total:
							print(f"Match is tie")
						elif bat_total > bowl_total:
							print(f"You won the match by {bat_total-bowl_total}")
						else:
							print(f"You lost the match by {bowl_total-bat_total}")
						bowl_flag = 1
					else:
						bowl_total = bowl_total+guess1
			else:
				bat_total = bat_total+guess
	else:
		while bowl_flag == 0:
			guess = int(input("Enter the number between 1 and 6: "))
			if guess == 0 or guess > 6:
				print("Invalid run")
				break
			if number == guess:
				print(f"Computer is out, Computer score is {bowl_total}")
				while bowl_flag == 0:
					if bat_total>bowl_total:
						print(f"You won the match, Computer lost the match")
						bowl_flag = 1
						break
					guess1 = int(input("Score the run between 1 and 6: "))
					if guess1 == 0 or guess1 > 6:
						print("Invalid run")
						break
					if number == guess1:
						print(f"You are out, Your score is {bat_total}")
						if bat_total == bowl_total:
							print(f"Match is tie")
						elif bat_total > bowl_total:
							print(f"You won the match by {bat_total-bowl_total}")
						else:
							print(f"You lost the match by {bowl_total-bat_total}")
						bowl_flag = 1
					else:
						bat_total = bat_total+guess1
			else:
				bowl_total = bowl_total+guess