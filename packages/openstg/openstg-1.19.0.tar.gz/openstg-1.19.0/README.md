# OpenSTG

OpenSTG is a OpenSource STG implementation supporting the following protocols:

- PRIME

## Use only STG (responses webservice)

If you want to create a responses webservice is simple as:

```python
from openstg.config import STGStandAlone

application = STGStandAlone.create_app()
```

Then you can use this app in WSGI. If you want you have `stgapp.py` ready to use.
