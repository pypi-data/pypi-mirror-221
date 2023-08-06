====================
**OTG Cryptography**
====================
The expansion of OTG cryptography is One Time Gamble. It is a hybrid and lightweight cryptographic system. that transforms a plaintext into a ciphertext so that secret communication is to be ensured.

--------------------
**Description**
--------------------
In the OTG system, the original password is hidden under several fake passwords in a vault. Also, these passwords are hashed by bcrypt hash function which is a one-way encryption and cannot be reversed. Moreover, the secret message will be deleted by itself if a user gives the wrong password only at once. As a result, it will be so much more difficult for a hacker to guess, retrieve and use the password correctly among fake passwords. Furthermore, the key is 128 bits long. So, a hacker needs to go for 2128 = 3.402e+38 possible ways in terms of finding the correct key to decrypt the ciphertext. It is by far impossible for a regular user device to solve the math. It will need a supercomputer to do the computation. However, a low computational powered device (e.g. IOT device) can easily handle it because of its symmetric and stream cipher architecture. Thus, it makes the algorithm lightweight. Also, OTG is a software and hardware-independent cryptography. In conclusion, this new innovation can make a fruitful impact on the current security epidemic.

----------------------------
**Program Utilization**
----------------------------
* A user inputed password.
* A user inputed secret message.
* The secret messages is stored in a vault with ChaCha20poly1305 method.
* A dictionary is containing manipulated (fake) passwords in addition to the real password.
* A dictionary containing seeds (Seed generator). Seeds are simply pointers that point to the secret message.
* The encryption algorithm: **cipher = password XOR key**.
* The decrpytion algorithm: **key = password XOR cipher**.
* A try/except block to search for actual password that do exist in the password dictionary.
* The message will be deleted if a user give wrong password.

--------------------------------
**Ideal Applications To Use**
--------------------------------
* Government Secret Message
* Sensitive Business Communication
* Low Computational Powered Device

--------------------------------
**Caution**
--------------------------------
* OTG is a very typo sensitive system.
* It should be used only for very sensitive work.
* This cryptography ensures OTC (One Time Chance) method.
* Message will be deleted if a user gives wrong password only at once.

--------------------------------
**Do You Want To Know Me?**
--------------------------------
* **Call**: +8801818832925
* **Email**: tahsin.ahmed@g.bracu.ac.bd
* **Facebook**: https://www.facebook.com/ahmedinsider
