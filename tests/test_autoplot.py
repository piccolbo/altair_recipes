import altair_recipes as ar
import numpy as np
import pandas as pd
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test


np.random.seed(seed=0)

test_size = 5000


def rand_cat(x, n):
    return (
        pd.Series((x + np.random.normal(size=test_size) * n) + 77)
        .astype(int)
        .apply(chr)
    )


x = np.random.normal(size=test_size)
y = np.random.normal(size=test_size) + x
z = np.random.normal(size=test_size) + y
data = pd.DataFrame(
    dict(
        x=x,
        x_cat=rand_cat(x, 1),
        y=y,
        y_cat=rand_cat(y, 0.5),
        z=z,
        z_cat=rand_cat(z, 0.5),
    )
)

#
# numvars = ["x", "y", "z"]
# catvars = ["x_cat", "y_cat", "z_cat"]
# n = 0
# for nvars in range(1, 4):
#     for ncatvars in range(0, nvars + 1):
#         vars = catvars[:ncatvars] + numvars[ncatvars:nvars]
#         for nrows in [10, 50, 250, 1000, 5000]:
#             n = n + 1
#             print(
#                 """
# #'Test autoplot #{n}
#
# @viz_reg_test
# def test_autoplot_{n}():
#     return ar.autoplot(data.head({nrows}), columns={vars})
#
# show_test(test_autoplot_{n})
# """.format(
#                     nrows=nrows, vars=vars, n=n
#                 )
#             )
#'Test autoplot #1


@viz_reg_test
def test_autoplot_1():
    return ar.autoplot(data.head(10), columns=["x"])


show_test(test_autoplot_1)


#'Test autoplot #2


@viz_reg_test
def test_autoplot_2():
    return ar.autoplot(data.head(50), columns=["x"])


show_test(test_autoplot_2)


#'Test autoplot #3


@viz_reg_test
def test_autoplot_3():
    return ar.autoplot(data.head(250), columns=["x"])


show_test(test_autoplot_3)


#'Test autoplot #4


@viz_reg_test
def test_autoplot_4():
    return ar.autoplot(data.head(1000), columns=["x"])


show_test(test_autoplot_4)


#'Test autoplot #5


@viz_reg_test
def test_autoplot_5():
    return ar.autoplot(data.head(5000), columns=["x"])


show_test(test_autoplot_5)


#'Test autoplot #6


@viz_reg_test
def test_autoplot_6():
    return ar.autoplot(data.head(10), columns=["x_cat"])


show_test(test_autoplot_6)


#'Test autoplot #7


@viz_reg_test
def test_autoplot_7():
    return ar.autoplot(data.head(50), columns=["x_cat"])


show_test(test_autoplot_7)


#'Test autoplot #8


@viz_reg_test
def test_autoplot_8():
    return ar.autoplot(data.head(250), columns=["x_cat"])


show_test(test_autoplot_8)


#'Test autoplot #9


@viz_reg_test
def test_autoplot_9():
    return ar.autoplot(data.head(1000), columns=["x_cat"])


show_test(test_autoplot_9)


#'Test autoplot #10


@viz_reg_test
def test_autoplot_10():
    return ar.autoplot(data.head(5000), columns=["x_cat"])


show_test(test_autoplot_10)


#'Test autoplot #11


@viz_reg_test
def test_autoplot_11():
    return ar.autoplot(data.head(10), columns=["x", "y"])


show_test(test_autoplot_11)


#'Test autoplot #12


@viz_reg_test
def test_autoplot_12():
    return ar.autoplot(data.head(50), columns=["x", "y"])


show_test(test_autoplot_12)


#'Test autoplot #13


@viz_reg_test
def test_autoplot_13():
    return ar.autoplot(data.head(250), columns=["x", "y"])


show_test(test_autoplot_13)


#'Test autoplot #14


@viz_reg_test
def test_autoplot_14():
    return ar.autoplot(data.head(1000), columns=["x", "y"])


show_test(test_autoplot_14)


#'Test autoplot #15


@viz_reg_test
def test_autoplot_15():
    return ar.autoplot(data.head(5000), columns=["x", "y"])


show_test(test_autoplot_15)


#'Test autoplot #16


@viz_reg_test
def test_autoplot_16():
    return ar.autoplot(data.head(10), columns=["x_cat", "y"])


show_test(test_autoplot_16)


#'Test autoplot #17


@viz_reg_test
def test_autoplot_17():
    return ar.autoplot(data.head(50), columns=["x_cat", "y"])


show_test(test_autoplot_17)


#'Test autoplot #18


@viz_reg_test
def test_autoplot_18():
    return ar.autoplot(data.head(250), columns=["x_cat", "y"])


show_test(test_autoplot_18)


#'Test autoplot #19


@viz_reg_test
def test_autoplot_19():
    return ar.autoplot(data.head(1000), columns=["x_cat", "y"])


show_test(test_autoplot_19)


#'Test autoplot #20


@viz_reg_test
def test_autoplot_20():
    return ar.autoplot(data.head(5000), columns=["x_cat", "y"])


show_test(test_autoplot_20)


#'Test autoplot #21


@viz_reg_test
def test_autoplot_21():
    return ar.autoplot(data.head(10), columns=["x_cat", "y_cat"])


show_test(test_autoplot_21)


#'Test autoplot #22


@viz_reg_test
def test_autoplot_22():
    return ar.autoplot(data.head(50), columns=["x_cat", "y_cat"])


show_test(test_autoplot_22)


#'Test autoplot #23


@viz_reg_test
def test_autoplot_23():
    return ar.autoplot(data.head(250), columns=["x_cat", "y_cat"])


show_test(test_autoplot_23)


#'Test autoplot #24


@viz_reg_test
def test_autoplot_24():
    return ar.autoplot(data.head(1000), columns=["x_cat", "y_cat"])


show_test(test_autoplot_24)


#'Test autoplot #25


@viz_reg_test
def test_autoplot_25():
    return ar.autoplot(data.head(5000), columns=["x_cat", "y_cat"])


show_test(test_autoplot_25)


#'Test autoplot #26


@viz_reg_test
def test_autoplot_26():
    return ar.autoplot(data.head(10), columns=["x", "y", "z"])


show_test(test_autoplot_26)


#'Test autoplot #27


@viz_reg_test
def test_autoplot_27():
    return ar.autoplot(data.head(50), columns=["x", "y", "z"])


show_test(test_autoplot_27)


#'Test autoplot #28


@viz_reg_test
def test_autoplot_28():
    return ar.autoplot(data.head(250), columns=["x", "y", "z"])


show_test(test_autoplot_28)


#'Test autoplot #29


@viz_reg_test
def test_autoplot_29():
    return ar.autoplot(data.head(1000), columns=["x", "y", "z"])


show_test(test_autoplot_29)


#'Test autoplot #30


@viz_reg_test
def test_autoplot_30():
    return ar.autoplot(data.head(5000), columns=["x", "y", "z"])


show_test(test_autoplot_30)


#'Test autoplot #31


@viz_reg_test
def test_autoplot_31():
    return ar.autoplot(data.head(10), columns=["x_cat", "y", "z"])


show_test(test_autoplot_31)


#'Test autoplot #32


@viz_reg_test
def test_autoplot_32():
    return ar.autoplot(data.head(50), columns=["x_cat", "y", "z"])


show_test(test_autoplot_32)


#'Test autoplot #33


@viz_reg_test
def test_autoplot_33():
    return ar.autoplot(data.head(250), columns=["x_cat", "y", "z"])


show_test(test_autoplot_33)


#'Test autoplot #34


@viz_reg_test
def test_autoplot_34():
    return ar.autoplot(data.head(1000), columns=["x_cat", "y", "z"])


show_test(test_autoplot_34)


#'Test autoplot #35


@viz_reg_test
def test_autoplot_35():
    return ar.autoplot(data.head(5000), columns=["x_cat", "y", "z"])


show_test(test_autoplot_35)


#'Test autoplot #36


@viz_reg_test
def test_autoplot_36():
    return ar.autoplot(data.head(10), columns=["x_cat", "y_cat", "z"])


show_test(test_autoplot_36)


#'Test autoplot #37


@viz_reg_test
def test_autoplot_37():
    return ar.autoplot(data.head(50), columns=["x_cat", "y_cat", "z"])


show_test(test_autoplot_37)


#'Test autoplot #38


@viz_reg_test
def test_autoplot_38():
    return ar.autoplot(data.head(250), columns=["x_cat", "y_cat", "z"])


show_test(test_autoplot_38)


#'Test autoplot #39


@viz_reg_test
def test_autoplot_39():
    return ar.autoplot(data.head(1000), columns=["x_cat", "y_cat", "z"])


show_test(test_autoplot_39)


#'Test autoplot #40


@viz_reg_test
def test_autoplot_40():
    return ar.autoplot(data.head(5000), columns=["x_cat", "y_cat", "z"])


show_test(test_autoplot_40)


#'Test autoplot #41


@viz_reg_test
def test_autoplot_41():
    return ar.autoplot(data.head(10), columns=["x_cat", "y_cat", "z_cat"])


show_test(test_autoplot_41)


#'Test autoplot #42


@viz_reg_test
def test_autoplot_42():
    return ar.autoplot(data.head(50), columns=["x_cat", "y_cat", "z_cat"])


show_test(test_autoplot_42)


#'Test autoplot #43


@viz_reg_test
def test_autoplot_43():
    return ar.autoplot(data.head(250), columns=["x_cat", "y_cat", "z_cat"])


show_test(test_autoplot_43)


#'Test autoplot #44


@viz_reg_test
def test_autoplot_44():
    return ar.autoplot(data.head(1000), columns=["x_cat", "y_cat", "z_cat"])


show_test(test_autoplot_44)


#'Test autoplot #45


@viz_reg_test
def test_autoplot_45():
    return ar.autoplot(data.head(5000), columns=["x_cat", "y_cat", "z_cat"])


show_test(test_autoplot_45)
