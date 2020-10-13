from .pair import Pair

def test_pair_name():
    assert Pair('EUR','USD').get_name() == 'EURUSD'