#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:51:03 2019

@author: anirban-mac
"""

"""
535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such 
as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no \
restriction on how your encode/decode algorithm should work. You just need to 
ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded 
to the original URL.
"""

import hashlib
class Codec:
    
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        encodedUrl = hashlib.sha256(longUrl.encode('utf-8')).hexdigest()
        self.urls[encodedUrl] = longUrl
        print(self.urls)
        return encodedUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
encodedUrl = codec.encode(url)
print(encodedUrl)
codec.decode(encodedUrl)