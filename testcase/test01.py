import pytest

class Test_09:
    def __int__(self,num):
        self.num = num
    def test001(self):
        print(self.num)
        pass
    def test002(self):
        print(self.num)
        pass


if __name__ == '__main__':
    pytest.main(["Test_09","-vs"])