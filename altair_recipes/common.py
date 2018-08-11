import altair as alt
def viz_reg_test(test_f):
    def fun(regtest):
        plot = test_f()
        if regtest is not None:
            regtest.write(plot.to_json())
        plot.save(
            test_f.__code__.co_filename + "_" + test_f.__qualname__ + ".html")
        return plot

    return fun


def to_dataframe(data):
    #this is an undocumented hack
    return alt.Chart(data).data


def default(*args):
    return next(x for x in args if x is not None)
