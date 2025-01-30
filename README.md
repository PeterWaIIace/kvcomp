# kvcomp
Key-value comparison

KVcomp is simple tool comparing two json files based on their key-values. It has few benefits over text diffs as it does not care about order of the keys nor values. It can tell you exactly which values are different and which ones unique to one of two compared files.

# prerequsites:

KVcomp uses [uv](https://astral.sh/blog/uv) as package manager.

# How to run:

Just call:
```
uv run .\kvcomp.py .\test1.json .\test2.json
```

Example output:
```
Unique first JSON file content:
{
    "job": "Engineer"
}

Different values between JSON files:
{
    "age": 25,
    "city": "New York"
}

Unique second JSON file content:
{
    "name": "Alice",
    "hobby": "Reading"
}
```