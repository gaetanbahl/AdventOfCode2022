with open("input.txt", 'r') as f:
	lines = f.readlines()
	lines.append("")

elves = []

curr = 0

for l in lines:
	stripped = l.strip()
	if stripped == "":
		elves.append(curr)
		curr = 0
	else:
		curr += int(stripped)

elves = sorted(elves)

print(sum(elves[-3:]))
