#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Group" data-toc-modified-id="Group-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Group</a></span><ul class="toc-item"><li><span><a href="#Definition" data-toc-modified-id="Definition-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Definition</a></span></li><li><span><a href="#Addition-Modular" data-toc-modified-id="Addition-Modular-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Addition Modular</a></span></li><li><span><a href="#Multiplication-Module" data-toc-modified-id="Multiplication-Module-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Multiplication Module</a></span></li><li><span><a href="#Unit-Group" data-toc-modified-id="Unit-Group-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Unit Group</a></span><ul class="toc-item"><li><span><a href="#Greatest-common-factor-(GCD)" data-toc-modified-id="Greatest-common-factor-(GCD)-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Greatest common factor (GCD)</a></span></li><li><span><a href="#Creating--Function-for-compute-GCD-" data-toc-modified-id="Creating--Function-for-compute-GCD--1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Creating  Function for compute GCD </a></span></li><li><span><a href="#-Definition-(Unit-Group)" data-toc-modified-id="-Definition-(Unit-Group)-1.4.3"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span> Definition (Unit Group)</a></span></li></ul></li></ul></li></ul></div>

# <html>
# <body>
# 
# <article>
#   <header>
#     <h1>Abstract Algebra with Python<span class="tocSkip"></span></h1>
#     <h3>Written by Rajesh Bandari Yadav<span class="tocSkip"></h3>
#     
# </article>
# 
# </body>
# </html>
# 

# <h1>Group</h1>

# <h2>Definition</h2> <br>
# If $G$ is a nonempty set and $a$ is a binary operation on $G$, then $(G, \square)$ is called a group if the following conditions are satisfied.<br>
# ।. For all $a, b \in G, a \square b \in G$ (Closure of under $\square$ ) <br>
# 2. For all $a, b, c \in G,(a \square b) \square c=a \square(b \square c)$.
# (Associative)<br>
# 3. There exists $e \in G$ with $e\square a=a\square e$ for all $a \in G$. (Existence of an Identity) <br>
# 4. For each $a \in G$, there is an elements $a^{\prime} \in G$ such that $a^{\prime} \square a=a\square a^{\prime} a=e$.

# <h2>Addition Modular</h2>

# Example: $\mathbb{Z}_{4}=\{0,1,2,3\}$ is a group w.r.to $+_{4}$ <br>
# 
# <b>Indetity</b>: 0 <br> 
# 
# <b>Inverse of $a=4-a(mod 4) \forall a \in \mathbb{Z}_{4}$</b><br> <br>
# 

# 

# 

# In[199]:


print("Calay's Table for (Z4,+4)")
print()
print("+4|",end='')
for j in range (4):
    print(format(j,"4d"),end='')
print()    
print("---------------------")


for i in range(4):
    print(i,"|",end='')
    for j in range(4):
        a=(i+j)%4
        print(format(a,"4d"),end='')
    print()
        
        


# <h2>Multiplication Module</h2>

# <b>Example</b>:$\mathbb{Z}_{5}-\{0\}=\{1,2,3,4\}$ is a group w.r.to $\times_{5}$
# <b>Indetity</b>: 1 <br> 
# 
# <b>Inverse</b> <br>
# inverse of $1$ is $1$ <br>
# inverse of $2$ is $3$ <br>
# inverse of $3$ is $2$ <br>
# inverse of $4$ is $4$ <br>
# 

# In[198]:


print("Calay's Table for (Z5-{0},+5)")
print()
print("x5|",end='')
for j in range (1,5):
    print(format(j,"4d"),end='')
print()    
print("---------------------")


for i in range(1,5):
    print(i,"|",end='')
    for j in range(1,5):
        a=(i*j)%5
        print(format(a,"4d"),end='')
    print()


# <h2>Unit Group</h2>

# <h3>Greatest common factor (GCD)</h3>

# Definition: The greatest common divisor of two nonzero integers a and $b, g c d(a, b)$, is the largest integer that divides both, except that $\operatorname{gcd}(0,0)=0$.<br>
# The exception is there because every number divides zero, and so we specially define $\operatorname{gcd}(0,0)=0$ to be a convenient value.

# <b>Properties of Greatest common divisor:</b> <br>
# 1.$\operatorname{gcd}(a, b)=\operatorname{gcd}(b, a)$.<br>
# 2. $\operatorname{gcd}(a, b)=\operatorname{gcd}(|a|,|b|)$.<br>
# 3.<b>Example:</b>
# $\operatorname{gcd}(-12,-14)=g c d(-12,14)=g c d(12,-14)=g c d(12,14)$ <br>
# 
# 4.If $a \neq 0$ or $b \neq 0$, then $\operatorname{gcd}(a, b)$ exists and satisfies $0<\operatorname{gcd}(a, b) \leq \min \{|a|,|b|\}$.<br>
# 5.If $\mathrm{a}>0$ then $\operatorname{gcd}(\mathrm{a}, 0)=\mathrm{a}$.<br>
# 6.gcd of $n$ numbers $a_{1}, a_{2}, a_{3}, a_{4}, \ldots \ldots \ldots . a_{n}$.<br>
# 7.$\operatorname{gcd}\left(a_{1}, a_{2}, a_{3}, a_{4}, \ldots \ldots . . a_{n}\right)=\operatorname{gcd}\left(\operatorname{gcd}\left(a_{1}, a_{2}, a_{3}, a_{4}, \ldots \ldots . a_{n-1}\right), a_{n}\right)$

# In[218]:


import math
a=math.gcd(12,14)
b=math.gcd(14,12)
c=math.gcd(-12,-14)
d=math.gcd(0,12)
e=math.gcd(0,0)
print(a)
print(b)
print(c)
print(d)
print(e)


# <h3>Creating  Function for compute GCD </h3>

# In[ ]:


def GCD(a,b):
    if a<b:
        c=a
    else:
        c=b
            
    for i in range(1,c+1):
        if(a%i==0 and b%i==0):
            gcd=i
    return gcd
            


# In[232]:


GCD(12,14)


# <h3> Definition (Unit Group)</h3>

# Let $n$ be a natural  number, consider the set $U(n)=\{x\in \mathbb{N};1\leq x\leq n,gcd(x,n)=1\}$ is a group w.r.to $\times_{n}$ is called Unit group.<br> <br>
# <b>Note:</b>Number of elements in $U(n)$ is equal to $\phi(n)$ <br>
# $$\phi(n)=n\bigg(1-\frac{1}{p_{1}}\bigg)\bigg(1-\frac{1}{p_{2}}\bigg)\dots \bigg(1-\frac{1}{p_{k}}\bigg)$$ where $p_{i}'s$ are primes and $n=p_{1}^{\alpha_{1}}p_{2}^{\alpha_{2}}\dots p_{k}^{\alpha_{k}}$
# 

# In[ ]:





# <b>Example:</b>List of number which are realtive prime to 9 that is $U(9)=\{x\in \mathbb{N};1\leq x\leq 9,gcd(x,9)=1\}$

# In[ ]:





# In[233]:


G=[]
for i in range(1,9):
    if GCD(i,9)==1:
        G.append(i)
print("List of the elements in G:",G)
print("Total number numbers which are relative prime to 9 are :",len(G))                


# In[ ]:





# $G=\{1,2,3,4,5,7,8\}$ is a forms a group w.r.to $\times_{9}$ <br>
# 
# <b> Identity :</b> 1 <br>
# <b>Inverse</b> <br>
# $(1)^{-1}=1$ <br>
# $(2)^{-1}=5$ <br>
# $(4)^{-1}=7$ <br>
# $(5)^{-1}=2$ <br>
# $(7)^{-1}=4$ <br>
# $(8)^{-1}=8$ <br>

# <b>Caylay's table for $(U(9),\times_{9})$</b>

# In[247]:


print("Calay's Table for (U(9),x9)")
print()
print("x9|",end='')
for j in G:
    print(format(j,"4d"),end='')
print()    
print("------------------------------")


for i in G:
    print(i," |",end='')
    for j in G:
        a=(i*j)%9
        print(format(a,"4d"),end='')
    print()
        


# In[ ]:





# In[322]:


def Sum(a,b):
    Sum=a+b
    return Sum  


# In[341]:


def is_associative(G):
    for a in G:
        for b in G:
            ab=Sum(a,b)
            for c in G:
                bc=Sum(b,c)
                ab_c=Sum(ab,c)
                a_bc=Sum(a,bc)
                if(ab_c!=a_bc):
                    return 0
                return 1
        


# In[344]:


G=[1,2,3,4,5]
is_associative(G) 


# In[326]:


Sum(1,2)


# In[285]:


Sum(2,3)


# In[286]:


Sum(5,7)


# In[323]:


Sum(20,34)


# In[321]:


2+3


# In[339]:


G=[20,21,22,23,24]
is_associative(G)


# In[340]:


G=[1,2,3,4,5]
is_associative(G)


# In[345]:


def is_Associative(G):
    for a in G:
        for b in G:
            ab=a+b
            for c in G:
                bc=b+c
                ab_c=ab+c
                a_bc=a+bc
                if(ab_c!=a_bc):
                    return 0
                return 1
        


# In[346]:


G=[1,2,3,4,5]
is_Associative(G)


# In[ ]:




