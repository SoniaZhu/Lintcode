queue(start)
visited(start)
step = -1
while queue:
  step++
  for in queue.size:
    pop()
    for nodes:
      calculate
      if next == target: return
      if outofbounds  or visited (or more): continue
      queue.push
      visited.add


maxes = []
row = [root]
while any(row):
    maxes.append(max(node.val for node in row))
    row = [kid for node in row for kid in (node.left, node.right) if kid]
return maxes
