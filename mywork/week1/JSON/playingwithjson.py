# Playing with JSON.
# PFDA - Topic 1 - getting started
# Author: Ermelinda Qejvani
# Based on lectures by Andrew Beatty

import json
data = {
    'name':'joe',
    'age':21,
    "student": True
}
jsonString = json.dumps(data)
print(data)
print(jsonString)
