import os
SERVER=os.environ.get("MONITOR_SERVER",default="edgex-core-data")
PORT=os.environ.get("MONITOR_PORT",default="59880")
PATH=os.environ.get("MONITOR_PATH",default="/api/v3/event/device/name")
TELEGRAM_CHANNEL_ID=os.environ.get("MONITOR_TELEGRAM_CHANNEL_ID",default="")
TELEGRAM_TOKEN=os.environ.get("MONITOR_TELEGRAM_TOKEN",default="")
DEVICES=['iotnode1','iotnode2','iotnode3']
POOL_SIZE=5
