with open("input.txt", 'r') as f:
	lines = f.readlines()
	lines.append("")

max = -1
curr = 0

for l in lines:
	stripped = l.strip()
	if stripped == "":
		if curr > max:
			max = curr
		curr = 0
	else:
		curr += int(stripped)

print(max)
