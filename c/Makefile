TARGETS=linked_list merge_sort primes queue select string

all:
	@echo 'Enter an option: clean style <target>'

clean:
	rm -f *.orig $(TARGETS)

style:
	astyle -s4 --style=allman *.c

$(TARGETS):
	gcc -o $@ $@.c
	./$@
