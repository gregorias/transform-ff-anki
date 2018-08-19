#!/usr/bin/env python3
"""Transform cards from "Fluent Forever" to my format."""
# Download https://github.com/dae/anki and extract anki/anki
import anki
col = anki.Collection('grzesiek/collection.anki2')
minimal_pair_model = col.models.byName('MinimalPair')
gmp_notes = col.findNotes('"deck:Foreign Languages::*German Minimal Pairs*"')
german_deck = col.decks.byName('Foreign Languages::German')
processed = set()
for gmp_note in [col.getNote(n_id) for n_id in gmp_notes]:
    gmp_note_fields = dict(gmp_note.items())
    new_note = anki.notes.Note(col, minimal_pair_model)
    new_note.model()['did'] = german_deck['id']
    new_note.fields[0] = gmp_note_fields['Recording 1']
    new_note.fields[1] = '{0}<br/>/{1}/'.format(
        gmp_note_fields['Word 1'],
        gmp_note_fields['Word 1 IPA'],)
    new_note.fields[2] = gmp_note_fields['Recording 2']
    new_note.fields[3] = '{0}<br/>/{1}/'.format(
        gmp_note_fields['Word 2'],
        gmp_note_fields['Word 2 IPA'],)
    new_note_key = (new_note.fields[0], new_note.fields[1])
    if new_note_key not in processed:
        col.addNote(new_note)
        processed.add(new_note_key)

picture_words_model = col.models.byName('Final 2. Picture Words')
basic_fb_model = col.models.byName('BasicFB')
pwm_notes = [col.getNote(id) for id in
             col.findNotes('mid:' + str(picture_words_model['id']))]
for pwm_note in pwm_notes:
    pwm_note_fields = dict(pwm_note.items())
    new_note = anki.notes.Note(col, basic_fb_model)
    new_note.model()['did'] = german_deck['id']
    new_note.fields[0] = '{0}<br/>/{1}/<br/>{2}'.format(
        pwm_note_fields['Word with Article'],
        pwm_note_fields['IPA for Word'],
        pwm_note_fields['Recording of the Word'],)
    new_note.fields[1] = '{0}<br/>{1}'.format(
        pwm_note_fields['Picture of the example word'],
        pwm_note_fields['English Translation'],)
    col.addNote(new_note)
col.close()
