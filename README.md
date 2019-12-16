# JSON basics

## Definition of JSON
Java Script Object Notation
--> is usually a dictionary

However confusingly an object in JS is the data type for both lists (arrays) and dictionairies (hash)

## Create a JSON file

### json.dumps(obj) --> string json

### json.dump(obj, file) --> writes json in file 

## Make post request with JSON
you need:
- path
- json 
- headers

##Task
Make a small program that requests 3 postcodes using POST and returns something like
```buildoutcfg
> 1 - Postcode: xyzpto with nhs location at: xyz
> 2 - Postcode: xyzpto2 with nhs location at: xyz
> 3 - "       "         "      "          "      "
```

