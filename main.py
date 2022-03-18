import person as pr

def main():
    name("Дастан")
    person = pr.Person("Name")
    print(person.info())


def name(last_name) -> str:
    print(last_name)

if __name__ == "__main__":
    main()