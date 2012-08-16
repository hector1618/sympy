from sympy import (plot_implicit, cos, Symbol, Eq, sin, re, And, Or, exp, I,
                    tan)
from sympy.plotting.plot import matplotlib
from tempfile import NamedTemporaryFile
from sympy.utilities.pytest import skip

def tmp_file(name=''):
    return NamedTemporaryFile(suffix='.png').name

def plot_and_save():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    #implicit plot tests
    plot_implicit(Eq(y, cos(x)), (x, -5, 5),
            (y, -2, 2), show=False).save(tmp_file())
    plot_implicit(Eq(y**2, x**3 - x), (x, -5, 5),
            (y, -4, 4), show=False).save(tmp_file())
    plot_implicit(y > 1 / x, (x, -5, 5),
            (y, -2, 2), show=False).save(tmp_file())
    plot_implicit(y < 1 / tan(x), (x, -5, 5),
            (y, -2, 2), show=False).save(tmp_file())
    plot_implicit(y >= 2 * sin(x) * cos(x), (x, -5, 5),
            (y, -2, 2), show=False).save(tmp_file())
    plot_implicit(y <= x**2, (x, -3, 3),
            (y, -1, 5), show=False).save(tmp_file())

    #Test all input args for plot_implicit
    plot_implicit(Eq(y**2, x**3 - x), show=False).save(tmp_file())
    plot_implicit(Eq(y**2, x**3 - x), adaptive=False,
            show=False).save(tmp_file())
    plot_implicit(Eq(y**2, x**3 - x), adaptive=False, points = 500,
            show=False).save(tmp_file())
    plot_implicit(y > x, (x, -5, 5), show=False).save(tmp_file())
    plot_implicit(And(y > exp(x), y > x + 2), show=False).save(tmp_file())
    plot_implicit(Or(y > x, y > -x), show=False).save(tmp_file())
    plot_implicit(x**2 - 1, (x, -5, 5), show=False).save(tmp_file())
    plot_implicit(x**2 - 1, show=False).save(tmp_file())
    plot_implicit(y > x, depth = -5, show=False).save(tmp_file())
    plot_implicit(y > x, depth = 5, show=False).save(tmp_file())
    plot_implicit(y > cos(x), adaptive=False, show=False).save(tmp_file())
    plot_implicit(y < cos(x), adaptive=False, show=False).save(tmp_file())
    plot_implicit(And(y > cos(x), Or(y > x, Eq(y, x))), show=False).save(tmp_file())

    #Test plots which cannot be rendered using the adaptive algorithm
    #TODO: catch the warning.
    plot_implicit(Eq(y, re(cos(x) + I*sin(x))), show=False).save(tmp_file())

def test_matplotlib():
    if matplotlib:
        plot_and_save()
    else:
        skip("Matplotlib not the default backend")
