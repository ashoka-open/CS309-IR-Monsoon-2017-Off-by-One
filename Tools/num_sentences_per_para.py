from Tools import sentence_count


def sentences_per_paragraph(paragraphs):
    sent_count = []
    for para in paragraphs:
        if para != "":
            sent_count.append(sentence_count.sentence_count(para))

    # array containing number of sentences in each paragraph.
    # sent_count[1] will be number of sentences in paragraph 1
    return sent_count
