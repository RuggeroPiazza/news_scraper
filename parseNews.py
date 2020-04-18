from classProjectNews import NEWS


def parsing_bbc():
    url = "https://www.bbc.co.uk/"
    tag = "span"
    tag_class = "top-story__title"
    bbc = NEWS(url, tag, tag_class)
    res = bbc.requesting()
    soup = bbc.creating_bs_obj(res)
    bbc.writing_data(soup)


def parsing_google_news():
    url = "https://news.google.com/?hl=en-GB&gl=GB&ceid=GB%3Aen"
    tag = "a"
    tag_class = "DY5T1d"
    google = NEWS(url, tag, tag_class)
    res = google.requesting()
    soup = google.creating_bs_obj(res)
    google.writing_data(soup)


if __name__ == "__main__":
    parsing_bbc()
    parsing_google_news()
