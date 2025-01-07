# Change the path based on your installation folder.
CPX_PATH = /home/koenig/ibm/ILOG/CPLEX_Studio2211/cplex

CC = g++-10
ARCH = x86-64_linux

cpx: 
	$(CC) -g -L $(CPX_PATH)/lib/$(ARCH)/static_pic/ -L lib/ -I $(CPX_PATH)/include/ilcplex/ -o get_cuts get_cuts.cpp -lm -lcplex -ldl -lpthread

