import sys
import ctypes


def generate_groups(string,maxNumber,year,exception = 0):
    result = []
    for i in range(0,len(string),1):
        result.append([]);
        for j in range(1,maxNumber[i]+1,1):
            if j in exception[i]:
                result = result
            else:
                result[i].append(string[i]+"-"+str(j)+"-"+str(year))
    return result


def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    output = sep.join(str(arg) for arg in args) + end
    file.write(output)
    if flush:
        file.flush()


def decrypt(v, k):
    v0 = ctypes.c_uint32(v[0]).value
    v1 = ctypes.c_uint32(v[1]).value
    sum = ctypes.c_uint32(0xC6EF3720).value
    delta = ctypes.c_uint32(0x9E3779B9).value
    k0 = ctypes.c_uint32(k[0]).value
    k1 = ctypes.c_uint32(k[1]).value
    k2 = ctypes.c_uint32(k[2]).value
    k3 = ctypes.c_uint32(k[3]).value
    for i in range(32):
        v1 = ctypes.c_uint32(v1 - (((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3))).value
        v0 = ctypes.c_uint32(v0 - (((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1))).value
        sum = ctypes.c_uint32(sum - delta).value
    v[0], v[1] = v0, v1
    print("\n",hex(v[0]),"|",hex(v[1]))



if __name__ == "__main__":
    arr = generate_groups(["ИВБО","ИКБО","ИМБО","ИНБО"],[8,33,2,13],21,[[0],[23,29],[0],[0]])
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])

    my_print('Hello', 'world', sep=', ', end='!', flush=True)
    
    key = [0,4,5,1]
    arrMy = [0xE3238557,0x6204A1F8,0x6537611,0x174E5747,0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637]
    strMy = []
    for i in range(0,len(arrMy),2):
        strMy.append(ctypes.c_uint32(arrMy[i]).value)
        strMy.append(ctypes.c_uint32(arrMy[i+1]).value)
        decrypt(strMy[i:i+2],key)