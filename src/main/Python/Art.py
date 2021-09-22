
def rules():
    print("__________________________________________________________________\n"
    "__________________________________________________________________\n" 
    "                       L O V E   L E T T E R                      \n" \
    "                                                                  \n" \
    "                         -- Setup --                             \n" \
    "We shuffle the 16 cards to form a face-down draw deck. Remove     \n" \
    "the top card of the deck from the game without looking at it.     \n" \
    "Each player get one card from the deck. This is the player's      \n" \
    "hand, and is kept secret from the others.                         \n" \
    "                                                                  \n" \
    "                      -- Object of the Game --                    \n" \
    "In the wake of the arrest of Queen Marianna for high treason,     \n" \
    "none was more heartbroken than her daughter, Princess Annette.    \n" \
    "Suitors throughout the City-State of Tempest sought to ease       \n" \
    "Annette's sorrow by courting her to bring some joy into her life. \n" \
    "                                                                  \n" \
    "You are one of these suitors, trying to get your love letter      \n" \
    "to the princess. Unfortunately, she has locked herself in the     \n" \
    "palace, so you must rely on intermediaries to carry your message. \n" \
    "During the game, you hold one secret card in your hand. This is   \n" \
    "who currently carries your message of love for the princess.      \n" \
    "                                                                  \n" \
    "Make sure that the person closest to the princess holds your      \n" \
    "love letter at the end of the day, so it reaches her first!       \n" \
    "                                                                  \n" \
    "                      -- Game Play --                             \n" \
    "Love Letter is played in a series of rounds. Each round           \n" \
    "represents one day. At the end of each round, one player's        \n" \
    "letter reaches Princess Annette, and she reads it.                \n" \
    "When she reads enough letters from one suitor, she becomes        \n" \
    "enamored and grants that suitor permission to court her.          \n" \
    "That player wins the princess's heart and the game.               \n" \
    "                                                                  \n" \
    "                      -- Taking a Turn   --                       \n" \
    "On your turn, you get the top card from the deck and add it to    \n" \
    "your hand. Then choose one of the two cards in your hand and      \n" \
    "discard it face up in front of you. Apply any effect on the card  \n" \
    "you discarded. You must apply its effect, even if it is bad       \n" \
    "for you.                                                          \n" \
    "                                                                  \n" \
    "All discarded cards remain in front of the player who discarded   \n" \
    "them. Overlap the cards so that it's clear in which order they    \n" \
    "were discarded. This helps players to figure out which cards other\n" \
    "players might be holding. Once you finish applying the            \n" \
    "card's effect, the turn passes to the player on your left.        \n" \
    "                                                                  \n" \
    "                      -- Out of the Round --                      \n" \
    "If a player is knocked out of the round, that player discards     \n" \
    "the card in his or her hand face up (do not apply the card's      \n" \
    "effect) and takes no more turns until next round.                 \n" \
    "                                                                  \n" \
    "                      -- End of a Round --                        \n" \
    "A round ends if the deck is empty at the end of a turn. The       \n" \
    "royal residence closes for the evening, the person closest to     \n" \
    "the princess delivers the love letter, and Princess Annette       \n" \
    "retires to her chambers to read it.                               \n" \
    "                                                                  \n" \
    "All players still in the round reveal their hands. The player     \n" \
    "with the highest ranked person wins the round. In case of a tie,  \n" \
    "the player who discarded the highest total value of cards wins.   \n" \
    "A round also ends if all players but one are out of the round,    \n" \
    "in which case the remaining player wins.                          \n" \
    "The winner receives a token of affection.                         \n" \
    "We shuffle all 16 cards together, and play a new round following  \n" \
    "all of the setup rules.                                           \n" \
    "                                                                  \n" \
    "                      -- End of the game --                       \n" \
    "A player wins the game after winning a number of tokens based     \n" \
    "on the server rules.\n"
    "                                      \n"
    "PD: A typing error can cost you dear... so be extremely careful!  \n"
    "__________________________________________________________________\n" 
    "__________________________________________________________________\n")

def card():
    print("Card      ST  #               Effects\n"
          "Guard      1  5   Player designates another player and names a\n"
          "                  type of card. If that player's hand matches\n"
          "                  the type of card specified, that player is \n"
          "                  eliminated from the round. However, Guard cannot\n"
          "                  be named as the type of card.\n"
          "Priest     2  2   Player is allowed to see another player's hand.\n"
          "Baron      3  2   Player will choose another player and privately\n"
          "                  compare hands. The player with the lower-strength\n"
          "                  hand is eliminated from the round.\n"
          "Handmaid   4  2   Player cannot be affected by any other player's\n"
          "                  card until the next turn.\n"
          "Prince     5  2   Player can choose any player (including themselves)\n"
          "                  to discard their hand and draw a new one. If the\n"
          "                  discarded card is the Princess, the discarding player\n"
          "                  is eliminated.\n"
          "King       6  1   Player trades hands with any other player.\n"
          "Countess   7  1   If a player holds both this card and either the King\n"
          "                  or Prince card, this card must be played immediately.\n"
          "Princess   8  1   If a player plays this card for any reason, they are \n"
          "                  eliminated from the round.\n")

def simbolo():
    print("hey")

#rules()