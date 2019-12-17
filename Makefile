## Make file for running required docker build commands prior to application commands
build:
	docker build -f prod-Dockerfile -t plangrid-homework .

build-nc: ## uses no cache to ensure a clean image
	docker build -f prod-Dockerfile -t plangrid-homework .

build-test: ## separate image for testing
	docker build -f test-Dockerfile -t plangrid-homework-test .

test: build-test ## Build the test container
	docker run -it plangrid-homework-test

run: build-nc ## Run the application
	docker run -itd -p 8000:8000 plangrid-homework

run-debug: build ## Run with debugging on on an alternate port
	docker run -it -p 8000:8000 --env LOGLEVEL=DEBUG plangrid-homework

.PHONY: test run run-debug