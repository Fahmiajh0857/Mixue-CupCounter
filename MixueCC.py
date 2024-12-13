print("bags kemarin (400 500 700) !")
prev_bags = input("=> ")
prev_bags = prev_bags.split(" ")

print("display kemarin (400 500 700) !")
prev_disp = input("=> ")
prev_disp = prev_disp.split(" ")

print("bags sekarang (400 500 700) !")
curr_bags = input("=> ")
curr_bags = curr_bags.split(" ")

print("display sekarang (400 500 700) !")
curr_disp = input("=> ")
curr_disp = curr_disp.split(" ")

total = []
cup = ["cup 400", "cup 500", "cup 700"]

print("box yang dibuka (400 500 700) !")
box = input()
box = box.split(" ")

for i in range(3):
	total.append((int(prev_bags[i]) + (int(box[i]) * 20) - int(curr_bags[i])) * 50 + int(prev_disp[i]) - int(curr_disp[i]))
	
l = 0
for j in total:
	print(f"{cup[l]} = {j}")
	l += 1