# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44
pages_book = 100
lines_page = 50
signs_line = 25
keep_sign = 4
byte_M = 1024 ** 2
disk_byte = disk * byte_M
book_byte = pages_book * lines_page * signs_line * keep_sign
amount_book = disk_byte // book_byte
print("Количество книг, помещающихся на дискету:", int(amount_book))
