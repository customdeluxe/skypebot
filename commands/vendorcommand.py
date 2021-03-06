# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class VendorCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "vendor" ]
        self.templates = [  Template("overlooked $name's email"),
                            Template("goes to voicemail"),
                            Template("tells $name to read the bloody small print"),
                            Template("underestimated the scope of it all"),
                            Template("is launching another !client's website"),
                            Template("can fit $name in next Tuesday, maybe."),
                            Template("never said he could actually implement it"),
                            Template("also has subcontracters."),
                            Template("is dragging out the process."),
                            Template("hasn't looked at the wireframes."),
                            Template("missed the hard deadline."),
                            Template("bollocksed it up."),
                            Template("wasn't listening."),
                            Template("gets precious about his code."),
                            Template("thinks it's his project."),
                            Template("mutters something about being too old for this shit."),
                            Template("is late for a Skype meeting."),
                            Template("reaches for the change control form."),
                            Template("looks confused, says 'I'm not that technical'."),
                            Template("is nagging $name about 30 day invoice terms."),
                            Template("buggered off on holiday without telling anyone."),
                            Template("hasn't checked Pivotal Tracker for weeks."),
                            Template("has other jobs, you know."),
                            Template("isn't paid enough to listen to your shit."),
                            Template("has fucked up the supply chain"),
                            Template("can fit $name in next Tuesday, maybe."),
                            Template("mutters something about scope creep."),
                            Template("gets the receptionist to answer the phone."),
                            Template("is still waiting for the bloody copy"),
                            Template("has kind of gone bankrupt"),
                            Template("has a bit of a cash flow problem"),
                            Template("wonders why $name is getting his knickers in a twist about the invoice")
                            ]



    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out            