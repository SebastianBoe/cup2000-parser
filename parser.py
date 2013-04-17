# This Python file uses the following encoding: utf-8

#oops remember W.O case

class Result:
    pass

def readIntoMemory(file):
    finished_matches = [] 
    unfinished_matches = []
    file.readline() #ignore first line
    for line in file:
        line = line.replace('"', "") #remove quote marks
        l = line.split(";") #parse into list
        l = l[:-1] #ignore last element
        
        result = Result()
        result.nr = l[0]
        result.rekke = l[1]
        result.kategori = l[2]
        result.navn1 = l[4]
        result.navn2 = l[6]
        result.score = l[7]
        if result.score:
            if l[8] == l[3]:
                result.winner = l[4]
                result.loser = l[6]
            else:
                result.winner = l[6]
                result.loser = l[4]

        if result.score:
            finished_matches.append(result)
        else:
            unfinished_matches.append(result)

    finished_file = open("finished_matches.html", "w")
    unfinished_file = open("unfinished_matches.html", "w")
    finished_matches.reverse()
    create_html(finished_matches, finished_file)
    finished_file.close()
    
    create_html(unfinished_matches, unfinished_file)
    unfinished_file.close()

def surround(d):
    return "<td>" + d + "</td>\n"

prefix = '<!DOCTYPE html>\n<html>\n<head><style type="text/css">\n<!--\n@import url("style.css");\n--></style></head><body>\n'

suffix = "\n</body>\n</html>\n"
def create_html(matches, f):
    f.write(prefix)
    f.write('<img alt="Logo" src="./logo.png">')
    if matches and matches[0].score:
        f.write("<h1>Ferdigspilte kamper</h1>")
    else:
        f.write("<h1>Spillende og kommende kamper</h1>")

    f.write('<table>\n')
    f.write('<col width="100px"><col width="140px">')
    f.write('<thead><tr><th>Kamp nr.</th><th>Klasse</th>')
    if matches and matches[0].score:
        f.write('<th>Vinner</th><th>Taper</th>')
        f.write('<th>Resultat</th>')
    else:
        f.write('<th>Spiller 1</th><th>Spiller 2</th>')
    f.write('</tr></thead>\n')

    for m in matches:
        f.write("<tr>\n")
        f.write(surround(m.nr))
        f.write(surround(m.kategori + " " + m.rekke))
        if not m.score:
            f.write(surround(m.navn1)) 
            f.write(surround(m.navn2))

        if m.score:
            f.write(surround(m.winner))
            f.write(surround(m.loser))
            f.write(surround(m.score))
        
        f.write("</tr>\n")
    f.write("</table>\n")

readIntoMemory(open("resultater.csv", "r"))
