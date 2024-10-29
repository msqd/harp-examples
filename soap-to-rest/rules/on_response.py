from harp.utils.bytes import ensure_bytes
from httpx import ByteStream
import json
import xmltodict
from collections import deque
from harp.http import HttpResponse

# response will be defined in the context in which this code is executed.
# cf https://docs.harp-proxy.net/en/0.7/apps/rules/on_response.html
response: HttpResponse
rest_body = xmltodict.parse(response.body)["soap:Envelope"]["soap:Body"]

# Recursive way would be better but we can't use it here in this context.
# Stack to hold dictionaries we need to process, starting with the top-level dictionary
stack = deque([(rest_body, rest_body)])

while stack:
    current_dict, parent_dict = stack.pop()

    # Dictionary to store cleaned key-value pairs at this level
    cleaned_dict = {}

    for key, value in current_dict.items():
        # Remove "m:" prefix if it exists, otherwise keep the original key
        new_key = key[2:] if key.startswith("m:") else key

        # Skip keys that start with "@"
        if new_key.startswith("@"):
            continue

        if isinstance(value, dict):
            # Clean nested dictionary in the same way
            cleaned_value = {
                k[2:] if k.startswith("m:") else k: v
                for k, v in value.items()
                if not k.startswith("@")
            }
            # Store the cleaned dictionary, push it to stack if it contains nested dictionaries
            cleaned_dict[new_key] = cleaned_value
            if cleaned_value:  # Push non-empty nested dictionaries onto the stack
                stack.append((value, cleaned_value))
        else:
            # Store the cleaned key-value pair for non-dictionary values
            cleaned_dict[new_key] = value

    # Update the parent dictionary with the cleaned entries at this level
    parent_dict.clear()
    parent_dict.update(cleaned_dict)

# Convert the fully processed dictionary to JSON
json_data = json.dumps(rest_body, indent=4)
response.stream = ByteStream(ensure_bytes(json_data))
