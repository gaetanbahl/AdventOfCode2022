# forgive me, it was faster to do this than writing a parser :(
monkeys = []
monkeys.append({"items":[83, 88, 96, 79, 86, 88, 70],
                "op": lambda x : x*5,
                "test": 11,
                "true": 2,
                "false": 3,
                "inspected": 0})
monkeys.append({"items":[59, 63, 98, 85, 68, 72],
                "op": lambda x : x*11,
                "test": 5,
                "true": 4,
                "false": 0,
                "inspected": 0})
monkeys.append({"items":[90, 79, 97, 52, 90, 94, 71, 70],
                "op": lambda x : x+2,
                "test": 19,
                "true": 5,
                "false": 6,
                "inspected": 0})
monkeys.append({"items":[97, 55, 62],
                "op": lambda x : x+5,
                "test": 13,
                "true": 2,
                "false": 6,
                "inspected": 0})
monkeys.append({"items":[74, 54, 94, 76],
                "op": lambda x : x**2,
                "test": 7,
                "true": 0,
                "false": 3,
                "inspected": 0}) 
monkeys.append({"items":[58],
                "op": lambda x : x+4,
                "test": 17,
                "true": 7,
                "false": 1,
                "inspected": 0})   
monkeys.append({"items":[66, 63],
                "op": lambda x : x+6,
                "test": 2,
                "true": 7,
                "false": 5,
                "inspected": 0})    
monkeys.append({"items":[56, 56, 90, 96, 68],
                "op": lambda x : x+7,
                "test": 3,
                "true": 4,
                "false": 1,
                "inspected": 0})   


for r in range(20):
    for m in monkeys:
        while(len(m["items"])):
            m["inspected"] += 1
            item = m["items"].pop()
            item = m["op"](item)
            item //= 3
            if not item % m["test"]:
                monkeys[m["true"]]["items"].append(item)
            else:
                monkeys[m["false"]]["items"].append(item)

scores = sorted([m["inspected"] for m in monkeys])
print(scores[-1] * scores[-2])