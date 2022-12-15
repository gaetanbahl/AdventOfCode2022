with open("input.txt", 'r') as f:
    lines = f.readlines()[1:]
    lines = [l.strip().split(" ") for l in lines]



def create_dir(name, parent):
    return {"children" : dict(), "files" : dict(), "size" : 0, "name" : name, "parent" : parent}

fs = create_dir("/", None)

curr = fs

while(len(lines) > 0):

    line = lines.pop(0)
    assert line[0] == "$"

    if line[1] == "ls":
        while lines[0][0] != "$":
            output_line = lines.pop(0)

            if output_line[0] == "dir":
                dir_name = output_line[1]
                curr["children"][dir_name] = create_dir(dir_name, curr)
            else:
                size = int(output_line[0])
                file_name = output_line[1]
                curr["files"][file_name] = size

            if len(lines) == 0:
                break
    
    if line[1] == "cd":
        next_dir = line[2]
        if next_dir == "..":
            curr = curr["parent"]
        else:
            curr = curr["children"][line[2]]


def compute_size(fs):

    n_small_total = 0
    for c in fs["children"]:
        n_small = compute_size(fs["children"][c])
        n_small_total += n_small
        
    fs["size"] += sum([fs["children"][c]["size"] for c in fs["children"] ])
    fs["size"] += sum([fs["files"][f] for f in fs["files"]])

    if fs["size"] <= 100000:
        n_small_total += fs["size"]
    
    return n_small_total

print(compute_size(fs))
