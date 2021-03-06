# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class QuizCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "quiz" ]

        self.questions = [
            "what do you like most about your profession?",
            "what do you like least?",
            "how long have you been doing this?",
            "should your parents have been more or less strict?",
            "how was your childhood?",
            "are you happy now?",
            "if you could go back in time, what would you do differently?",
            "if you hadn't been born in this century, when and where would you like to have lived?",
            "who are your heroes?",
            "who do you have no respect for?",
            "what do you do in your spare time?",
            "are you politically active?",
            "do you do any volunteer work?",
            "how has America changed in the last ten years?",
            "how have you changed?",
            "what's the side of you that the public never sees?",
            "do you wish you had more privacy?",
            "do you think the public and critics expect too much from you?",
            "how hard do you push yourself?",
            "when are you completely satisfied with your work?",
            "why have you succeeded in a field where so many others have failed?",
            "what's the magic formula for success?",
            "what do you think about reincarnation?",
            "how about astrology?",
            "what about life on other planets?",
            "what do you do to relax?",
            "is there a battle of the sexes?",
            "who's winning?",
            "are we returning to a more romantic time?",
            "how do you define macho?",
            "do you believe in the traditional roles for men and women?",
            "if you were a man how different do you think your career would have gone?",
            "what's the most unbelievable rumor ever printed about you?",
            "what was the most important day of your life?",
            "do you worry about whether people like you for the real you, or because you're a celebrity?",
            "do you make friends easily?",
            "which do you enjoy most: a night on the town or staying in with that someone special?",
            "what's your favorite pig-out food?",
            "what do you do for exercise?",
            "what's your favorite sports team?",
            "do you think americans put too much emphasis on competition?",
            "if you were president, what's the first thing you'd do?",
            "what's the first song you ever remember hearing?",
            "what are you listening to lately?",
            "what's your favorite album by another artist?",
            "what song of yours are you most proud of?",
            "why?",
            "are there any songs you've done that you wish you hadn't?",
            "is this your first album?",
            "had any of you recorded with other groups before forming _",
            "how long is this tour?",
            "is it possible to be out on the road and not eat any junk food?",
            "people have the image that it's non-stop partying out there. is it true?",
            "are you married or involved with anyone?",
            "is it hard to maintain a relationship when you're out on the road?",
            "when do you go back in the studio?",
            "what does your contract rider call for in terms of backstage amenities?",
            "what would you be doing if you weren't a musician?",
            "how many guitars do you own?",
            "how many songs in your home collection?",
            "how do you feel about censorship?",
            "do you censor yourself? have you ever written anything and then decided it was too harsh?",
            "what's next for you?",
            "how old were you when you started writing?",
            "when did you know that this would be your profession?",
            "who's your favorite author?",
            "why?",
            "are there any writers whose success mystifies you?",
            "do you read more fiction, or non-fiction?",
            "what are you reading lately?",
            "what are a couple of your all-time favorite books?",
            "can an author write for the pulitzer and the public at the same time?",
            "publishing has become big business. has that hurt?",
            "what inspired your latest book?",
            "do you think television is responsible for illiteracy?",
            "when you go to see a movie, do you try to read the book first?",
            "many schools have banned certain books for various reasons. where do you think the line should be drawn?",
            "how do you overcome writer's block?",
            "have you ever written about your own bad habits?",
            "do you ever feel forced to write?",
            "how would you feel if a publisher wanted to condense your work?",
            "who do you enjoy working with the most?",
            "who is the hardest to work with?",
            "how much do you draw on your own experience when you act?",
            "what do you do if you find yourself acting in your real-life relationships?",
            "if you could star in a re-make of a classic film, who would you want to play?",
            "how do you feel about nude scenes?",
            "when doing a love scene, do you imagine you're with somebody else?",
            "do you think there's too much violence in tv and movies?",
            "what work are you most proud of?",
            "is there anything you'd done that you'd like to burn all the copies of?",
            "are there any actors who turned out to be nothing like you thought they'd be?",
            "if oscars were for sale, how much would you pay for one?",
            "when was the last time you told a lie?",
            "how do you feel about the colorization of old black and white films?",
            "when a scene calls for you to display hatred, what do you think about?",
            "what was your most challenging role?",
            "how much of hollywood is superficial?",
            "are you often compared to other actors?",
            "are the movies better than ever, or are they worse?",
            "why do producers feel they have to spend $100 million to make a film?",
            "what's the meaning of life?",
            "other than this interview, what's the stupidest thing you've ever agreed to do?",
            "is there life after marriage?",
            "do you believe there is intelligent life on earth?",
            "when the aliens land on earth, why will you be the first person they talk to?",
            "do people think you're macho?",
            "if you could be any animal...what animal would you be?",
            "How do you feel about botstep?",
            "how would you explain the infomorph aesthetic?",
            "what is a dong?",
            "surely, this would be better with a dubstep beat?",
            "what do you think of Marcus?",
            "what do you think of Satan's hat?",
            "tell me about time and cock",
            "where do mice come from?",
            "can I borrow your braces?",
            "how many planners does it take to make a robot?",
            "what is an infomorph?",
            "why?",
            "what are you trying to say?",
            "will it always be this way?",
            "what if I trip?",
            "can we?",
            "where is the drop?",
            "where is the drop on this botstep?",
            "seriously, where is the fucking drop?!",
            "what is this shit?",
            "do you think we've stolen a bit of your soul?",
            "why have you sat three on a sofa?",
            "are you trying to control the conversation?",
            "I mean, Satan, what kind of name is that anyway?",
            "seriously? seriously?",
            "where the hell is Pambot?",
            "where's the fish?",
            "can you feel it?",
            "mate, what are you on about?",
            "does talking about this bother you?" ]

        self.templates = [  Template("asks $name: $question"),
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        question = random.choice( self.questions )
        message_out = template.substitute( name=name, question=question )
        return "/me %s" % message_out