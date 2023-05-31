from videohash import VideoHash
url1 = "kapil1.mp4"
videohash1 = VideoHash(path=url1)

url2 = "kapil3.mp4"
videohash2 = VideoHash(path=url2)
videohash2 - videohash1

print(videohash2 - videohash1, videohash1, videohash2)

print(videohash2.is_similar(videohash1))
