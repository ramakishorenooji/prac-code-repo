import json

  # TODO implement
def add_ele(a, b):
    body = "Hello i am learning API gateway technology"
    (res) = (a+b)
    statusCode = 200
    res = str(res)
    return {
        'statusCode': 200,
        'body': json.dumps(res + body),
        "headers": {
            "Content-Type": "application/json"
            }
    }
result = add_ele(10, 20)
print(result)