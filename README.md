**# Python-Data-Structures**
Register a struct data like C++,

**# Eg1.**

    pack = ui.RegisterStructClass('a b c')(15, {}, [])
    pack.a += 50
    pack.b.update({0: 250})
    pack.c.append(100)
    print (pack.a, pack.b, pack.c)
**# Eg2.**

    def Transfer(self, c_pData):
		print(c_pData.szName, c_pData.lX, c_pData.lY)

    self.Transfer(ui.RegisterStructClass('szName lX lY')(GetName(), GetX(), GetY()))
