This is just a small test / demo for [BIP 122: URI scheme for Blockchain references / exploration](https://github.com/bitcoin/bips/blob/master/bip-0122.mediawiki).

It contains an HTML test page with some blockchain references and a sample Python handler **bc-handler.pyw** that acts as a block explorer proxy of sort. The **bc-handler.conf** is a JSON file with templates for a number of block explorers (other can easily be added). Note on the final "open" entry that more than one explorer can be opened at the same time.

**register-handler.reg** is a Windows registry fragment to easily associate the URI with the Python script. Note that it will probably need to be tweaked to adjust the paths. On other OS, use the appropriate tools / procedures.

----

[YouTube - Demo Blockchain: URI (BIP 122) handler](https://www.youtube.com/watch?v=7wwVnQn7rj8)

[YouTube - Demo Eternity Wall & Blockchain: URI (BIP 122) handler ](https://www.youtube.com/watch?v=lMbxnP_xj04)

This is an example of a blockchain: link that point to a transaction (the one shown in the video above): [blockchain:/tx/d11561307901a131dd21feda66184e16717c3fb9faf588e76ea102f7a9ee16a9](blockchain:/tx/d11561307901a131dd21feda66184e16717c3fb9faf588e76ea102f7a9ee16a9)
