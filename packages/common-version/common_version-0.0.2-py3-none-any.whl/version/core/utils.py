import os


def gen_hash_key(key, seed=0):
    if isinstance(key, str):
        key = key.encode('utf8')
    assert isinstance(key, bytes)
    h = seed
    size = len(key)
    key_x4 = [key[i:i+4] for i in range(0, size, 4)]
    if len(key_x4[-1]) != 4:
        key = key_x4[-1]
        key_x4 = key_x4[:-1]
    else:
        key = b''
    for key_x4_item in key_x4:
        k = int(key_x4_item.hex(), 16)
        k *= 0xcc9e2d51
        k &= 0xffffffff
        k = (k << 15) | (k >> 17)
        k &= 0xffffffff
        k *= 0x1b873593
        k &= 0xffffffff
        h ^= k
        h = (h << 13) | (h >> 19)
        h &= 0xffffffff
        h = (h * 5) + 0xe6546b64
        h &= 0xffffffff
    if key:
        k = 0
        for key_item in reversed(key):
            k <<= 8
            k |= key_item
        k *= 0xcc9e2d51
        k &= 0xffffffff
        k = (k << 15) | (k >> 17)
        k &= 0xffffffff
        k *= 0x1b873593
        k &= 0xffffffff
        h ^= k
    h ^= size
    h ^= h >> 16
    h *= 0x85ebca6b
    h &= 0xffffffff
    h ^= h >> 13
    h *= 0xc2b2ae35
    h &= 0xffffffff
    h ^= h >> 16
    return h


def gen_pre_path(path, prefix='/mnt/disk/', disk_num=3, seed=0):
    assert '/' not in path
    key = gen_hash_key(path, seed)
    return os.path.join(prefix, "%02d" % (key % disk_num))
