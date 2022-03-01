class ContextManager(object):

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
        if exc_type is not None:
            print("  Exception:", exc_value)
            return True


with ContextManager():
    print("  Inside the with statement")
    print(1 / 0)

print("*" * 20)
from contextlib import contextmanager

# yield 之前的部分可以看成是 __enter__ 的部分，
# yield 的值可以看成是 __enter__ 返回的值，
# yield 之后的部分可以看成是 __exit__ 的部分
@contextmanager
def my_contextmanager():
    print("Enter")
    yield "my value"
    print("Exit")


with my_contextmanager() as value:
    print(value)
