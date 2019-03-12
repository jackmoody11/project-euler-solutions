CC = gcc
RM = rm -f

default: all

all:

p001: p001.c
	$(CC) p001.c -o p001.o

p002: p002.c
	$(CC) p002.c -o p002.o

p003: p003.c
	$(CC) utils.c p003.c -o p003.o

p005: p005.c
	$(CC) p005.c -o p005.o

p006: p006.c
	$(CC) p006.c -o p006.o

p007: p007.c
	$(CC) utils.c p007.c -o p007.o

clean:
	$(RM) *.o