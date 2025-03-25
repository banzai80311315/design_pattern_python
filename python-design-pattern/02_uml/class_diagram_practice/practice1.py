class Employee:
    """Employee class"""         # 三重クォートによるコメント

    # コンストラクタ
    def __init__(self , emp_id: int , name_id: str , salary : int):
        self.__emp_id = emp_id
        self.__name = name_id
        self.__salary = salary

    def _work(self) -> None:
        print("働きます")
    
    # get,set
    def getSalary(self) -> int:
        return self.salary
    
    def setSalary(self, salary) -> None:
        self.salary = salary