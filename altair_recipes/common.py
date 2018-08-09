def viz_reg_test(test_f):
    def fun(regtest):
        plot = test_f()
        if regtest is not None:
            regtest.write(plot.to_json())
        return plot

    return fun
