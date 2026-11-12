#Server Health Report Generator

"""This is a small tool where I enter a server’s name and its CPU, memory and disk usage. 
It then prints a one-page report showing how much of each is used and free, 
the average load, and the time of the check. 
It saves the team from writing this summary by hand every time."""

from datetime import datetime

server_name= input("Server name: ")
environment= input("dev/test/prod: ")
cpu_used= float(input("CPU used (%): "))
memory_used= float(input("Memory used (%): "))
disk_used= float(input("Disk used (%):"))

def calculate_health(cpu, memory, disk):
    result= {
        "cpu_free" : round(100 - cpu, 1),
        "memory_free" : round(100 - memory, 1),
        "disk_free" : round(100 - disk, 1),
        "average_load" : round((cpu + memory + disk)/3, 1)
    }
    return result

health = calculate_health(cpu_used, memory_used, disk_used)

now = datetime.now()
report_time= now.strftime("%Y-%m-%d %H:%M:%S")

print(
    "-----------SERVER HEALTH REPORT CARD-----------".title(),
    f"Server        : {server_name}",
    f"Environment   : {environment}",
    f"Checked at    : {report_time}",

    f"CPU           : {cpu_used} % used | {health["cpu_free"]} % free",
    f"Memory        : {memory_used} % used | {health['memory_free']} % free",
    f"Disk          : {disk_used} % used | {health['disk_free']} % free",
    f"Average Load  : {health["average_load"]} %",

    sep= "\n"
)