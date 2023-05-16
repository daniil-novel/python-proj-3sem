import my_package.module1
import my_package.module2
import json

if __name__ == "__main__":
    my_package.module1.hello()
    my_package.module2.bye()

    with open('my_package/my_json.json') as f:
        data = json.load(f)

    print(data)