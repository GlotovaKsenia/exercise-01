import dungeon_stats

test = [12,15,11,14,48]

a = dungeon_stats.mean(test)
m = dungeon_stats.median(test)
o = dungeon_stats.is_outlier(a,test)
print(a)
print(m)
print(o)