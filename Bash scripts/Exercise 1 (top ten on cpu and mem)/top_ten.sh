ps -eo user,pid,cmd,%cpu --sort=-%cpu | head
ps -eo user,pid,cmd,%mem --sort=-%mem | head
