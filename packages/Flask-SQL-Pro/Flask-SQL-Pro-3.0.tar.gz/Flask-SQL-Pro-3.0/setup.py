from setuptools import setup, find_packages

setup(
    name='Flask-SQL-Pro',
    version='3.0',
    description='基于Flask-SQLAlchemy, 抽离SQL语句, 使用Jinja2语法实现动态SQL, 支持上下文事务, 支持分页',
    long_description=open('README.rst').read(),
    author='miaokela',
    author_email='2972799448@qq.com',
    maintainer='miaokela',
    maintainer_email='2972799448@qq.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'pyyaml',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
