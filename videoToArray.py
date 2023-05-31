import skvideo.io  
videodata = skvideo.io.vread("/Users/Shanmukha/Desktop/services/videoClustering/kapil1.mp4")  
print(videodata.shape, type(videodata))