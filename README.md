# Tapioca TeamCulture

## Installation
```
pip install tapioca-teamculture
```

## Documentation

### Instantiating the Client
``` python
from tapioca_teamculture import TeamCulture
api = TeamCulture(token='your_token', dev=True)

```

## Get Users - paginated
``` python
from tapioca_teamculture import TeamCulture

api = TeamCulture(token='your_token', dev=True)
users = api.users().get(params={'offset': 0, 'limit': 10})

for user in users().pages(max_pages=2):
    print(user)

```

## Get Groups - doesn't support pagination
``` python
from tapioca_teamculture import TeamCulture

api = TeamCulture(token='your_token', dev=True)
groups = api.groups().get()

print(groups)

```

## Get Action Plans - paginated
``` python
from tapioca_teamculture import TeamCulture

api = TeamCulture(token='your_token', dev=True)
action_plans = api.action_plans().get(params={'page': 1, 'perPage': 10})

for action_plan in action_plans().pages(max_pages=2):
    print(action_plan)

```

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
