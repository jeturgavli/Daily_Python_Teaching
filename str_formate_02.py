# st.format() = optional method that gives users
#               more control when displaying output

name = "Jetur"
print("Hello, my name is {}".format(name))

# -------Space ----------
fd1 = "Akib"
print("Hello, my name is {:10}. Niceto meet you".format(fd1)) 

# ------- you doing also this type of format ----------
fd2 ="Mohit"
print("Hello, my name is {0:10}. Niceto meet you".format(fd2)) 

# ----- Alig Left--------
bigbro = "Vivek"
print("Hello, my name is {:<10}. Niceto meet you".format(bigbro)) 

# ----- Alig Right--------
litlbro1 = "Martin"
print("Hello, my name is {:>10}. Niceto meet you".format(litlbro1))

# ----- Alig Center--------
litlbro2 = "Keron"
print("Hello, my name is {:^10}. Niceto meet you".format(litlbro2))
