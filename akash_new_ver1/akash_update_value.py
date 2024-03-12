import requests

#new_value = int(input("Enter the new value: "))
new_value = 10  # Replace 10 with the new value you want to set for xx

# Send a POST request to update the value
response = requests.post('http://localhost:5000/update', json={'new_value': new_value})

print(response.text)
