# coding=UTF-8

from string import Template
import random

class ByeCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("waves goodbye to $name."),
							Template("throws his hands up as $name finally leaves the bar."),
							Template("hardly notices that $name leaves."),
							Template("couldn't give a flying pickle about $name leaving."),
							Template("breaks wind and blames $name."),
							Template("calls last orders at the bar."),
							Template("comes running after $name as they try to dodge the bill, again."),
							Template("tries to get $name to have one more drink.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out