import struct
from ctypes import *
import hashlib
import binascii
import sys

def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

m = hashlib.md5()
s = hashlib.sha1()
s512 = hashlib.sha512()
s224 = hashlib.sha224()
s3224 = hashlib.sha3_224()
bl2s = hashlib.blake2s()
bl2b = hashlib.blake2b()
s3384 = hashlib.sha3_384()
s3512 = hashlib.sha3_512()
s384 = hashlib.sha384()
ske128 = hashlib.shake_128()
ske256 = hashlib.shake_256()

s3256 = hashlib.sha3_256()
s256 = hashlib.sha256()

if(len(sys.argv) != 2):
	exit(0)


fobj = open(sys.argv[1], 'rb')
raw_bytes = fobj.read()




bs = ''.join(map(lambda x: '{:08b}'.format(x), raw_bytes))

fobj.close()

bitNumb = 0
nybblesz = int(len(bs)/4)

hs = ''
for i in range(0,int(nybblesz)): 
	nybble = bs[bitNumb] + bs[bitNumb+1] +bs[bitNumb+2] +bs[bitNumb+3]
	bitNumb = bitNumb + 4
	hs = hs + hex(int(nybble,2))[2:]

hs_8 = [hs[i:i+2] for i in range(0,len(hs),2)]
hs_16 = [hs[i:i+4] for i in range(0,len(hs),4)]
hs_32 = [hs[i:i+8] for i in range(0, len(hs), 8)]

## SPLIT UP INTO 128 bit chuncks for MD5 Hashing
hs_128 = [hs[i:i+32] for i in range(0, len(hs),32)]

## SPLIT UP INTO 160 bit chucks for SHA1 Hashing
hs_160 = [hs[i:i+40] for i in range(0, len(hs),40)]

## SPLIT UP INTO 512 bit chucks for SHA512 Hashing
hs_512 = [hs[i:i+128] for i in range(0, len(hs),128)]

## SPLIT UP INTO 224 bit chuncks for SHA224 and SHA3_224 Hashing
hs_224 = [hs[i:i+56] for i in range(0, len(hs),56)]

hs_256 = [hs[i:i+64] for i in range(0, len(hs),64)]

hs_384 = [hs[i:i+96] for i in range(0, len(hs),96)]


hashedString = ''
for h in hs_128:
	uhB = bytes.fromhex(h)
	m.update(uhB)
	hashedString = hashedString+m.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('MD5 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/md5-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()




hashedString = ''
for h in hs_160:
	uhB = bytes.fromhex(h)
	s.update(uhB)
	hashedString = hashedString+s.hexdigest()

print('SHA 1 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

out1 = open('../src/hshs/s1-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()






hashedString = ''
for h in hs_512:
	uhB = bytes.fromhex(h)
	s512.update(uhB)
	hashedString = hashedString+s512.hexdigest()

print('SHA-2 512 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

out1 = open('../src/hshs/s2512-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()






hashedString = ''
for h in hs_224:
	uhB = bytes.fromhex(h)
	s224.update(uhB)
	hashedString = hashedString+s224.hexdigest()

print('SHA-2 224 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

out1 = open('../src/hshs/s2224-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()



hashedString = ''
for h in hs_224:
	uhB = bytes.fromhex(h)
	s3224.update(uhB)
	hashedString = hashedString+s3224.hexdigest()

print('SHA-3 224 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

out1 = open('../src/hshs/s3224-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()


hashedString = ''
for h in hs_256:
	uhB = bytes.fromhex(h)
	bl2s.update(uhB)
	hashedString = hashedString+bl2s.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('BLAKE2S HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/bl2s-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_512:
	uhB = bytes.fromhex(h)
	bl2b.update(uhB)
	hashedString = hashedString+bl2b.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('BLAKE2B HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/bl2b-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_384:
	uhB = bytes.fromhex(h)
	s3384.update(uhB)
	hashedString = hashedString+s3384.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHA3-384 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/s3384-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()


hashedString = ''
for h in hs_512:
	uhB = bytes.fromhex(h)
	s3512.update(uhB)
	hashedString = hashedString+s3512.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHA3-512 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/s3512-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_384:
	uhB = bytes.fromhex(h)
	s384.update(uhB)
	hashedString = hashedString+s384.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHA2-384 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/s384-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_128:
	uhB = bytes.fromhex(h)
	ske128.update(uhB)
	hashedString = hashedString+ske128.hexdigest(128)

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHAKE128 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/ske128-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_256:
	uhB = bytes.fromhex(h)
	ske256.update(uhB)
	hashedString = hashedString+ske256.hexdigest(256)

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHAKE256 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/ske256-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_256:
	uhB = bytes.fromhex(h)
	s256.update(uhB)
	hashedString = hashedString+s256.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHA2-256 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/s256-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()

hashedString = ''
for h in hs_256:
	uhB = bytes.fromhex(h)
	s3256.update(uhB)
	hashedString = hashedString+s3256.hexdigest()

#print('\nORIGINAL STRING')
#print(hs)
#print('\n\n\n\n')

print('SHA3-256 HASH STRING for' + sys.argv[1])
#print(hashedString)
#print('\n\n\n\n')

#out1 = open('testq.bin', 'wb')
#new_bytes = bytes.fromhex(hs)
#ut1.write(new_bytes)	
#out1.close()
out1 = open('../src/hshs/s3256-'+sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1], 'wb')
out1.truncate()
new_bytes = bytes.fromhex(hashedString)
out1.write(new_bytes)	
out1.close()





Rints32=[]
Rfloats32=[]

for h in hs_32: 
	Rints32.append(int(h,16))
	Rfloats32.append(convert(h))

Rints16=[]

for h in hs_16:
	Rints16.append(int(h,16))

Rints8=[]

for h in hs_8:
	Rints8.append(int(h,16))

R32ias = 'ri32 <- c('
R32fas = 'rf32 <- c('
R16ias = 'ri16 <- c('
R8ias = 'ri8 <- c('

for integer in Rints32:
	R32ias = R32ias + str(integer) + ', '

R32ias = R32ias[:-2] + ')'

for floatv in Rfloats32:
	R32fas = R32fas + str(floatv) + ', '

R32fas = R32fas[:-2] + ')'

for integer in Rints16:
	R16ias = R16ias + str(integer) + ', '

R16ias =  R16ias[:-2] + ')'

for integer in Rints8:
	R8ias = R8ias + str(integer) + ', '

R8ias =  R8ias[:-2] + ')'

