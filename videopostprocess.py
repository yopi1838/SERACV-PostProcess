import cv2
import glob
img_array = []
foldername = "Movie_damage_4percent_mscale1e-6"
target_filename = "damage_4percent_mscale1e-6"
time = 0
count=0
for filename in glob.glob("./{}/*.png".format(foldername)):
    time += 1e-3
    if count % 5 != 0:
        count +=1
        continue
    # describe the type of font
    # to be used.
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread(filename)
    cv2.putText(img, 
                "dyna_time : "+str(round(time,3)) + " s", 
                (900, 100), 
                font, 1, 
                (0, 0, 0), 
                2, 
                cv2.LINE_4)
    h,w,l = img.shape
    size = (w,h)
    img_array.append(img)
    count +=1
    pass

out = cv2.VideoWriter("{}.mp4".format(target_filename),cv2.VideoWriter_fourcc(*'mp4v'),30,size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
