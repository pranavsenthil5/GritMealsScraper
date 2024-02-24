from datetime import datetime

with open('test.txt', 'w') as file:
    timestamp = datetime.now()
    formatted_timestamp = timestamp.strftime("%m%d%Y_%H%M%S")
    file.write(formatted_timestamp)