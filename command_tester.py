from commands import pondercommand
from commands import shoutoutcommand
from commands import lspcommand
from commands import commandscratch
from commands import hankcommand
from commands import regretscommand
from commands import ballcommand
from commands import ennuicommand


# bullshit
test_command = ennuicommand.EnnuiCommand()
print test_command.generate( "shardcore" )

# ponder
test_command = pondercommand.PonderCommand()
print test_command.generate( "prehensile" )

# shoutout
test_command = shoutoutcommand.ShoutoutCommand()
test_message = { "Body": "#shoutout to the berlin massive" }
print test_command.execute( test_message )
