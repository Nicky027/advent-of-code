OBJS	= main.o utils.o packet.o
SOURCE	= main.cpp utils.cpp packet.cpp
HEADER	= utils.h packet.h
OUT	= day_16
CC	 = g++
FLAGS	 = -g -c -Wall


all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)


main.o: main.cpp
	$(CC) $(FLAGS) main.cpp -std=c++17

utils.o: utils.cpp
	$(CC) $(FLAGS) utils.cpp -std=c++17

packet.o: packet.cpp
	$(CC) $(FLAGS) packet.cpp -std=c++17

clean:
	rm -f $(OBJS) $(OUT)

run: $(OUT)
	./$(OUT)