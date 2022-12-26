.PHONY: build run

build:
	docker build -t at-w3schools-tests .

run: build
	mkdir -p $$(pwd)/logs
	docker run --rm -i --name at-w3schools-tests -v $$(pwd)/logs:/app/logs -p 9000:9000 at-w3schools-tests
