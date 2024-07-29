rooms=[1,2]
status=[]
n=len(rooms)
for i in range(n):
    print(f"Is room {i} clean[0] or dirty[1]?")
    status.append(int(input()))
    # if status[i]!=1 or status[i]!=0:
    #     print("Invalid Input Detected")
    #     break;

for i in range(n):
    if status[i]==1:
        print(f"Room {rooms[i]} is dirty")
        print("Cleaning...")
        status[i]=0
    else:
        print(f"Room {rooms[i]} is clean")
    print("Moving to next room")
if 1 not in status:
    print("All rooms are clean\nProgram Exiting")