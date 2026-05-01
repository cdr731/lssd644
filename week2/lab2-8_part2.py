# Lab 2-8 Part 2 by Chris Reutz
lab2items = ['Books', 3.14, 'Pencils', 'Cars', 'Balloons']
lab2items.append([1,2,3])
lab2items.append('Yahoo')
lab2items.append(True)
rm_item=lab2items[1]
del lab2items[1]
print('Part 2 items now include: ', lab2items)
print(f'I removed {rm_item} from the list')