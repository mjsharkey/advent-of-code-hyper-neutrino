print((lambda c: (lambda f: sum(f(f, "?".join([cfg] * 5), tuple(map(int, nums.split(","))) * 5) for cfg, nums in [line.split() for line in open(0)]))(lambda f, cfg, nums, flag = False: (lambda k: c[k] if k in c else (lambda x: [c.__setitem__(k, x), x][1])(int(sum(nums) == 0) if cfg == "" else int("#" not in cfg) if sum(nums) == 0 else (0 if flag and nums[0] == 0 else f(f, cfg[1:], (nums[0] - 1, *nums[1:]), True)) if cfg[0] == "#" else (0 if flag and nums[0] > 0 else f(f, cfg[1:], nums[1:] if nums[0] == 0 else nums, False)) if cfg[0] == "." else (f(f, cfg[1:], nums[1:], False) if nums[0] == 0 else f(f, cfg[1:], (nums[0] - 1, *nums[1:]), True)) if flag else f(f, cfg[1:], nums, False) + f(f, cfg[1:], (nums[0] - 1, *nums[1:]), True)))((cfg, nums, flag))))({}))