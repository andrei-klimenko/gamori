import numpy as np

fotx = (3,2)
limit1 = [((0,2), 1, 8), ((4,-1), 1, 5), ((3,-3), 1, 5), ((4,-2), -1, 4)]

m1 = np.zeros((len(limit1) + 1, len(fotx) + len(limit1) + 1))
for idx, row in enumerate(limit1):
    if row[1] > 0:
        m1[idx][0] = row[0][0]
        m1[idx][1] = row[0][1]
        m1[idx][len(fotx) + idx ] = row[1]
        m1[idx][-1] = row[2]
    else:
        m1[idx][0] = row[0][0]*(-1)
        m1[idx][1] = row[0][1]*(-1)
        m1[idx][len(fotx) + idx ] = row[1]*(-1)
        m1[idx][-1] = row[2]*(-1)

m1[-1][0] = fotx[0]*(-1)
m1[-1][1] = fotx[1]*(-1)

def is_row_negative(row):
    for i in row:
        if i < 0:
            return False
        else:
            return True

def find_min_from_first_elem(column):
    min_teta = min(x[0] for x in column)
    for i in column:
        if i[0] == min_teta:
            return i

def rukozhop_symplex(m1):
    # while is_row_negative(m1[-1]):
    get_min = min(m1[-1]) # 3
    get_idx_column = np.where(m1[-1] == get_min)[0][0]
    full_column = m1[:,get_idx_column]
    base_column = m1[:,-1]
    teta_column = []
    for idx, el in enumerate(base_column):
        if full_column[idx] != 0 and el != 0:
            teta_column.append((el/full_column[idx], idx))
    teta_pair = find_min_from_first_elem(teta_column)
    


    return teta_pair
print(rukozhop_symplex(m1))