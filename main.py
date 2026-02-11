from facade import *
from strategy import *
from command import *

santa = SantaClausFacade()
order = GiftOrderCommand(santa)
order.execute(
 gift_type="toy",
 strategy=ReindeerDelivery()
)
# Sortie console :
# Elf Stark notified: Toy wrapped with ribbon with message 'Ho Ho Ho!'
# Elf Rob notified: Toy wrapped with ribbon with message 'Ho Ho Ho!'
# Toy wrapped with ribbon with message 'Ho Ho Ho!'
# Delivered by reindeer
