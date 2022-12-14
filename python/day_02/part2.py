with open("input.txt", 'r') as f:
	lines = f.readlines()

lines = [tuple(l.strip().split(" ")) for l in lines]

loss_score = 0
win_score = 6
draw_score = 3
outcomes = {("A", "X") : loss_score + 3,
			("B", "Y") : draw_score + 2,
			("C", "Z") : win_score + 1,
			("A", "Y") : draw_score + 1,
			("B", "Z") : win_score + 3,
			("C", "X") : loss_score + 2,
			("A", "Z") : win_score + 2,
			("B", "X") : loss_score + 1,
			("C", "Y") : draw_score + 3}

total_score = sum([outcomes[l] for l in lines])

print(total_score)
