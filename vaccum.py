status=[]
n=int(input("How many rooms: "))
rooms=list(range(1,n+1))
for i in range(n):
    print(f"Is room {rooms[i]} clean[0] or dirty[1]?")
    status.append(int(input()))
    if status[i] not in [0,1]:
        print("Invalid Input Detected")
        break;

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