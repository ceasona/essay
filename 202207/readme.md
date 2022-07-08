git中保证文件完整性的SHA-1值（commit ID）

SHA-1是一种加密哈希函数（cryptographic hash function），另外两种SHA（secure hash algorithm）算法是SHA-0和SHA-2。SHA-1将文件中的内容通过其hash算法生成一个160bit的报文摘要，即40个十六进制数字（每个十六进制数字占4位）

ethereum 私钥 长度64 sha-256, 公钥长度128，账号40，tx_hash 64
私钥在本质上是一个随机数


|         | MD5  | SHA1 | SHA-256 | SHA-512 |
| ------- | ---- | ---- | ------- | ------- |
| hex长度 | 32   | 40   | 64      | 128     |
|         |      |      |         |         |
|         |      |      |         |         |



EIP-55 格式的账户地址

该提议按照一定逻辑，将地址中的部分字母大写，与剩余的小写字母来形成校验和，让地址拥有自校验的能力



### 签名算法 secp256k1

secp256k1 是[高效密码组标准(SECG)](https://www.secg.org/) 协会开发的一套高效的椭圆曲线签名算法标准。 在比特币流行之前，secp256k1并未真正使用过。secp256k1 命名由几部分组成：sec来自SECG标准，p表示曲线坐标是素数域，256表示素数是256位长，k 表示它是 Koblitz 曲线的变体，1表示它是第一个标准中该类型的曲线。

## 参考资料：

- [区块链钱包 -公私钥生成原理及私钥管理](http://shniu.github.io/2018/08/15/blockchain/wallet-intro1/)
- [椭圆曲线乘法ECDSA](https://blog.csdn.net/w1375834506/article/details/89076195)
- [简述椭圆曲线算法](https://silence-linhl.github.io/blog/2020/04/01/ECC/)
- [RSA算法原理](https://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)
- [签名与校验](https://learnblockchain.cn/books/geth/part3/sign-and-valid.html)
- [以太坊签名验签原理揭秘](https://mirror.xyz/0x9B5b7b8290c23dD619ceaC1ebcCBad3661786f3a/jU9qUqkhF5PAG_TXIB0Mb481-cGaaaaTAvAF8FaHt40)