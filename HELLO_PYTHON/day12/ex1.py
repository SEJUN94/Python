from datetime import datetime


now = datetime.now()
ymd_hm = now.strftime("%Y%m%d_%H%M")
print(ymd_hm)