# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class BullshitCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )

        self.command_mappings = [ "bullshit" ]

        self.array1 = ["aggregates", 
                       "beta-tests", 
                       "integrates", 
                       "captures", 
                       "creates", 
                       "designs", 
                       "disintermediates",
                       "enables",
                       "integrates",
                       "posts",
                       "remixes",
                       "reinvents",
                       "shares",
                       "syndicates",
                       "tags",
                       "incentivizes",
                       "engages",
                       "reinvents",
                       "harnesses",
                       "integrates",
                       "aggregates",
                       "architects",
                       "benchmarks",
                       "brands",
                       "cultivates",
                       "delivers",
                       "deploys",
                       "disintermediates",
                       "drives",
                       "e-enables",
                       "embraces",
                       "empowers",
                       "enables",
                       "engages",
                       "engineers",
                       "enhances",
                       "envisioneers",
                       "evolves",
                       "expedites",
                       "exploits",
                       "extends",
                       "facilitates",
                       "generates",
                       "grows",
                       "harnesses",
                       "implements",
                       "incentivizes",
                       "incubates",
                       "innovates",
                       "integrates",
                       "iterates",
                       "leverages",
                       "matrixes",
                       "maximizes",
                       "meshs",
                       "monetizes",
                       "morphs",
                       "optimizes",
                       "orchestrates",
                       "productizes",
                       "recontextualizes",
                       "redefines",
                       "reintermediates",
                       "reinvents",
                       "repurposes",
                       "revolutionizes",
                       "scales",
                       "seizes",
                       "strategizes",
                       "streamlines",
                       "syndicates",
                       "synergizes",
                       "synthesizes",
                       "targets",
                       "transforms",
                       "transitions",
                       "unleashs",
                       "utilizes",
                       "visualizes",
                       "whiteboards"]
        
        self.array2 =["AJAX-enabled",
                      "A-list",
                      "authentic",
                      "citizen-media",
                      "Cluetrain",
                      "data-driven",
                      "dynamic",
                      "embedded",
                      "long-tail",
                      "peer-to-peer",
                      "podcasting",
                      "rss-capable",
                      "semantic",
                      "social",
                      "standards-compliant",
                      "user-centred",
                      "user-contributed",
                      "viral",
                      "blogging",
                      "rich-client",
                      "24/365",
                      "24/7",
                      "B2B",
                      "B2C",
                      "back-end",
                      "best-of-breed",
                      "bleeding-edge",
                      "bricks-and-clicks",
                      "clicks-and-mortar",
                      "collaborative",
                      "compelling",
                      "cross-platform",
                      "cross-media",
                      "customized",
                      "cutting-edge",
                      "distributed",
                      "dot-com",
                      "dynamic",
                      "e-business",
                      "efficient",
                      "end-to-end",
                      "enterprise",
                      "extensible",
                      "frictionless",
                      "front-end",
                      "global",
                      "granular",
                      "holistic",
                      "impactful",
                      "innovative",
                      "integrated",
                      "interactive",
                      "intuitive",
                      "killer",
                      "leading-edge",
                      "magnetic",
                      "mission-critical",
                      "next-generation",
                      "one-to-one",
                      "open-source",
                      "out-of-the-box",
                      "plug-and-play",
                      "proactive",
                      "real-time",
                      "revolutionary",
                      "rich",
                      "robust",
                      "scalable",
                      "seamless",
                      "sexy",
                      "sticky",
                      "strategic",
                      "synergistic",
                      "transparent",
                      "turn-key",
                      "ubiquitous",
                      "user-centric",
                      "value-added",
                      "vertical",
                      "viral",
                      "virtual",
                      "visionary",
                      "web-enabled",
                      "wireless",
                      "world-class"]

        self.array3 = ["APIs",
                       "blogospheres",
                       "communities",
                       "ecologies",
                       "feeds",
                       "folksonomies",
                       "life-hacks",
                       "mashups",
                       "network effects",
                       "networking",
                       "platforms",
                       "podcasts",
                       "value",
                       "web services",
                       "weblogs",
                       "widgets",
                       "wikis",
                       "synergies",
                       "ad delivery",
                       "tagclouds",
                       "action-items",
                       "applications",
                       "architectures",
                       "bandwidth",
                       "channels",
                       "communities",
                       "content",
                       "convergence",
                       "deliverables",
                       "e-business",
                       "e-commerce",
                       "e-markets",
                       "e-services",
                       "e-tailers",
                       "experiences",
                       "eyeballs",
                       "functionalities",
                       "infomediaries",
                       "infrastructures",
                       "initiatives",
                       "interfaces",
                       "markets",
                       "methodologies",
                       "metrics",
                       "mindshare",
                       "models",
                       "networks",
                       "niches",
                       "paradigms",
                       "partnerships",
                       "platforms",
                       "portals",
                       "relationships",
                       "ROI",
                       "synergies",
                       "web-readiness",
                       "schemas",
                       "solutions",
                       "supply-chains",
                       "systems",
                       "technologies",
                       "users",
                       "vortals",
                       "web services"]
        
    def generate( self, name ):
        a = random.choice( self.array1 )
        b = random.choice( self.array2 )
        c = random.choice( self.array3 )

        message_out = ( a+' '+b+' '+c )
        return "/me %s" % message_out