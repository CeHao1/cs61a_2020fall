
V=pi/3 # vision
position.X=[] # a list to store X position of points
position.Y=
position.angle=[]#store angles of points
pts=[] # how many points can be observed

for i in range(position.X.length):
    position.angle.append(np.arctan2(position.Y[i],position.X[i]))

for i in range(position.X.length):
    alpha=position.angle[i]
    temp=0
    for j in range(position.X.length):
        if alpha>position.angle[j] and alpha-V<position.angle[j]:
            temp+=1
        pts.append(temp)

max_pts=max(pts)
max_angle=argmax(max_pts)
