#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

index = sorted(dir(hidden_4))
for index, item in enumerate(index):
    if item[:2] != '__':
        print("{}".format(item))
