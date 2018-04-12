## Python Mockito Demo

The purpose of this project is two fold:

- Demonstrate the power of the [mockito-python](https://github.com/kaste/mockito-python).
- A personal playing around project to learn more about testing in python

### Running The Project

To run the project ensure all the dependencies in `setup.py` are installed and simply execute: 

```bash
python mockito_demo/server.py
```

You can then hit the following endpoints:  

```bash
GET /hello
POST /hello
POST /worker/{job_type} #job_type = SumJob or LongJob
```

### Running the tests

All the tests are located in the test 