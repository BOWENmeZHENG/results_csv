import success_fail_func as sf

locations = ['/media/bowen/TOSHIBA EXT/ga_2/results/till0117']
ids = [7]

for i, loc in enumerate(locations):
    sf.success_fail(ids[i], loc)