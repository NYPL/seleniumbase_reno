from seleniumbase import BaseCase


class BlogAllPage(BaseCase):
    explore_by = '//*[@id="search-filters--heading"]'
    search_results = '//*[@id="search-results-details"]'

    clear_all_search_terms = '//*[@id="search-results-details__button"]'

    channels = '//*[@id="multiselect-channel"]/button'
    channel_links = '//*[@id="multiselect-channel"]/div/ul'
    clear_channel = '//*[@id="multiselect-button-clear-channel"]'
    apply_channel = '//*[@id="multiselect-button-save-channel"]'
    asian_american = '//*[contains(text(), "Asian American & Pacific Islander Culture")]'

    subjects = '//*[@id="multiselect-subject"]/button'
    apply_subject = '//*[@id="multiselect-button-save-subject"]'

    libraries = '//*[@id="multiselect-library"]/button'
    apply_library = '//*[@id="multiselect-button-save-library"]'
    clear_library = '//*[@id="multiselect-button-clear-library"]'

    divisions = '//*[@id="multiselect-division"]/button'
    apply_division = '//*[@id="multiselect-button-save-division"]'
    clear_division = '//*[@id="multiselect-button-clear-division"]'

    audience = '//*[@id="multiselect-audience_by_age"]/button'
    apply_audience = '//*[@id="multiselect-button-save-audience_by_age"]'
    clear_audience = '//*[@id="multiselect-button-clear-audience_by_age"]'

    adults = '//*[@id="multiselect-audience_by_age"]/div/ul/li[1]/label/span[2]'
    kids = '//*[@id="multiselect-audience_by_age"]/div/ul/li[2]/label/span[2]'
    teens = '//*[@id="multiselect-audience_by_age"]/div/ul/li[3]/label/span[2]'

    li_dic = {"asian_american": '//*[contains(text(), "Asian American & Pacific Islander Culture")]'
        , "biography": '//*[contains(text(), "Biography & Memoir")]',
              "black_culture": '//*[@id="multiselect-channel"]/div/ul/li[3]/label/span[2]',
              "book_lists": '//*[@id="multiselect-channel"]/div/ul/li[4]/label/span[2]',
              "comics_graphic": '//*[@id="multiselect-channel"]/div/ul/li[5]/label/span[2]',
              "digital_collections": '//*[@id="multiselect-channel"]/div/ul/li[6]/label/span[2]',
              "doc_chat": '//*[@id="multiselect-channel"]/div/ul/li[7]/label/span[2]',
              "early_literacy": '//*[@id="multiselect-channel"]/div/ul/li[8]/label/span[2]',
              "espanol_spanish": '//*[@id="multiselect-channel"]/div/ul/li[9]/label/span[2]',
              "for_kids": '//*[@id="multiselect-channel"]/div/ul/li[10]/label/span[2]',
              "for_teachers": '//*[@id="multiselect-channel"]/div/ul/li[11]/label/span[2]',
              "for_teens": '//*[@id="multiselect-channel"]/div/ul/li[12]/label/span[2]',
              "francais_french": '//*[@id="multiselect-channel"]/div/ul/li[13]/label/span[2]',
              "hispanic_latinx": '//*[@id="multiselect-channel"]/div/ul/li[14]/label/span[2]',
              "horror": '//*[@id="multiselect-channel"]/div/ul/li[15]/label/span[2]',
              "lgbtq+": '//*[@id="multiselect-channel"]/div/ul/li[16]/label/span[2]',
              "library_stories": '//*[@id="multiselect-channel"]/div/ul/li[17]/label/span[2]',
              "library_talks": '//*[@id="multiselect-channel"]/div/ul/li[18]/label/span[2]',
              "mysteries_crime": '//*[@id="multiselect-channel"]/div/ul/li[19]/label/span[2]',
              "nonfiction": '//*[@id="multiselect-channel"]/div/ul/li[20]/label/span[2]',
              "poetry": '//*[@id="multiselect-channel"]/div/ul/li[21]/label/span[2]',
              "popular_culture": '//*[@id="multiselect-channel"]/div/ul/li[22]/label/span[2]',
              "research_at_nypl": '//*[@id="multiselect-channel"]/div/ul/li[23]/label/span[2]',
              "romance": '//*[@id="multiselect-channel"]/div/ul/li[24]/label/span[2]',
              "science_fiction": '//*[@id="multiselect-channel"]/div/ul/li[25]/label/span[2]',
              "the_librarian": '//*[@id="multiselect-channel"]/div/ul/li[26]/label/span[2]',
              "women's_history": '//*[@id="multiselect-channel"]/div/ul/li[27]/label/span[2]',
              "work_cited": '//*[@id="multiselect-channel"]/div/ul/li[28]/label/span[2]',
              "chinese_language": '//*[@id="multiselect-channel"]/div/ul/li[29]/label/span[2]',

              "art": '//*[@id="multiselect-subject"]/div/ul/li[1]/label/span[2]',
              "business": '//*[@id="multiselect-subject"]/div/ul/li[2]/label/span[2]',
              "genealogy": '//*[@id="multiselect-subject"]/div/ul/li[3]/label/span[2]',
              "history": '//*[@id="multiselect-subject"]/div/ul/li[4]/label/span[2]',
              "nyc_history": '//*[@id="multiselect-subject"]/div/ul/li[5]/label/span[2]',
              "performing_arts": '//*[@id="multiselect-subject"]/div/ul/li[6]/label/span[2]',
              "science": '//*[@id="multiselect-subject"]/div/ul/li[7]/label/span[2]'
              }

    location_dic = {'Art & Architecture Collection': 'Stephen A. Schwarzman Building',
                    'Art and Artifacts Division': 'Schomburg Center for Research in Black Culture',
                    'Billy Rose Theatre Division': 'The New York Public Library for the Performing Arts',
                    'Carl H. Pforzheimer Collection of Shelley and His Circle': 'Stephen A. Schwarzman Building',
                    'DeWitt Wallace Periodical Room': 'Stephen A. Schwarzman Building',
                    'Dorot Jewish Division': 'Stephen A. Schwarzman Building',
                    'General Research Division': 'Stephen A. Schwarzman Building',
                    'George Arents Collection': 'Stephen A. Schwarzman Building',
                    'Henry W. and Albert A. Berg Collection of English and American Literature': 'Stephen A. Schwarzman Building',
                    'Irma and Paul Milstein Division of United States History, Local History and Genealogy': 'Stephen A. Schwarzman Building',
                    'Jean Blackwell Hutson Research and Reference Division': 'Schomburg Center for Research in Black Culture',
                    'Jerome Robbins Dance Division': 'The New York Public Library for the Performing Arts',
                    'Lionel Pincus and Princess Firyal Map Division': 'Stephen A. Schwarzman Building',
                    'Manuscripts and Archives Division': 'Stephen A. Schwarzman Building',
                    'Manuscripts, Archives and Rare Books Division': 'Schomburg Center for Research in Black Culture',
                    'Moving Image and Recorded Sound Division': 'Schomburg Center for Research in Black Culture',
                    'Music Division': 'The New York Public Library for the Performing Arts',
                    'Photographs and Prints Division': 'Schomburg Center for Research in Black Culture',
                    'Photography Collection': 'Stephen A. Schwarzman Building',
                    'Picture Collection': 'Stephen A. Schwarzman Building',
                    'Print Collection': 'Stephen A. Schwarzman Building',
                    'Rare Book Division': 'Stephen A. Schwarzman Building',
                    'Spencer Collection': 'Stephen A. Schwarzman Building',
                    'The Rodgers and Hammerstein Archives of Recorded Sound': 'The New York Public Library for the Performing Arts',
                    'Theatre on Film and Tape Archive': 'The New York Public Library for the Performing Arts'}

    def open_blog_page(self):
        # self.open("https://www.nypl.org/blog/all")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/blog/all")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/blog/all")

