""" This program notifies someone to take a break after each two hours of continuouslyusing a computer. During the break, a web browser is opened and plays music"""
import webbrowser
import time

total_breaks=3
total_count=0

print("This program started on " + time.ctime())
while (total_count < total_breaks):
	print("This is count  %d "%total_count)
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=UONnRMuuDps")
	total_count=total_count + 1