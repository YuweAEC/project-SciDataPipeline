install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	black src/

all: compile_fortran

compile_fortran:
    gfortran -o process_data src/process_data.f90

clean:
    rm -f process_data
