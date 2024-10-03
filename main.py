from payroll import Developer, Manager

def main():
    developer = Developer(name="John Smith", age=30, salary=5000, is_happy=True,
                          language="Python", position="Senior Developer", company="Tech Corp")

    manager = Manager(name="Jane Doe", age=40, salary=7000, is_happy=False,
                      department="IT", position="Project Manager", company="Tech Corp")

    print("=== Developer Information ===")
    print(developer.get_data())
    developer.display_summary()
    print(developer.get_job_details())
    print()

    print("=== Manager Information ===")
    print(manager.get_data())
    manager.display_summary()
    print(manager.get_job_details())

    print("\n=== Salary Raise for Developer ===")
    developer.salary_raise(10)
    developer.display_summary()

    print("\n== Salary Raise for Manager ===")
    manager.salary_raise(20)
    manager.display_summary()

if __name__ == '__main__':
    main()
