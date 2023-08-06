from lark_oapi import JSON
from lark_oapi.core.model import EventContext

t = '{"challenge":"ebc4d296-187e-46e1-8bf3-e8a3a991d9a0","token":"oCyDEyApsZRk8DZ7UvvHrbSipoRpM6CM","type":"url_verification"}'
context = JSON.unmarshal(t, EventContext)
print("{\"challenge\":\"%s\"}" % context.challenge)
