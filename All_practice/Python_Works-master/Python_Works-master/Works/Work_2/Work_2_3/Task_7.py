s = 50; print(bool([i for i in range(2) if s % sum(list(map(int, list(str(s))))) == 0 and i == 1 or i == 0 and s % sum(list(map(int, list(str(s))))) != 0][0]))
