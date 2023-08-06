from small_pipe import pipe, each, where, reduce
    

def test_alias():        
        double = each(lambda x: x * 2)
        assert pipe(range(3), double, list) == [0, 2, 4]


def test_higher_order():
        value = pipe(
            range(5),
            each(lambda x: x * 2),
            where(lambda x: x % 4 == 0),
            reduce(lambda x, y: x + y, 30),
        )
        assert value == 42 