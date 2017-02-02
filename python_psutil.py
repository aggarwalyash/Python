import psutil
import datetime

cpu_time = psutil.cpu_times()
#Return system CPU times as a namedtuple.

cpu_percent = psutil.cpu_percent()
#Return a float representing the current system-wide CPU utilization as a percentage.

cpu_count = psutil.cpu_count(logical=True)
#Return the number of logical CPUs in the system. If logical is False return the number of physical cores only 

cpu_stats = psutil.cpu_stats()
#Return various CPU statistics as a namedtuple

cpu_freq = psutil.cpu_freq()
#Return CPU frequency as a nameduple including current, min and max frequencies expressed in Mhz.

disk_partitions = psutil.disk_partitions(all=False)
#Return all mounted disk partitions as a list of namedtuples

disk_usage = psutil.disk_usage('/')
#Return disk usage statistics about the given path as a namedtuple including total, used and free space expressed in bytes, plus the percentage usage.

boot_time = psutil.boot_time()
#Return the system boot time expressed in seconds

users = psutil.users()
#Return users currently connected on the system as a list of namedtuples

print(cpu_time)
print(cpu_percent)
print(cpu_count)
print(cpu_stats)
print(cpu_freq)
print(disk_partitions)
print(disk_usage)
print(boot_time)
print(users)