# auto ssh login
# windows https://blog.csdn.net/qq_45624685/article/details/122631083
type C:\Users\95028\.ssh\id_rsa.pub | ssh root@xx.xx.xx.xx "cat >> .ssh/authorized_keys"