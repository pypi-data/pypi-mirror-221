import time
import pytest


@pytest.mark.parametrize('case', ['01', '02', '03', '04', '05'])
def test_demo01(case):
    time.sleep(1)
    print(f'执行测试用例-{case}')
    # assert 1 != 2
