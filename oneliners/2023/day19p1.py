print((lambda workflows, parts: sum(sum(part.values()) for part in parts if (lambda f: f(f, "in"))(lambda f, name: False if name == "R" else True if name == "A" else f(f, next(x.split(":")[-1] for x in workflows[name] if ":" not in x or {">": int.__gt__, "<": int.__lt__}[x[1]](part[x[0]], int(x[2:].split(":")[0])))))))(*(lambda top, bot: ({line.split("{")[0]: line[:-1].split("{")[1].split(",") for line in top.splitlines()}, [{segment[0]: int(segment[2:]) for segment in line[1:-1].split(",")} for line in bot.splitlines()]))(*open(0).read().split("\n\n"))))