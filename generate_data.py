import sympy as sp

if __name__ == '__main__':
    sp.init_printing(use_unicode=True) #no ugly math allowed

# a_r is the scale factor
a_r = sp.Symbol('a_r')
# f_c is the transmitted frequency
f_c = sp.Symbol('f_c')
# t is time
t = sp.Symbol('t')
# ----
# eps is epsilon which is the wavelength
eps = sp.Symbol('eps')
# v_rad is the radial velocity of the center of rotation with respect to the radar
v_rad = sp.Symbol('v_rad')
# r is the range of the center of rotation
r = sp.Symbol('r')
# -----

pi = sp.pi
e  = sp.E

# I just decomposed the psi's gigantic expression into manageable parts
top_4pi = (4*pi / eps) * (r + (v_rad * t))
top_2pi = (2 * pi * f_c * t)