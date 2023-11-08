"""
You can use this script on any *_Taml.* files. 
It will look through the file and remove any superscripts that
may have been introduced due to transliteration from languages 
with more sounds than Tamil. 

Ex. Tamil has only one letter to represent the following 4 sounds
common in the other 3 Dravidian languages: 
    tel kan  mal tam 
k    క   ಕ   ക   க 
kh   ఖ  ಖ   ഖ   க₂ 
g    గ   ಗ   ഗ   க₃
gh   ఘ  ಘ  ഘ   க₄

The subscripts/superscripts are introduced to differentiate the four sounds. 
These are 5 such sequences. Unicode uses superscripts instead of subscript 

""" 