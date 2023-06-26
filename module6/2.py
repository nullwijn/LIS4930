from datetime import datetime, timedelta

current_time = datetime.now()
updated_time = current_time - timedelta(seconds=60) + timedelta(days=365 * 2)
print(updated_time)
