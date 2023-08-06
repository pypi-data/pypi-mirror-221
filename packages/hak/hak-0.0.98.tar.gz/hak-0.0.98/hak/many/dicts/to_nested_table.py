# ignore_overlength_lines
from hak.one.dict.rate.make import f as make_rate
from hak.one.string.print_and_return_false import f as pf
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.one.dict.rate.to_str import f as rate_to_str

f_a = lambda x, a, b   : [rate_to_str(r[a][b]) for r in x]
f_b = lambda x, a, b   : unit_to_str(x[0][a][b]['unit'])
f_c = lambda x, a, b   : max(len(_) for _ in [b, f_b(x, a, b), *f_a(x, a, b)])
f_d = lambda x, a, b   : max(f_c(x, a, b), len(a))
f_e = lambda x, a      : f_g(x[0][a])
f_f = lambda x         : sum(x)+(len(x)-1)*3
f_g = lambda x         : sorted(x.keys())
f_h = lambda x         : f_g(x[0])
f_i = lambda x, a      : f_f([f_d(x, a, k) for k in f_e(x, a)])
f_j = lambda x, a      : [a(x, z) for z in f_h(x)]
f_k = lambda x, a      : f'|{a}'+f'{a}|{a}'.join(x)+f'{a}|'
f_top_border = lambda x: f_k(['-'*_ for _ in f_j(x, f_i)], '-')
f_m = lambda x, a, b   : '-'*f_d(x, a, b)
f_n = lambda x         : [(a, b) for a in f_h(x) for b in f_e(x, a)]
f_o = lambda x         : f_k(x, '-')
f_horizontal_line = lambda x: f_o([f_m(x, a, b) for (a, b) in f_n(x)])
f_q = lambda x, a      : f'{a:>{f_f([f_d(x, a, k) for k in f_e(x, a)])}}'
f_root_header = lambda x: f_k(f_j(x, f_q), ' ')
f_s = lambda x         : f_k(x, ' ')
f_t = lambda x, fn     : f_s([fn(x, a, b) for (a, b) in f_n(x)])
f_underlined = lambda x, fn     : [f_t(x, fn), f_horizontal_line(x)]
f_v = lambda x, a, b   : f'{b:>{f_d(x, a, b)}}'
f_w = lambda x, a, b   : f"{f_b(x, a, b):>{f_d(x, a, b)}}"
f_x = lambda x, a, b, r: f'{rate_to_str(r[a][b]):>{f_d(x, a, b)}}'
f_y = lambda x, r      : [f_x(x, a, b, r) for (a, b) in f_n(x)]
f_row_values = lambda x: [f_s(f_y(x, r)) for r in x]
f_units = lambda x: f_underlined(x, f_w)
f_sub_header = lambda x: f_underlined(x, f_v)

f = lambda x: '\n'.join([
  f_top_border(x),
  f_root_header(x),
  f_horizontal_line(x),
  *f_sub_header(x),
  *f_units(x),
  *f_row_values(x),
  f_horizontal_line(x)
])

def t_nested_b():
  x = [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(1, 1, {'apple': 1}),
        'bananazzz': make_rate(2, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  y = '\n'.join([
    "|--------------------|-----------------------------------|--------|",
    "|             prices |                           volumes | zloops |",
    "|---------|----------|----------|-----------|------------|--------|",
    "|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |",
    "|---------|----------|----------|-----------|------------|--------|",
    "| $/apple | $/banana |    apple |    banana |       pear |  zloop |",
    "|---------|----------|----------|-----------|------------|--------|",
    "|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |",
    "|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |",
    "|---------|----------|----------|-----------|------------|--------|",
  ])
  z = f(x)
  return y == z or pf([f'x: {x}', f'y:\n{y}', f'z:\n{z}'])

def t():
  if not t_nested_b(): return pf('t_nested failed')
  return True
