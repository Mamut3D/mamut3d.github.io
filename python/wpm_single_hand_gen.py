#!/usr/bin/env python3

# importing random module
import random
import json
import argparse
import sys

parser = argparse.ArgumentParser(description="Generator of randomized lessons for python wpm package. Lessons are generated for each hand separately",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-w", "--word-count", type=int, default=100, help="number of words per lesson")
parser.add_argument("-p", "--permutations", type=int, default=20, help="number of random word permutations per json")
parser.add_argument("-H", "--hand", choices=['left', 'right'], default='left')
args = parser.parse_args()
config = vars(args)

right_hand_words = [
    'hillo', 'hilly', 'hilum', 'hinny', 'hippo', 'hippy', 'hokily', 'hokku', 'hokum',
    'hokypoky', 'holily', 'hollo', 'holloo', 'holly', 'holmium', 'homily', 'hominy', 'homonym',
    'homonymy', 'homophony', 'honky', 'hookup', 'hooky', 'hooly', 'hoopoo', 'hoppy', 'huipil',
    'hulky', 'hullo', 'humph', 'humpy', 'hunky', 'hypolimnion', 'hypopyon', 'ilium', 'illinium',
    'imino', 'imply', 'inion', 'inulin', 'ionium', 'jillion', 'jiminy', 'jimminy', 'jimmy',
    'jimply', 'jimpy', 'jinni', 'johnny', 'jokily', 'jollily', 'jolly', 'joypop', 'jumpily',
    'jumpy', 'junky', 'jupon', 'khoum', 'kilim', 'killjoy', 'kimono', 'kinin', 'kinkily',
    'kinky', 'knoll', 'knolly', 'kooky', 'limpkin', 'limply', 'limuli', 'linin', 'linkup',
    'linky', 'linum', 'lipin', 'lippy', 'lollipop', 'lollop', 'lolly', 'lollypop', 'lookup',
    'loony', 'loopy', 'loppy', 'lumpily', 'lumpy', 'lupin', 'lupulin', 'lymph', 'milium',
    'milkily', 'milky', 'millimho', 'milliohm', 'million', 'minikin', 'minim', 'minimill', 'minimum',
    'minion', 'minium', 'minny', 'molly', 'mommy', 'monohull', 'monophony', 'monophyly', 'monopoly',
    'moonily', 'moony', 'moujik', 'moulin', 'muhly', 'mujik', 'mukluk', 'mullion', 'mummy',
    'munnion', 'muonium', 'muumuu', 'myopy', 'nihil', 'ninny', 'ninon', 'nippily', 'nippy',
    'noily', 'nomoi', 'nonillion', 'nonoily', 'nonunion', 'nonyl', 'nooky', 'nylon', 'nymph',
    'nympho', 'oilily', 'onion', 'oniony', 'onium', 'oomph', 'opinion', 'opium', 'phonily',
    'phono', 'phonon', 'phony', 'phyllo', 'phylon', 'phylum', 'pillion', 'pimply', 'pinion',
    'pinkly', 'pinko', 'pinky', 'pinny', 'pinon', 'pinup', 'pinyin', 'pinyon', 'pipkin',
    'pippin', 'plink', 'plonk', 'plummy', 'plump', 'plumply', 'plumy', 'plunk', 'poilu',
    'pokily', 'polio', 'pollinium', 'polonium', 'polynyi', 'polyp', 'polyphony', 'polypi', 'pommy',
    'pompom', 'pompon', 'poplin', 'poppy', 'poyou', 'pulik', 'pullup', 'pulpily', 'pulpy',
    'pumpkin', 'punily', 'punkin', 'punky', 'punny', 'pupil', 'puppy', 'pylon', 'unhip',
    'unholily', 'unholy', 'unhook', 'union', 'unkink', 'unlink', 'unpin', 'uphill', 'uplink',
    'yolky', 'yomim', 'youpon', 'yummy', 'yupon'
]
left_hand_words = [
    'Edgar', 'strawberry', 'rest', 'baste', 'sarge', 'badger', 'dab', 'bad', 'brew',
    'brave', 'bear', 'ted', 'fade', 'vested', 'trade', 'sax', 'rear', 'reader',
    'read', 'sad', 'grade', 'crew', 'start', 'caste', 'cast', 'straw', 'taser',
    'wax', 'sweater', 'swear', 'date', 'database', 'retested', 'assert', 'asserted', 'adverse',
    'stargate', 'retreave', 'retarded', 'retard', 'dart', 'tears', 'tear', 'tea', 'feet',
    'frred', 'free', 'dew', 'cards', 'card', 'drax', 'draft', 'drew', 'fast',
    'sat', 'see', 'fears', 'feared', 'fear', 'far', 'tar', 'war', 'cart',
    'fart', 'fest', 'zest', 'west', 'sass', 'ass', 'dear', 'draw', 'freeze',
    'stabbed', 'deface', 'crest', 'seat', 'tewater', 'grass', 'grease', 'race', 'Swedes',
    'Qatar', 'Greece', 'verde', 'terse', 'tweed', 'east', 'gas', 'as', 'geez',
    'we', 'tree', 'faster', 'reverberate', 'cascade', 'greatest', 'accrete', 'abracadabra', 'defaced',
    'weedeater', 'redfaced', 'barge', 'tweet', 'retract', 'drag', 'gaff', 'vest', 'vast',
    'wart', 'starve', 'dread', 'wage', 'were', 'water', 'te', 'affect', 'effect',
    'strafe', 'grave', 'crave', 'farce', 'Stewart', 'ave', 'caves', 'veer', 'Avesta',
    'staves', 'sex', 'starter', 'exec', 'crested', 'greed', 'great', 'badge', 'bastard',
    'gated', 'age', 'drear', 'treat', 'eaves', 'zed', 'vexes', 'crater', 'stress',
    'dressed', 'created', 'waver', 'qat', 'wrest', 'axes', 'waves', 'red', 'tea'
]

if args.hand == 'left':
    if len(left_hand_words) < args.word_count:
        sys.exit('Number of left hand words selected for permutatios must be lower or equal to ' + str(len(left_hand_words)))
    seed = left_hand_words
else:
    if len(right_hand_words) < args.word_count:
        sys.exit('Number of right hand words selected for permutatios must be lower or equal to ' + str(len(right_hand_words)))
    seed = right_hand_words
result = []

for i in range(args.permutations):
    word_perm_array = random.sample(seed, args.word_count)
    word_perm_tmp = {
        "author": "The Internet",
        "title": "Single hand beating",
        "text": " ".join(word_perm_array)
    }
    result.append(word_perm_tmp)

print(json.dumps(result,indent=4))
