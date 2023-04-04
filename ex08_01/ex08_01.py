def chop(set):
    del set[0]
    del set[-1]
    
def middle(set):
    newSet = set[1:-1]
    return newSet

orgSet = [12, 24, 36, 48, 60, 72]
dupeSet = [12, 24, 36, 48, 60, 72]
chopSet = chop(orgSet)
midSet = middle(dupeSet)

print(orgSet)
print(chopSet)
print(dupeSet)
print(midSet)
