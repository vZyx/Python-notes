
class EmployeesManager:
    def __init__(self):
        self.employees_names = []

    def add_employee(self, name):
        self.employees_names.append(name)

    def __len__(self):
        return len(self.employees_names)

    def __getitem__(self, idx):
        return self.employees_names[idx]

if __name__ == '__main__':
    mgr = EmployeesManager()
    mgr.add_employee('Mostafa')
    mgr.add_employee('Belal')
    mgr.add_employee('Ziad')


    for name in mgr:    # recall our get next / has next?
        print(name, end=' ')    # Mostafa Belal Ziad

    print(list(zip(mgr, mgr)))
