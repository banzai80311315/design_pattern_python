# これは「委譲 (Delegation)」と呼ばれるデザインパターンに近い
# - EmployeeData のインスタンスを 引数として受け取る だけで、PayCalculator が直接 EmployeeData を持たない
# - EmployeeData にあるデータを利用するが、PayCalculator 自体は EmployeeData のメンバではない
# - 必要な時だけ EmployeeData を参照する（「計算のために一時的にデータを借りる」イメージ）

# 継承を使うべきなのは？

# PayCalculator が EmployeeData の一部として機能する場合

# 例えば、給与計算が 全社員に共通する基本機能 の場合（PayCalculator は EmployeeData の子クラスにするべき）

# 集約を使うべきなのは？

# PayCalculator が EmployeeData のインスタンスを保持 して、複数回使う場合

# 例えば、PayCalculator が特定の従業員の給与計算を管理し続ける場合

# 委譲を使うべきなのは？

# PayCalculator が EmployeeData を保持せず、一時的に計算に使うだけ の場合（今回のケース）

# 例えば、「給与計算システム」と「従業員データ」は独立しているが、計算時にデータを受け取って処理する」 という設計にしたいとき


class EmployeeData:
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self):
        print("給与計算専用の労働時間計算ロジック")

    def calculate_pay(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の給与を計算しました")


class HourReporter:
    def __get_regular_hours(self):
        print("労働時間レポート専用の労働時間計算ロジック_V2")

    def report_hours(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の労働時間をレポートしました")


class EmployeeRepository:
    def save(self):
        pass


if __name__ == "__main__":
    employee_data = EmployeeData("Suzuki", "develop")
    pay_calculator = PayCalculator()
    hour_reporter = HourReporter()

    print("経理部門")
    pay_calculator.calculate_pay(employee_data)

    print("")
    print("人事部門")
    hour_reporter.report_hours(employee_data)
