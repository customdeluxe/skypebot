# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class AdmanCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "artist" ]

          self.templates = [  Template("decides that $name is not an artist."),
                    Template("decides that $name is an artist."),
                    Template("decides that $name is 50% artist."),
                    Template("decides that $name is 66.6% artist.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
