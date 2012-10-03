# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class RegretsCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "regrets","myway" ] 


        self.wisdom = [ 
            "And now, the end is here, And so I face the final curtain", 
            "My friend, I\'ll say it clear, I\'ll state my case, of which I\'m certain", 
            "I\'ve lived a life that\'s full, I traveled each and ev\'ry highway", 
            "And more, much more than this, I did it my way", 
            "Regrets, I\'ve had a few, But then again, too few to mention", 
            "I did what I had to do and saw it through without exception", 
            "I planned each charted course, each careful step along the byway", 
            "And more, much more than this, I did it my way", 
            "Yes, there were times, I\'m sure you knew, When I bit off more than I could chew", 
            "Yes, there were times, I\'m sure you knew, When there was fuck, fuck all else to do", 
            "But through it all, when there was doubt, I ate it up and spit it out", 
            "I faced it all and I stood tall and did it my way", 
            "I've loved, I've laughed and cried", 
            "I've had my fill, my share of losing", 
            "And now, as tears subside, I find it all so amusing", 
            "To think I did all that, And may I say, not in a shy way", 
            "Oh, no, oh, no, not me, I did it my way", 
            "For what is a man, what has he got? If not himself, then he has naught" ,
            "To say the things he truly feels and not the words of one who kneels", 
            "The record shows I took the blows and did it my way!" 
]
        

        self.templates = [  Template("advises $name: "),
                            Template("croons: "),
                            Template("emotes: ")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        quote = random.choice( self.wisdom );
        message_out = template.substitute(name=name)+"\""+quote+"\"";
        return "/me %s" % message_out
