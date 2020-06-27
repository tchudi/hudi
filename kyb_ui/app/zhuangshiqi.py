# def hi(name='kobe'):
#     def greet():
#         print('greet  fun() ')
#     def welcome():
#         print('welcome fun()')
#
#     if name=='kobe':
#         return greet
#     else:
#         return welcome
#
# hi(name='james')()

#
# def foo():
#     print('foo')
#
# def bar(func):
#     func()
# bar(foo)

import logging
import logging.config

CON_LOG=r'D:/kyb_ui/config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

# def foo():
#     print('i an foo')
#     logging.info('foo is running')
# foo()


# def use_logging(func):
#     logging.info('%s is running'%func.__name__)
#     return func()
#
# def greet():
#     print('i am greet')
#
# use_logging(greet)


# def use_logging(func):
#     def wrapper():
#         logging.warn('%s is running'%func.__name__)
#         return func()
#
#     return wrapper

# def foo():
#     print('i am foo')
#
# foo=use_logging(foo)
# foo()

# @use_logging
# def foo():
#     print('i am foo')
# foo()


def use_logging(func):
    def wrapper(*args):
        logging.info('%s is running'%func.__name__)
        return func(*args)
    return wrapper


@use_logging
def foo(args):
    print('i am %s'%args)
t=('kobe','basketball')
foo(t)

