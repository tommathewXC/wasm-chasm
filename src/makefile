all: clean test main

test:
	@echo "Making test page and test js + wasm"
	@emcc test.cpp --emrun -s WASM=1 -o ../server/public/test.html

main:
	@echo "Making maing wasm binaries"
	@emcc -O3 -s WASM=1 -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap"]' main.cpp
	@mv a.out.js ../server/public/main.js
	@mv a.out.wasm ../server/public/main.wasm


clean:
	@echo "Cleaning"
	@rm -rf ../server/public/*js
	@rm -rf ../server/public/*wasm
	@rm -rf ../server/public/test.html