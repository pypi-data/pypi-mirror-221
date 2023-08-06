import gevent
import pytest
from gevent import monkey
from pprint import pprint

monkey.patch_all()


def pytest_addoption(parser):
    # 创建pytest --help组
    group = parser.getgroup('dev16', 'manual pytest plugin')
    # 添加选项、默认参数、帮助说明
    group.addoption('--task', type=str, default='module',
                    help='Specify the type of task to be executed concurrently, you can fill in case or model, '
                         'the default is case')
    group.addoption('--concurrent', type=int, default=1,
                    help='Specify the number of concurrent tasks, the default is 1')


def pytest_runtestloop(session: pytest.Session) -> bool:
    """" 用于控制测试用例的执行 -- 根据不同task类型创建携程执行 """
    task_level = session.config.getoption('--task')
    print(f'获取传入的任务类型--task：{task_level}')

    if task_level == 'case':
        run_case(session)
    elif task_level == 'module':
        run_module(session)
    else:
        raise Exception('The task type is wrong, it can only be case or module')

    return True  # 用例执行完毕，不在执行其他模块 pytest_runtest_protocol


def run_task(items):
    """ 封装用例执行方法 """
    while len(items) != 0:
        item = items.pop()  # 取用例列表中最后一个，顺便移除，直到没有则终止
        item.ihook.pytest_runtest_protocol(item=item, nextitem=None)  # 执行用例


def run_case(session: pytest.Session):
    """ 以案例的维度进行执行用例 """
    concurrent = session.config.getoption('--concurrent')
    print(f'获取传入的并发用户数--concurrent：{concurrent}')
    print('session.items: ', session.items)  # 包含所有用例的列表
    # gs = []
    # for _ in range(concurrent):
    #     g = gevent.spawn(run_task, session.items)  # 使用gevent协程。将session.items装着用例的列表传给，执行方法
    #     gs.append(g)
    # 简化成推导式
    gs = [gevent.spawn(run_task, session.items) for _ in range(concurrent)]
    gevent.joinall(gs)  # 等待所有携程执行结束
    print('gs: ', gs)  # 携程执行结果
    pprint(gs)


def run_module(session: pytest.Session):
    """ 以模块的维度进行执行用例 不需要--concurrent """
    module_dict = {}
    for item in session.items:
        module = item.module
        # print('item.module：', module)
        # item.module： <module 'pythonProject2.testcases.test_demo01' from 'D:\\...\\testcases\\test_demo01.py'>
        # if module not in module_dict:
        #     module_dict[module] = []
        #     module_dict[module].append(item)
        # else:
        #     module_dict[module].append(item)
        # 替换常用方法：python 字典自带方法
        module_dict.setdefault(module, []).append(item)  # 在module_dict中，module列表没有就创建，有就返回该列表。再插入item
        # pprint(module_dict)  # 检查打印字典
    # 以模块数量做并发数，不用--concurrent
    # gs = []
    # for module_name, item in module_dict.items():
    #     gs.append(gevent.spawn(run_task, item))
    # 简化成推导式
    gs = [gevent.spawn(run_task, item) for module_name, item in module_dict.items()]
    gevent.joinall(gs)  # 等待所有携程执行结束


if __name__ == '__main__':
    # pytest.main(['--help'])  # 查看帮助信息 是否添加了 --task --concurrent
    print('====== -s ====================================')
    # pytest.main(['-s', '--task=case', '--concurrent=3'])  # 10 passed, 2 errors in 4.47s
    # pytest.main(['-s', '--task=case', '--concurrent=12'])  # 6 passed, 6 errors in 1.85s
    # pytest.main(['-s', '--task=module', '--concurrent=12'])  # 11 passed, 1 error in 6.96s

    print('====== -v ====================================')
    # pytest.main(['-v', '--task=case', '--concurrent=12'])  # 6 passed, 6 errors in 1.87s
    pytest.main(['-v', '--task=module', '--concurrent=1'])  # 11 passed, 1 error in 6.90s
