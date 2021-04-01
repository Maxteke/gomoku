##
## EPITECH PROJECT, 2021
## gomoku
## File description:
## gomoku Makefile
##

NAME		:=
ifeq ($(OS),Windows_NT)
	NAME +=	pbrain-gomoku-ai.exe
else
	NAME +=	pbrain-gomoku-ai
endif

gomo:	$(NAME)

$(NAME):
ifeq ($(OS),Windows_NT)
	copy pbrain-nazo.py pbrain-gomoku-ai.exe
else
	cp pbrain-nazo.py pbrain-gomoku-ai
	chmod 755 pbrain-gomoku-ai
endif


all:	gomo

clean_gomo:
ifeq ($(OS),Windows_NT)
	del pbrain-gomoku-ai.exe
else
	rm -rf pbrain-gomoku-ai
endif

clean:	clean_gomo

fclean_gomo:	clean_gomo

fclean: fclean_gomo

re_gomo:	fclean_gomo gomo

re: re_gomo