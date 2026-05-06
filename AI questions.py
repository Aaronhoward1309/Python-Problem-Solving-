nums=[49,45,34,50,51,52,54,56,60,70,76,73,75]
for i in nums:
    if i>50 and i %2==0:
        print(i)

for i in range(100,-1,-1):
    print(i)
    if i==0:
        print("end of sequence")

        
nums1=[1, 2, 2, 3, 4, 4, 4, 5]
print(set(nums1))

person_a = {"coding", "hiking", "reading"}

person_b = {"cooking", "hiking", "gaming"}

print(set(person_a)&set(person_b))
