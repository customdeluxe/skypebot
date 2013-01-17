# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ShoutoutCommand( BaseCommand ):

     def __init__(self):
          BaseCommand.__init__( self )
          self.command_mappings = [ "shoutout", "bigup", "holdtight" ]
          self.templates = [  Template("shouts out to $name."),
                              Template("goes brap brap brap at $name."),
                              Template("big ups $name."),
                              Template("puts his hands up for $name."),
                              Template("praises $name."),
                              Template("scratches the shit out of $name."),
                              Template("turns the LFO for $name."),
                              Template("drops a piano break on $name."),
                              Template("spins the record back for $name."),
                              Template("drops the beat on $name.")
                            ]
          self.gifting_enabled = False

     def generate( self, name ):
          template = random.choice( self.templates )
          message_out = template.substitute( name=name )
          if name.endswith( (".","!","?") ) and message_out.endswith("."):
               message_out = message_out[:-1] # lose the fullstop if name is already punctuated
          return "/me %s" % message_out

     def execute( self, message ):
          body = message.Body
          bl = body.lower()
          for commandstring in self.command_mappings:
               if commandstring in bl:
                    print commandstring
                    command_index = bl.find( commandstring )
                    print command_index
                    if command_index > -1:
                         remainder = body[ command_index + len(commandstring): ]
                         remainder = remainder.lstrip()
                         print remainder
                         to_string = "to"
                         to_index = remainder.lower().find( to_string )
                         name = None
                         if to_index > -1:
                              name = remainder[ to_index + len(to_string): ]
                              name = name.lstrip()
                              return self.generate( name )
          name = message.FromDisplayName
          return self.generate( name )               
 
