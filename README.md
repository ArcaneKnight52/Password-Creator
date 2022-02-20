# Password-Creator
Python program to create a password generator


Password Generators are a tool to generate passwords based on security guidelines that user sets to create strong and unpredictable password. A strong password must have at least 15 characters consisting of uppercase ascii letters, lowercase ascii letters, numbers, symbols (“! @ # $ % ^ & * ( ) ”) .

The following source code is written in python. Modules used are tkinter, random, pyperclip. Tkinter is used for simple GUI implementation, random is used for creating random choices and pyperclip to copy information onto clipboard. 
The basic logic is to:

	1.Create an application window
  
    1.1. initialize root as Tk()
    
    1.2. create a window using geometry method of tkinter
    
    1.3. get variables for length and storing password 
    
    1.4. generate password using python
    
    1.5. create buttons and set commands as per pre-defined methods
    
    1.6.  run infinite mainloop() to run the code through front end (GUI using tkinter)
    
	2.Create a password using python (using random module).
  
	3.Copy and display it in GUI window according to data inputted from user.
  

The strength of any password is determined by the random algorithms used to generate it and the length of the password. Pseudo-random algorithms are methods such as atmospheric randomness or FIPS181.
A password created using a pseudo random algorithm can be retraced and easily reproduced. The random module in python is also a pseudo random as it works on PRNG (pseudorandom number generator). To create a truly random number SystemRandom method is used under random module.
The information entropy is calculated for assessing the strength of a random password. It is given by H as 

H = 〖L*log〗_2⁡N=L*(log⁡N/log⁡2 )

Where L is length of the password
N=number of possible characters

Entropy(H) is measured in bits. A strong password capable of securing financial information has an entropy in the range of 60-127 bits.
Using the current source code for a standard password of length of 15 characters we can get an entropy of 92.84736838320026 bits which is very secure.

If we only use random from random module it will cycle same values, can be reproduced and the randomness is not truly random.
Whereas using SystemRandom() method from random module as random.SystemRandom() generates truly random generations. Thus SystemRandom is used under random.
