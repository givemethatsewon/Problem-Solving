n, target = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = sum(lessons)

while start <= end:
    disk_len = (start + end) // 2
    
    disks = 1
    x = 0
    for lesson in lessons:
        x += lesson
        if x == disk_len:
            disks += 1
            x = 0
        elif x > disk_len:
            disks += 1
            x = lesson
    if x == 0:
        disks -= 1
    
    if disks > target:
        start = disk_len + 1
    else:   #disks <= target
        ans = disk_len
        end = disk_len - 1

print(ans)