FLAGS = -lm
CFLAGS= -pg -O3 -Wall -lgmp
CXXFLAGS= -pg -O3 -Wall -lgmp
CC=mpicxx
CXX=mpicxx
RM=rm

PROGRAM_NAME= mandelbox

$(PROGRAM_NAME): main.o print.o timing.o savebmp.o getparams.o 3d.o getcolor.o distance_est.o mandelboxde.o raymarching.o renderer.o init3D.o
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)

run-serial: $(PROGRAM_NAME)
	python params.py;
	python runMe.py 1;

run-parallel: $(PROGRAM_NAME)
	python params.py;
	python runMe.py 32;


clean:
	$(RM) *.o $(PROGRAM_NAME)$(EXEEXT) 
