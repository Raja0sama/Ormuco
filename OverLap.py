def didOverlaps(a,b):
    if b[0] > a[0] and b[0] < a[1]:
        return True
    else:
        return False
        
print (didOverlaps([1,5],[6,8]))

