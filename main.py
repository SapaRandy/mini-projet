from facade import *
from strategy import *
from command import *

santa = SantaClausFacade()
order = GiftOrderCommand(santa)
order.execute(
 gift_type="toy",
 strategy=ReindeerDelivery()
)

order.execute(
 gift_type="book",
 strategy=DroneDelivery()
)
# Sortie console :

#Elf Stark notified: Toy wrapped with ribbon with message 'Ho Ho Ho!'
#Toy wrapped with ribbon with message 'Ho Ho Ho!'
#Delivered by reindeer
#--------------------------------------------------
#Elf Stark notified: Book wrapped with ribbon with message 'Ho Ho Ho!'
#Book wrapped with ribbon with message 'Ho Ho Ho!'
#Delivered by drone

# It always select the same elf because elf's state doesn't change beetween two calls
# I can fix that with a variable but isn't a solution for a true development
# I do add a queue but for the moment I didn't succeed