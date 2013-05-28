# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class HangoverCommand( BaseCommand ):

    def __init__(self):
      BaseCommand.__init__( self )
      self.command_mappings = [ "hangover", "hungover", "benefit" ]
      self.templates = [ Template("is still wearing yesterday's clothes."),
                           Template("doesn't smell so good."),
                           Template("has bags on the bags under his eyes."),
                           Template("gazes off into space."),
                           Template("forgets what he was saying."),
                           Template("sneaks off for a nap."),
                           Template("glazes over."),
                           Template("has been sitting in someone else's seat for ten minutes without realising it."),
                           Template("burped and tasted a forgotten late-night kebap."),
                           Template("is wearing his boxers back to front."),
                           Template("blames !satan."),
                           Template("weeps emotionally over nothing in particular."),
                           Template("asks everyone if they could just... shh a bit."),
                           Template("is running on !coffee & painkillers."),
                           Template("bangs on about Irn Bru."),
                           Template("!bacon !bacon !bacon"),
                           Template("would rather not talk about it."),
                           Template("wants to go home."),
                           Template("is sweating booze."),
                           Template("can barely speak."),
                           Template("is still drunk."),
                           Template("has his head in his hands.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
