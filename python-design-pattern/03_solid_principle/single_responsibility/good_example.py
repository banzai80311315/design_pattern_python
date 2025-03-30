import sys
sys.stdout.reconfigure(encoding="utf-8")

class EmployeeData:
    def __init__(self , name: str , department : str):
        self.name = name
        self.department = department
        
class EmployeeRepository(EmployeeData):
    def __init__(self, name: str, department: str):
        super().__init__(name, department)  # 親クラスの __init__ を明示的に呼ぶ

    def save(self):
        print(f"{self.name}（{self.department}）のデータを保存しました。")
        
class HourReporter(EmployeeData):
    def __init__(self, name: str, department: str):
        super().__init__(name, department)  # 親クラスの __init__ を明示的に呼ぶ
        
    def __getRegularHours(self):
        print("労働時間レポート専用の労働時間計算ロジック")

    def reportHours(self):
        self.__getRegularHours()
        print(f"{self.name}（{self.department}）の労働時間をレポートしました。")
        
class PayCalculator(EmployeeData):
    def __init__(self, name: str, department: str):
        super().__init__(name, department)  # 親クラスの __init__ を明示的に呼ぶ
        
    def __getRegularHours(self):
        print("給与計算専用の労働時間計算ロジック")

    def calculatePay(self):
        self.__getRegularHours()
        print(f"{self.name}（{self.department}）の給与を計算しました。")
        
class Engineer(EmployeeRepository):
    pass

class HRDepartment(HourReporter):
    pass

class AccountingDepartment(PayCalculator):
    pass

if __name__ == "__main__":
    # employee_data = EmployeeData("Suzuki", "develop")
    pay_calculator = PayCalculator("Suzuki", "develop")
    hour_reporter = HourReporter("Suzuki", "develop")

    print("経理部門")
    pay_calculator.calculatePay()

    print("")
    print("人事部門")
    hour_reporter.reportHours()
