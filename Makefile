all:
	chmod +x run.py
	./run.py

clean:
	@echo 'Removing assembly files.'
	rm *.s
