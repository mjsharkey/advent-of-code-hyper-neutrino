print((lambda grid, pq = __import__("queue").PriorityQueue(), s = set(), q = []: (lambda add: [pq.put((0, 0, 0, 0, 1, 0)), pq.put((0, 0, 0, 1, 0, 0)), q.append(pq.get()), [[s.add((r, c, dr, dc, n)), n < 3 and add(hl, r + dr, c + dc, dr, dc, n + 1), add(hl, r - dc, c + dr, -dc, dr, 1), add(hl, r + dc, c - dr, dc, -dr, 1), (r, c) == (len(grid) - 1, len(grid[0]) - 1) or pq.empty() or q.append(pq.get()), hl][-1] if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c, dr, dc, n) not in s else pq.empty() or q.append(pq.get()) for hl, r, c, dr, dc, n in q]][-1])(lambda hl, r, c, dr, dc, n: 0 <= r < len(grid) and 0 <= c < len(grid[0]) and pq.put((hl + grid[r][c], r, c, dr, dc, n)))[-1])([list(map(int, line.strip())) for line in open(0)]))
