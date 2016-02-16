#!/usr/bin/env python
from kivy.gesture import GestureDatabase

gdb = GestureDatabase()

square1 = \
gdb.str_to_gesture('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')

square2 = \
gdb.str_to_gesture('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')

square3 = \
gdb.str_to_gesture('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')

square4 = \
gdb.str_to_gesture('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')

square5 = \
gdb.str_to_gesture('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')

square6 = \
gdb.str_to_gesture('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')

square7 = \
gdb.str_to_gesture('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')

square8 = \
gdb.str_to_gesture('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')

timeline = \
gdb.str_to_gesture('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')
# simple_timeline = \
# gdb.str_to_gesture('eNq1l0tu2zAQhve6SLypwXlzLpBuC+QARZoIiZHUEWynbW7f4ShNH4gsoYC8sS19/EnNJ0rkZvew+/ayveuPp+dD3318/R5Kt7kdoLu62F9/7S+6AeNnfFF3vLo4ng5PD/0x/nK3eRyk27wbcpVYN2iLsmg/PO32p9astmY+0exTo7oBxhG0IbxEE8Du8kPZllIqVyMlFAeuANZG9KMRlASzWTAAjqVQwe745fp8R5wdSXfX+sguoFYttRgyisb/6OPuV3whKKgFzYHcZT4+Lz+GuSieSA3iKKCbIi2IrxnvK8VjWkBYGF9U0cXIWEyU5uMx42lZPJIWLyCsUhWc6nx+ukVZLT/l4kK5IE6oqg4VmGE+Pd2ir5NOqZZgpfQ0SwvNAqi5CNfKzh7Tdz4/zdJCsyEVSMytAgJr/JzvINWSrddB2iVfrQNOwbxEcJx0NK4FXEGQQsJ8fBpmWis+BbOsFZ962daKT7nsi+KBRQWlklMRR5x/Z0mqlWVqUeKGgbfn/vyNI2lWaKX0FCuyUnp6FVspPbXKMq2x+EAHqXHSXX0+XdOqwkrpaVWXWaXqjFXAhItIsfkHsqZWlbXi06su8xoHjEQsFojI8eKaX4hoitVlYmMBOi6fqGI1xvnaW5o1WCs+1doytYLOFgAQKFeer42lWZP/Tm9bhptD3+/fNgCmbQcQE25zSWjb0l0i163/+eHuNFjtroOgMk34SExn1JIE8zQBSdjYi+QF/v5oIzCJqtMENYKJ/z01gXPiSgtxabgQTPevjdAi04QlwWeuIattr5V6l8hqxwZskvCsdnWfJrLaELfINIIjItNGPOsdd9n0YJ1HRM+MJesK8SCdRnREzqXYiFScRuqI+JmLjtqOc+W+393dn9qOtgQMf6Fxxbnh/b67Pd0nAt2la6tCHD09PfaH6/1Nn2dyskI7/jqvPw+Hp9vnmzE6Zituq9e4CVWLQlvdxGTd/gSfQhQG')
gestures=[square1,square2,square3,square4,square5,square6,square7,square8,timeline]