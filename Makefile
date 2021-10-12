PY = py

run:
	$(PY) ./src/main.py	./examples/$(example)

asm:
	$(PY) ./src/test.py