#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[name][0:2] != "__":
            print(dir(hidden_4)[name])
