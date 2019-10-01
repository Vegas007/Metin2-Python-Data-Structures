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
    def Transfer(self, p):
		print(p.szName, p.lX, p.lY)

    self.Transfer(RegisterStructClass('szName lX lY')(GetName(), GetX(), GetY()))
```
**# Example #3.**
```py
config = ui.RegisterStructClass('width height default_size_dict rank_list text')(450, 300, {'w': 400, 'h': 500}, [1, 2, 3], 'Metin2')

print (
	config.width, config.height, config.text,
	config.default_size_dict.get('w'), config.default_size_dict.get('h'),
	config.rank_list
)
```
