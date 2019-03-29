CC = gcc
RM = rm -f

default: all

all:


# $< takes first dependency name and $@ takes target name
# target: dependencies

p001.o: p001.c
	$(CC) $< -o $@

p002.o: p002.c
	$(CC) p002.c -o p002.o

p003.o: p003.c
	$(CC) utils.c $< -o $@

p004.o: p004.c
	$(CC) utils.c $< -o $@

p005.o: p005.c
	$(CC) $< -o $@

p006.o: p006.c
	$(CC) $< -o $@

p007.o: p007.c
	$(CC) utils.c $< -o $@

p008.o: p008.c
	$(CC) utils.c $< -o $@

p009.o: p009.c
	$(CC) $< -o $@

p010.o: p010.c
	$(CC) utils.c $< -o $@

p012.o: p012.c
	$(CC) utils.c $< -o $@

p014.o: p014.c
	$(CC) utils.c $< -o $@

p015.o: p015.c
	$(CC) $< -o $@ -lgmp

p016.o: p016.c
	$(CC) $< -o $@ -lgmp

p039.o: p039.c
	$(CC) $< -o $@

clean:
	$(RM) *.o