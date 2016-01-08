This is just a small test / demo for [BIP 122: URI scheme for Blockchain references / exploration](https://github.com/bitcoin/bips/blob/master/bip-0122.mediawiki).

[YouTube - Demo Blockchain: URI handler](https://www.youtube.com/watch?v=87floGLZU2I)

It contains an HTML test page with some blockchain references and a sample Python handler **bc-handler.pyw** that act as a block explorer proxy of sort. The **bc-handler.conf** is a JSON file with templates for a number of block explorers (other can easily be added). Note on the final "open" entry that more than one explorer can be opened at the same time.

**register-handler.reg** is a Windows registry fragment to easily associate the URI with the Python script. Note that it will probably need to be tweaked to adjust the paths. On other OS, use the appropriate tools / procedures.
