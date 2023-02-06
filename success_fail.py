import utils
import os
from pathlib import Path
# If stress_t < 0.2, fail
with open('result.csv', 'w') as f:
    f.write('name,density,strength,failure_strain,num_atoms,num_bonds,bond_per_atom\n')
all_folders = [f.path for f in os.scandir() if f.is_dir()]
for folder in all_folders:
    if folder.startswith(f'./_f') and Path(f'{folder}/tension.lammpstrj').is_file():
        print('now start: ' + folder)
        strain_t, stress_t, density = utils.read_results(folder)
        strength, failure_strain = utils.tensile_strength(stress_t, strain_t)
        boxsize, xyz = utils.parse(f'{folder}/tension.lammpstrj')
        bond_count, num_atoms, bond_per_atom = utils.comp_bond(xyz, boxsize, bl=1.7)
        print(folder + 'done')
        with open('result.csv', 'a') as f:
            f.write(f'{folder[3:]},{density:.1f},{strength:.3f},{failure_strain:.3f},{bond_count},{num_atoms},{bond_per_atom:.3f}\n')
    # utils.plot_curves(strain_t, stress_t)
