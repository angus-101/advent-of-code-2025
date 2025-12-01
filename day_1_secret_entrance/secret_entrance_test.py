from secret_entrance_2 import secret_entrance

def test_happy_path():
    rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    zeroes = secret_entrance(rotations)
    assert zeroes == 6
    
def test_counts_end_zeroes_l():
    rotations = ['L50']
    zeroes = secret_entrance(rotations)
    assert zeroes == 1
    
def test_counts_end_zeroes_r():
    rotations = ['R50']
    zeroes = secret_entrance(rotations)
    assert zeroes == 1
    
def test_counts_rotation_zeroes_r():
    rotations = ['R51']
    zeroes = secret_entrance(rotations)
    assert zeroes == 1
    
def test_counts_rotation_zeroes_long_r():
    rotations = ['R150']
    zeroes = secret_entrance(rotations)
    assert zeroes == 2

def test_counts_rotation_zeroes_l():
    rotations = ['L51']
    zeroes = secret_entrance(rotations)
    assert zeroes == 1
    
def test_counts_rotation_zeroes_long_l():
    rotations = ['L150']
    zeroes = secret_entrance(rotations)
    assert zeroes == 2
    
def test_counts_starts_0_r():
    rotations = ['R50', 'R150']
    zeroes = secret_entrance(rotations)
    assert zeroes == 2
    
def test_counts_starts_0_l():
    rotations = ['R50', 'L150']
    zeroes = secret_entrance(rotations)
    assert zeroes == 2
    
def test_many_zeroes_l():
    rotations = ['L50', 'L100', 'L100', 'L100']
    zeroes = secret_entrance(rotations)
    assert zeroes == 4
    
def test_many_zeroes_r():
    rotations = ['R50', 'R100', 'R100', 'R100']
    zeroes = secret_entrance(rotations)
    assert zeroes == 4