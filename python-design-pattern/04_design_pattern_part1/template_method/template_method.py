# template
import sys
sys.stdout.reconfigure(encoding="utf-8")
from abc import ABCMeta, abstractmethod

# Template
class TestTemplate(metaclass = ABCMeta):
    def test(self):
        self.setup()
        self.execute()
        self.teardown()
        pass
    
    @abstractmethod # このアノテーションで抽象メソッドになる
    def setup(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    def teardown(self):
        print("teardown")
    
# Concrete Class
class ItemServiceTest(TestTemplate):
    def setup(self):
        print("setup ok")
    def execute(self):
        print("execute ok")
    
# Concrete Class
class UserServiceTest(TestTemplate):
    def setup(self):
        print("setup okk")
    def execute(self):
        print("execute okk")
        
        
if __name__ == "__main__":
    item = ItemServiceTest()
    user = UserServiceTest()
    
    print("====Item Test===")
    item.test()
    
    print("====User Test===")
    user.test()