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

p004: p004.c
	$(CC) utils.c p004.c -o p004.o

p005: p005.c
	$(CC) p005.c -o p005.o

p006: p006.c
	$(CC) p006.c -o p006.o

p007: p007.c
	$(CC) utils.c p007.c -o p007.o

p009: p009.c
	$(CC) p009.c -o p009.o

p010: p010.c
	$(CC) utils.c p010.c -o p010.o

p012: p012.c
	$(CC) utils.c p012.c -o p012.o

p015: p015.c
	$(CC) p015.c -o p015.o -lgmp

clean:
	$(RM) *.o