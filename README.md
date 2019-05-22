
# What's the issue?
```c
SYSERR: Aug 22 18:36:42.624296 :: ReadEtcDropItemFile: No such an item (name:  Èò»ö  ´ó±â+) SYSERR:  
Aug 22 18:36:42.624379 :: Boot: cannot load ETCDropItem: locale/germany/etc_drop_item.txt
```
Some people fixed it long time ago by replacing the **column** name from **item_proto** (which is korean) with **vnum**.
<p align="center">
  <img src="https://i.gyazo.com/9adce9af6771f49f6ab51b91f505a597.png" width="292px" height="68px"/></p>

If you want to do it like this and don't want the source change (from below) *or* you don't have the source code of your game core. You can do a update query and copy the **vnum** to **name** just if the **vnum** from **item_proto** exists inside of **mob_proto.drop_item** by a specific mob.  

```sql
UPDATE player.item_proto SET name = vnum
	WHERE vnum IN (SELECT drop_item FROM player.mob_proto WHERE drop_item >= 10);  
# Affected rows: 83  
# Time: 35.919ms
```
# How can i know where the items are dropped?
So, the structure of *etc_drop_item.txt* is based on dropping a item with a probability from a specific mob where that mob have the ***item vnum*** attached in column ***mob_drop*** -> ***drop_item***.
```sql
SELECT DISTINCT locale_name, vnum, drop_item FROM player.mob_proto where drop_item >= 10;
```

| 	locale_name  	| 	vnum		|	drop_item	| 
| ----------------- | ------------- | ------------- |
| Wolf  			| 		102	  	| 	30028  		|
| Alpha Wolf		| 		103	  	| 	30069		|
| Alpha Blue Wolf 	| 		105	  	| 	30027		|
| Grey Wolf			| 		106	  	| 	30070		|

# How-To-Fix

 - [ ] Default structure:

| item_proto.name  | prob | 
| ------------- | ------------- |
| 늑대발톱  | 2.0  |
| 늑대발톱+  | 2.0  |
| 늑대털  | 2.0  |
| 멧돼지의 어금니  | 2.0  | 

 - [x] With the fix you can use both of methods.

| item_proto.[name or vnum]  | prob |
| ------------- | ------------- |
| 30028  | 2.0  |
| 30069  | 2.0  |
| 30027  | 2.0  |
| 멧돼지의 어금니  | 2.0  |
___
**Srcs/Server/game/src/itemitem_manager_read_tables.cpp**
```c
// Search for:
		if (!ITEM_MANAGER::instance().GetVnumByOriginalName(szItemName, dwItemVnum))
		{
			sys_err("No such an item (name: %s)", szItemName);
			fclose(fp);
			return false;
		}
// Replace with:
#ifdef ENABLE_FIX_READ_ETC_DROP_ITEM_FILE_BY_VNUM
		if (!ITEM_MANAGER::instance().GetVnumByOriginalName(szItemName, dwItemVnum))
		{
			str_to_number(dwItemVnum, szItemName);
			if (!ITEM_MANAGER::instance().GetTable(dwItemVnum))
			{
				sys_err("No such an item (name/vnum: %s)", szItemName);
				fclose(fp);
				return false;
			}
		}
#else
		if (!ITEM_MANAGER::instance().GetVnumByOriginalName(szItemName, dwItemVnum))
		{
			sys_err("No such an item (name: %s)", szItemName);
			fclose(fp);
			return false;
		}
#endif
```
-   **Srcs/Server/common/service.h**
```c
#define ENABLE_FIX_READ_ETC_DROP_ITEM_FILE_BY_VNUM
```
