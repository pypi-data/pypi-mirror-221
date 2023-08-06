from setuptools import setup, find_packages

setup(
    name='pytest-xiuyu',                                            # 包名
    # packages=["ManualPytestPlugin"],                              # 指定包含的包
    packages=find_packages(),                                       # 自动搜寻包 find_packages() 自动在setup.py同级目录下找报的名称
    version='1.0.0',                                                # 指定版本号
    include_package_data=True,                                      # 是否包含数据文件
    description="This is a pytest plugin",                          # 简要描述信息
    long_description=open('README.md', encoding='utf-8').read(),    # 详细描述信息  setup.py统计目录
    long_description_content_type="text/markdown",                  # 指定详细描述的信息的格式
    author='TonyGao',                                               # 指定作者
    author_email='5942527@qq.com',  # 作者邮箱
    url='https://github.com/TonyGao2527/pytest-xiuyu',  # 指定项目地址

    # 配置pytest插件模块
    # 1.配置pytest插件的入口  ["包名＝路径"]
    # 2.配置pytest插件模块的名称
    entry_points={"pytest16": ["pytest-xiuyu = ManualPytestPlugin.conftest"]},
    # 3.配置pytest模块的分类 参考https://pypi.org/project/aiohttp/ 页面左侧的Classifiers 左侧 双冒号代替等号，可传多个值，放入列表中。
    classifiers=["Development Status :: 5 - Production/Stable"],
)

"""
在 setup.py 文件所在的目录下运行以下命令，同级目录创建分发包dist文件夹：
运行命令 python setup.py sdist
    生成 dist/xxxx.tar.gz压缩文件    
运行命令 python setup.py sdist bdist_wheel  (提前安装 pip install wheel)
    生成 dist/xxxx..whl 压缩文件：
在 PyPI 存储库中，.tar.gz 文件和 .whl 文件都是 Python 软件包的常见格式。
    .tar.gz 文件是源代码发布文件。.tar.gz 文件是原始的 Python 代码和源代码文件的压缩包，它需要在目标计算机上执行安装过程才能编译和安装。
    .whl 文件则是编译安装文件,编译为二进制字节码的文件，里面是pyc文件。.whl 文件已经被编译，可以直接在目标计算机上执行安装，无需重新编译，安装速度更快。
    
    因此，默认情况下，对于 Windows 系统，较新的 Python 发行版更倾向于使用 .whl 文件，
    而对于 Linux，仍然更倾向于使用 .tar.gz 文件。


如果需要将当前的包发布到pypi官方仓库中
1.安装twine
pip install twine

2.将dist/*发布到官方仓库
终端进入dist同级目录 运行命令 twine upload dist/*


"""
