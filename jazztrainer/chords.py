# JazzTrainer - a tool to learn jazz chords
# Copyright (C) 2010 Emil Loer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# chord record structure: (category,[[chord name, chord symbol, list of intervals]])

sharp=u"\u266f"
flat=u"\u266d"

# chord catalog
chords = [
	("Triads",[
		["Major",					"",				["1","3","5"]],
		["Minor",					"m",			["1","b3","5"]],
		["Augmented",				"+",			["1","3","#5"]],
		["Diminished",				"dim",			["1","b3","b5"]],
		["Suspended",				"sus4",			["1","4","5"]],
		["Major, flatted fifth",	"("+flat+"5)",	["1","3","b5"]],
	]),

	("Triads, first inversion",[
		["Major",					"",				["3","5","o1"]],
		["Minor",					"m",			["b3","5","o1"]],
		["Augmented",				"+",			["3","#5","o1"]],
		["Diminished",				"dim",			["b3","b5","o1"]],
		["Suspended",				"sus4",			["4","5","o1"]],
		["Major, flatted fifth",	"("+flat+"5)",	["3","b5","o1"]],
	]),

	("Triads, second inversion",[
		["Major",					"",				["5","o1","o3"]],
		["Minor",					"m",			["5","o1","ob3"]],
		["Augmented",				"+",			["#5","o1","o3"]],
		["Diminished",				"dim",			["b5","o1","ob3"]],
		["Suspended",				"sus4",			["5","o1","o4"]],
		["Major, flatted fifth",	"("+flat+"5)",	["b5","o1","o3"]],
	]),

	# triads with octave
	# triads with octave, first inversion
	# triads with octave, second inversion

	("Close position chords",[
		["Major 6th",				"6",["1","3","5","6"]],
		["Major 7th",				"maj7",["1","3","5","7"]],
		["Minor 6th",				"m6",["1","b3","5","6"]],
		["Minor 7th",				"m7",["1","b3","5","b7"]],
		["Half diminished 7th",		"m7"+flat+"5",["1","b3","b5","b7"]],
		["Diminished 7th",			"dim7",["1","b3","b5","bb7"]],
		["Dominant 7th",			"7",["1","3","5","b7"]],
		["Minor/major 7th",			"m/maj7",["1","b3","5","7"]],
		["Suspended dominant 7th",	"7sus4",["1","4","5","b7"]],
	]),

	# drop 2 voicing, rooted
	# drop 2 voicing, rootless
	# drop 3 voicing, rooted
	# drop 3 voicing, rootless

	# guide tones (3/7)
	("Guide tones (3rd and 7th)",[
		["Major 7th",				"maj7",			["3","7"]],
		["Minor 7th",				"m7",			["b3","b7"]],
		["Half diminished 7th",		"m7"+flat+"5",	["b3","b7"]],
		["Diminished 7th",			"dim7",			["b3","bb7"]],
		["Dominant 7th",			"7",			["3","b7"]],
		["Minor/major 7th",			"m/maj7",		["b3","7"]],
		["Suspended dominant 7th",	"7sus4",		["4","b7"]],
	]),

	("Bud Powell rooted shells",[
		["Major 6th",				"6",		["1","3","6"]],
		["Major 7th",				"maj7",		["1","3","7"]],
		["Minor 6th",				"m6",		["1","b3","6"]],
		["Minor 7th",				"m7",		["1","b3","b7"]],
		["Minor/major 7th",			"m/maj7",	["1","b3","7"]],
		["Dominant 7th",			"7",		["1","3","b7"]],
		["Suspended dominant 7th",	"7sus4",	["1","4","b7"]],
	]),

	# rootless three note

	("Bill Evans rootless voicings",[
		["Major 6/9 (Type A)",							"6/9 (Type A)",						["3","5","6","9"]],
		["Major 6/9 (Type B)",							"6/9 (Type B)",						["6","9","o3","o5"]],
		["Major 9th (Type A)",							"maj9 (Type A)",					["3","5","7","9"]],
		["Major 9th (Type B)",							"maj9 (Type B)",					["7","9","o3","o5"]],
		["Major 13th (Type A)",							"maj13 (Type A)",					["3","6","7","9"]],
		["Major 13th (Type B)",							"maj13 (Type B)",					["7","9","o3","o5"]],
		["Minor 6/9 (Type A)",							"m6/9 (Type A)",					["b3","5","6","9"]],
		["Minor 6/9 (Type B)",							"m6/9 (Type B)",					["6","9","ob3","o5"]],
		["Minor 9th (Type A)",							"m9 (Type A)",						["b3","5","b7","9"]],
		["Minor 9th (Type A)",							"m9 (Type B)",						["b7","9","ob3","o5"]],
		["Minor 13th (Type A)",							"m13 (Type A)",						["b3","6","7","9"]],
		["Minor 13th (Type B)",							"m13 (Type B)",						["7","9","ob3","o5"]],
		["Minor/major 9th (Type A)",					"m/maj9 (Type A)",					["b3","5","7","9"]],
		["Minor/major 9th (Type B)",					"m/maj9 (Type B)",					["7","9","ob3","o5"]],
		["Dominant 7th, sharp 5th, sharp 9th (Type A)",	"7"+sharp+"5"+sharp+"9 (Type A)",	["3","#5","b7","#9"]],
		["Dominant 7th, sharp 5th, sharp 9th (Type B)",	"7"+sharp+"5"+sharp+"9 (Type B)",	["b7","#9","o3","o#5"]],
		["Dominant 7th, sharp 5th, flat 9th (Type A)",	"7"+sharp+"5"+flat+"9 (Type A)",	["3","#5","b7","b9"]],
		["Dominant 7th, sharp 5th, flat 9th (Type B)",	"7"+sharp+"5"+flat+"9 (Type B)",	["b7","b9","o3","o#5"]],
		["Dominant 9th (Type A)",						"9 (Type A)",						["3","5","b7","9"]],
		["Dominant 9th (Type B)",						"9 (Type B)",						["b7","9","o3","o5"]],
		["Dominant 13th (Type A)",						"13 (Type A)",						["3","6","b7","9"]],
		["Dominant 13th (Type B)",						"13 (Type B)",						["b7","9","o3","o6"]],
		["Dominant 13th, flat 9th (Type A)",			"13"+flat+"9 (Type A)",				["3","6","b7","b9"]],
		["Dominant 13th, flat 9th (Type B)",			"13"+flat+"9 (Type B)",				["b7","b9","o3","o6"]],
		["Half diminished 7th (Type A)",				"m7"+flat+"5 (Type A)",				["b3","b5","b7","o1"]],
		["Half diminished 7th (Type B)",				"m7"+flat+"5 (Type B)",				["b7","o1","ob3","ob5"]],
		["Half diminished 7th, flat 9th (Type A)",		"m7"+flat+"5"+flat+"9 (Type A)",	["b3","b5","b7","b9"]],
		["Half diminished 7th, flat 9th (Type B)",		"m7"+flat+"5"+flat+"9 (Type B)",	["b7","b9","ob3","ob5"]],
		["Half diminished 9th (Type A)",				"m9"+flat+"5 (Type A)",				["b3","b5","b7","9"]],
		["Half diminished 9th (Type B)",				"m9"+flat+"5 (Type B)",				["b7","9","ob3","ob5"]],
	]),

	# two hand voicings page 77

	("Quartal voicings",[
		["So What chord",		"m7sus4",					["1","4","b7","ob3","o5"]],
		["",					"7sus4 quartal one hand",	["1","4","b7"]],
		["",					"m7sus4 two hand quartal",	["1","b3","6","9","o5"]],
		["Kenny Barron chord",	"m11",						["1","5","9","ob3","ob7","o11"]],
	]),

]

# scale catalog
scales=[
	# Major scale modes
	("Ionian (Major scale)",	["1","2","3","4","5","6","7"]),
	("Dorian",					["1","2","b3","4","5","6","b7"]),
	("Phrygian",				["1","b2","b3","4","5","b6","b7"]),
	("Lydian",					["1","2","3","#4","5","6","7"]),
	("Mixolydian",				["1","2","3","4","5","6","b7"]),
	("Aeolian (Minor scale)",	["1","2","b3","4","5","b6","b7"]),
	("Locrian",					["1","b2","b3","4","b5","b6","b7"]),

	# Pentatonic/blues scales
	("Blues scale",				["1","b3","4","b5","5","b7"]),
	("Major pentatonic",		["1","2","3","5","6"]),
	("Minor pentatonic",		["1","b3","4","5","b7"]),
	# TODO: in sen, kumoi, others

	# Diminished scales
	("Diminished whole-half",	["1","2","b3","4","b5","#5","6","7"]),
	("Diminished half-whole",	["1","b2","b3","3","b5","5","6","b7"]),

	# Melodic minor scale modes
	("Melodic minor",			["1","2","b3","4","5","6","7"]),
	# TODO: modes here

	# Other
	("Whole tone",				["1","2","3","b5","b6","b7"]),
	# TODO: neapolitan, gypsy scales, 
]

# scale degrees and offsets for the first octave
degrees=[
	("1",0),
	("b2",1),
	("2",2),
	("#2",3),("b3",3),
	("3",4),("b4",4),
	("4",5),("#3",5),
	("b5",6),("#4",6),
	("5",7),
	("#5",8),("b6",8),
	("6",9),("bb7",9),
	("b7",10),("#6",10),
	("7",11),
	("8",12),
	("b9",13),
	("9",14),
	("#9",15),("b10",15),
	("10",16),("b11",16),
	("11",17),("#10",17),
	("#11",18),("b12",18),
	("12",19),
	("#12",20),("b13",20),
	("13",21),
	("b14",22),("#13",22),
	("14",23),
	("15",24),
	("b16",25),
	("16",26),
	("#16",27),("b17",27),
	("17",28),("b18",28),
	("18",29),("#17",29),
]

# scale degrees and offsets for three octaves
offsets=dict(degrees+[("o"+a,12+b) for (a,b) in degrees]+[("oo"+a,24+b) for (a,b) in degrees])

notes=[["C"],["C"+sharp,"D"+flat],["D"],["D"+sharp,"E"+flat],["E"],["F"],["F"+sharp,"G"+flat],["G"],["G"+sharp,"A"+flat],["A"],["A"+sharp,"B"+flat],["B"]]
