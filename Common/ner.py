from yargy import Parser, rule, and_
from yargy.predicates import gram, is_capitalized, dictionary

UNIVERSITY = rule(
    dictionary({
    'пнипу',
    'политех',
    'вуз',
    'полик',
    'пгту',
    'универ',
    'университет',
    'институт'
    })
)

ETF = rule(
    dictionary({
    	'электротех',
    	'электротехнический',
	'этф',
	'электротехнический факультет'
    })
)

HOSTEL = rule(
    dictionary({
    	'общежитие',
    	'общага'
    })
)

GNF = rule(
    dictionary({
    	'гнф',
	'горный',
	'горно-нефтяной',
	'горно нефтяной',
	'нефтяной',
	'горнонефтяной'
    })
)

GUMF = rule(
    dictionary({
    	'гум',
    	'гумфак',
	'гуманитарный',
	'гуманитарный факультет'
    })
)

SCHOLARSHIP = rule(
    dictionary({
    	'стипендия',
    	'стипа',
    	'стипуха'
    })
)

G_SCHOLARSHIP = rule(
    dictionary({
    	'губернаторская стипендия',
    	'губер'
    })
)

MILITARY_DEPT = rule(
    dictionary({
    	'военная кафедра'
    })
)

MEDICAL_DOC = rule(
    dictionary({
    	'мед справка',
    	'мёд справка',
    	'медицинская справка',
    	'086-у',
    })
)

rules = {
	"УНИВЕРСИТЕТ": UNIVERSITY,
	"ЭТФ": ETF,"GNF": GNF,
	"ГумФ": GUMF,
	"СТИПЕНДИЯ": SCHOLARSHIP,
	"ГУБЕР_СТИПЕНДИЯ": G_SCHOLARSHIP,
	"ВОЕННАЯ_КАФЕДРА": MILITARY_DEPT,
	"МЕДИЦИНСКАЯ_СПРАВКА": MEDICAL_DOC,
    "ОБЩЕЖИТИЕ": HOSTEL
}




