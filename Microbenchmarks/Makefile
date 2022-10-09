CC=gcc
CXX=g++
program1=bench_1
program2=bench_2
program3=bench_3

all: $(program1) $(program2) $(program3)

$(program1) : bench_1.c
	mkdir -p bin
	$(CC) bench_1.c -o ./bin/$@

$(program2): bench_2.c
	mkdir -p bin 
	$(CC) bench_2.c -o ./bin/$@

$(program3): bench_3.c
	mkdir -p bin
	$(CC) bench_3.c -o ./bin/$@

clean-$(program1):
	rm -f ./bin/$(program1)

clean-$(program2):
	rm -f ./bin/$(program2)

clean-$(program3):
	rm -f ./bin/$(program3)

clean:
	rm -f ./bin/bench_*

