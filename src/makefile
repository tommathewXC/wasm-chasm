all: clean build

build:
	emcc main.cpp --emrun -s WASM=1 -o ../server/public/test.html

clean:
	rm -rf ../server/public/*