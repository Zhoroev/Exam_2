def func(name, **args):
    print(name)
    for i, j in args.items():
        print(f'{i} - {j}')


func(name='USA', population='330 million', is_democratic=True)

func(name='Kyrgyzstan', area='200 km2',
     have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
