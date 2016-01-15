#! python3

DEBUG = True

import tkinter
import tkinter.messagebox as tkMessageBox
import os
import sys
import webbrowser
import json
from urllib.parse import urlparse

def isblockheight(hash):
    # just a super simple euristic
    if len(hash) < 10:
        return True
    else:
        return False

def blockhash2nick(hash):
    nick = ""
    hashlist = {"":"BTC-main",
                "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f":"BTC-main",
                "000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943":"BTC-test",
                "0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206":"BTC-regtest"
                }
    if hash in hashlist:
        nick = hashlist[hash]
    return nick

root = tkinter.Tk()
root.withdraw()

query = sys.argv[1]

confname = os.path.join(os.path.dirname(sys.argv[0]), "bc-handler.conf")
with open(confname) as fconf:
    conf = json.load(fconf)
    fconf.close()

bc_chain = bc_type = bc_hash = ""

pr = urlparse(query)
if pr.scheme == "blockchain":
    bc_chain = pr.netloc
    bc_type, bc_hash = pr.path.split("/")[-2:]
    bc_type = bc_type.lower()
        
if DEBUG:
    tkMessageBox.showinfo("Python", "Blockchain URI handler\n\n" +
                      "chain: %s\n" % (blockhash2nick(bc_chain)) +
                      "type: %s\n" % (bc_type) +
                      "hash: %s" % (bc_hash) +
                      "\n\n\nRaw: [%s]" % (query))

if bc_type == "block":
    if isblockheight(bc_hash):
        bc_type = "height"

for explorerid in conf["open"]:
    url = ""
    for spec in conf["block-explorers"]:
        if spec["name"] == explorerid:
            if bc_type in spec:
                    url = spec[bc_type] % (bc_hash)
    if url:
        webbrowser.open(url)
