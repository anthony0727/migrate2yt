# migrate2yt

env
* pipenv

framework:
* PyQt5
* tensorflow

lib:
* BeautifulSoap

api:
* youtube data python API

pattern:
* classic MVC

## dev note

**how to parse text containing yt links?**

- [x] BeautifulSoap
- [ ] regex

why? I trust in BS

**how to get user's likes from genie/melon?**

- [x] crawl
- [ ] genie/melon APIs

why? their API sucks and changes instantaneously

**coroutine vs celery**

i dunno.

but must take in to consideration, 

since 10000 likes will lead to 10000 requests

maybe or maybe not.

