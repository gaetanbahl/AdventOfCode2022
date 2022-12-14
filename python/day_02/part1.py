with open("input.txt", 'r') as f:
	lines = f.readlines()

lines = [tuple(l.strip().split(" ")) for l in lines]

loss_score = 0
win_score = 6
draw_score = 3
shape_scores = dict(X = 1, Y = 2, Z = 3)
outcomes = {("A", "X") : draw_score,
			("B", "Y") : draw_score,
			("C", "Z") : draw_score,
			("A", "Y") : win_score,
			("B", "Z") : win_score,
			("C", "X") : win_score,
			("A", "Z") : loss_score,
			("B", "X") : loss_score,
			("C", "Y") : loss_score}

total_score = sum([outcomes[l] + shape_scores[l[1]] for l in lines])

print(total_score)