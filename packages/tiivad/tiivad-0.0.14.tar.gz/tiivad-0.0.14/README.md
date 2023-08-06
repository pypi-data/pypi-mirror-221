# Setup
* Use Python 3.10
* Install requirements from requirements.txt

# Run validation
```

```

# Running tests:
```
# All tests
python -m pytest
# For one file
python -m pytest test/test_file.py
```

# Packaging:
* Remove the old versions from `dist` folder.
* Change the version in `tiivad/version.py` and run:
```
python setup.py sdist
```

# Laeme uue versiooni üles:
```
python -m twine upload dist/* 
```

# PyPi repo asukoht:
https://pypi.org/project/tiivad/

# Local run/test with Docker
## Let's rename the image with -t .
```
cd docker
docker build --progress plain --no-cache -f tiivad-base -t tiivadbase1 .
```

## Let's build the second container with assessment code and sample solution
```
cd docker
docker build --progress plain --no-cache -f dockerfile-evaluate -t evaluate1 .
```

## Get docker images
```
docker images
```

## Run the latest evaluate container and name it "evaluator"
```
docker run -it --name evaluator evaluate1 /bin/bash
```

### Inside the container run:
```
./evaluate.sh
```

## Print the logs (outside the container, another terminal)
```
docker logs evaluator
```
