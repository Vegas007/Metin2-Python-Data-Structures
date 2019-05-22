**# Python-Data-Structures**
----------
**# Example #1**
```py
    pack = RegisterStructClass('a b c')(15, {}, [])
    pack.a += 50
    pack.b.update({0: 250})
    pack.c.append(100)
    print (pack.a, pack.b, pack.c)
```
**# Example #2.**
```py
    def Transfer(self, c_pData):
		print(c_pData.szName, c_pData.lX, c_pData.lY)

    self.Transfer(RegisterStructClass('szName lX lY')(GetName(), GetX(), GetY()))
```
