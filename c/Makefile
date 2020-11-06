all:
	@echo 'Enter an option: clean merge_sort linked_list string style'

clean:
	rm -f merge_sort linked_list string *.orig

merge_sort:
	gcc -o merge_sort merge_sort.c
	./merge_sort

linked_list:
	gcc -o linked_list linked_list.c
	./linked_list

string:
	gcc -o string string.c
	./string

style:
	astyle -s4 --style=allman *.c
