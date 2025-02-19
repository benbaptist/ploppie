```python 
from ploppie import Utility

utility = Utility(
    model="gpt-4o-mini"
)

response = utility.json(
    prompt="Create a weather report for the next 7 days in JSON format.",
    data="The weather in San Francisco is sunny and 60 degrees. After that, it will be cloudy and 55 degrees. The following days will be thunderstorming, with temperatures ranging from 45 to 50 degrees linearly.",
    schema={
        "type": "object",
        "properties": {
            "weather": {"type": "string"},
            "temperature": {"type": "number"},
        },
    },
    attempts=3,
    hard_validation=True
)

print(response)
```