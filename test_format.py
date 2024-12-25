import json

with open("prediction.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        try:
            impid, ranks = line.strip('\n').split()
            ranks = json.loads(ranks)  # Kiểm tra JSON
        except Exception as e:
            print(f"Error at line {i}: {line}")
            print(f"Exception: {e}")
