all:
	@echo 'Enter an option: clean array linked_list string style'

clean:
	rm -f array linked_list string *.orig

array:
	gcc -o array array.c
	./array

linked_list:
	gcc -o linked_list linked_list.c
	./linked_list

string:
	gcc -o string string.c
	./string

style:
	astyle -s4 --style=allman *.c
