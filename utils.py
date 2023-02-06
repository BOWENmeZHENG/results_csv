import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_results(folder):
    strain_t, stress_t = read_curve(folder)
    density = read_density(folder)
    return strain_t, stress_t, density

def read_curve(folder):
    # with open(f"{folder}/compression.txt") as f:
    #     lines = f.readlines()
    # lines[0] = 'x stress\n'
    # with open(f"{folder}/compression_post.txt", "w") as f:
    #     f.writelines(lines)
    with open(f"{folder}/tension.txt") as f:
        lines = f.readlines()
    lines[0] = 'x stress\n'
    with open(f"{folder}/tension_post.txt", "w") as f:
        f.writelines(lines)
    # data_c = pd.read_csv(f"{folder}/compression_post.txt", delimiter=r'\s+')
    # strain_c = -(data_c.x - data_c.x[0]) / data_c.x[0]
    # stress_c = -data_c.stress
    data_t = pd.read_csv(f"{folder}/tension_post.txt", delimiter=r'\s+')
    strain_t = (data_t.x - data_t.x[0]) / data_t.x[0]
    stress_t = data_t.stress
    return strain_t.to_numpy(), stress_t.to_numpy()  # strain_c.to_numpy(), stress_c.to_numpy(), 

def read_density(folder):
    with open(f"{folder}/log.tension") as f:
        while True:
            line = f.readline()
            if line[:8] == '       0':
                break
    density = list(map(float, line.split()))[4] * 1000  # mg/cm3
    return density

def tensile_strength(stress_t, strain_t):
    strength = np.amax(stress_t)
    failure_strain = strain_t[np.argmax(stress_t)]
    return strength, failure_strain

def plot_curves(strain, stress, num_pts=40):
    plt.figure(figsize=(8, 6))
    plt.plot(strain[:num_pts], stress[:num_pts], linewidth=2)
    plt.xlabel("strain", fontsize=20)
    plt.ylabel("stress (GPa)", fontsize=20)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.show()


def parse(trj_name, line_limit=500000):
    xyz = []
    i = 0
    with open(trj_name) as f_trj:
        while i < line_limit:
            if len(xyz) > 0:
                break
            line = f_trj.readline()
            i += 1

            # Get atom number
            if line == 'ITEM: NUMBER OF ATOMS\n':
                line = f_trj.readline()
                i += 1
                line_list = [int(num_str) for num_str in line.split()]
                num_atoms = line_list[0]
            
            # Get box size
            if line == 'ITEM: BOX BOUNDS pp pp pp\n':
                line = f_trj.readline()
                i += 1
                line_list = [float(num_str) for num_str in line.split()]
                box_size = line_list[-1] * 2

            # Get xyz
            if line[:11] == 'ITEM: ATOMS':
                line = f_trj.readline()
                i += 1
                line_list = [float(num_str) for num_str in line.split()]
                xyz.append(line_list[2: 5])
                for _ in range(num_atoms - 1):  
                    line = f_trj.readline()
                    i += 1         
                    line_list = [float(num_str) for num_str in line.split()]
                    if line_list[1] == 1.:
                        xyz.append(line_list[2: 5])
                xyz = np.array(xyz)
                print(i)
    
    return box_size, xyz

def comp_bond(frame, boxsize, bl=1.7):
    num_atoms = len(frame)
    bond_count = 0
    for i, atom1 in enumerate(frame):
        for atom2 in frame[i + 1:]:
            # filter out the impossible
            if boxsize - bl > abs(atom1[0] - atom2[0]) > bl or boxsize - bl > abs(atom1[1] - atom2[1]) > bl or boxsize - bl > abs(atom1[2] - atom2[2]) > bl:
                continue
            
            # solve the boundary cases
            if atom1[0] - atom2[0] > boxsize - bl:
                atom2[0] += boxsize
            if atom1[0] - atom2[0] < -(boxsize - bl):
                atom2[0] -= boxsize
            if atom1[1] - atom2[1] > boxsize - bl:
                atom2[1] += boxsize
            if atom1[1] - atom2[1] < -(boxsize - bl):
                atom2[1] -= boxsize
            if atom1[2] - atom2[2] > boxsize - bl:
                atom2[2] += boxsize
            if atom1[2] - atom2[2] < -(boxsize - bl):
                atom2[2] -= boxsize

            dist = comp_dist(atom1, atom2)
            if dist < bl:
                bond_count += 1
    bond_per_atom = bond_count / num_atoms
    return bond_count, num_atoms, bond_per_atom

def comp_dist(xyz_1, xyz_2):
    return np.linalg.norm(xyz_2 - xyz_1)