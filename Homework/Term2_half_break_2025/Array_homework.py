
birdname = ["robin","blackbird","pigeon","magpie","bluetit","thrush","wren","starling"]

print(birdname)
bird = input("Enter the name of the bird:")
bird = bird.lower()

try:
    birdname.index(bird) in birdname
    index = birdname.index(bird)
    print("Bird found at index ",index)
except:
    print("Bird not found")