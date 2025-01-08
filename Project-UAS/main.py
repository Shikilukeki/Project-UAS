from view import View
from process import Process

def main():
    view = View()
    process = Process()

    try:
        name, age = view.get_input()
        process.validate_input(name, age)
        data = process.create_data(name, age)
        view.display_result(data)
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
