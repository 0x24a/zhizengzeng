<h1 align="center">ZhiZengZeng-Python-SDK</h1>
<p align="center">
<em>✨A simple OpenAI-like SDK for ZhiZengZeng AI.✨</em>
</p>


# Quickstart
Install using pip:
This will install ZhiZengZeng Python SDK with minimal (pure Python) dependencies.
```
$ pip3 install zhizengzeng
```
Create an application, in example.py:
```
from zhizengzeng import ZhiZengZeng
client = ZhiZengZeng(api_key="YOUR_API_KEY")
print("GPT says 1+1="+client.completions.create(model="gpt-3.5-turbo-instruct", prompt="1+1=2\n2+2=4\n4+4=8\n1+1=",max_tokens=1).choices[0].text)
```
Remember to replace `YOUR_API_KEY` to your real ZhiZengZeng(Not OpenAI!) token.  
If nothing was wrong, You should see `GPT says 1+1=2` in your console.

# Usage
Most API calls are made in the same way as OpenAI (see [here](https://github.com/openai/openai-python/blob/e41abf7b7dbc1e744d167f748e55d4dedfc0dca7/api.md)), and are listed here only in relation to the OpenAI, only the different/additional APIs are listed here.

## Get Balance
The Balance API allows you to get the balance of your account (in CNY), which can be called in two ways.
### Using property
```python
from zhizengzeng import ZhiZengZeng
client = ZhiZengZeng(api_key="YOUR_API_KEY")
print("Account balance: " + str(client.balance)) #Balance is float type!
```
### Using get_balance()
```python
from zhizengzeng import ZhiZengZeng
client = ZhiZengZeng(api_key="YOUR_API_KEY")
print("Account balance: " + str(client.get_balance())) #Balance is float type!
```

# Requirements
Python 3.7 or higher.