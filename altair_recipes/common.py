def viz_reg_test(test_f):
    def fun(regtest):
        plot = test_f()
        if regtest is not None:
            regtest.write(plot.to_json())
        plot.save(
            test_f.__code__.co_filename + "_" + test_f.__qualname__ + ".html")
        return plot

    return fun
