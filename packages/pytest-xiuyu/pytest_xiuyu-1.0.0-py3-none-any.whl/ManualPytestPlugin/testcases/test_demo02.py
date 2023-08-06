import time
import pytest


@pytest.mark.parametrize('case', ['11', '12', '13', '14', '15', '16', '17'])
def test_demo03(case):
    time.sleep(1)
    print(f'执行测试用例-{case}')

