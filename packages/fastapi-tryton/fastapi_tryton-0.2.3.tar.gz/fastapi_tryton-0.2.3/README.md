
# README.md
This file is part of fastapi_tryton. The COPYRIGHT file at the top level of this repository contains the full copyright notices and license terms.

# FastAPI-Tryton

Adds Tryton support to FastAPI application.

By default transactions are readonly except for PUT, POST, DELETE and PATCH
request methods.
It provides also 2 routing converters `record` and `records`.

Setting the `configure_jinja` flag adds the following filters on jinja
templates: `numberformat`, `dateformat`, `currencyformat` and
`timedeltaformat`. The filters apply the same formatting as Tryton reports.

## Nutshell

TODO: Add examples of use, and docs, all collaboration is welcome!,
but for now you can see test_api.py file where there is examples ;)

## Installation
You can install the package using `pip`.

```bash
pip install fastapi_tryton
```

## Usage

```python
# main.py
from fastapi import FastAPI
from fastapi_tryton import Tryton, Settings

app = FastAPI()
app.settings = Settings(
    tryton_db=dbname,
    tryton_user=None,
    tryton_config=config
)
tryton = Tryton(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Deployment
You can deploy your FastAPI application using Uvicorn.
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## License
GPL-3.0 License

## Contributors
- PRESIK SAS, gerente@presik.com
